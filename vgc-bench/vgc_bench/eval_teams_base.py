import argparse
import asyncio
import os
import random
from statistics import mean, median

import numpy as np
from poke_env import cross_evaluate
from poke_env.player import MaxBasePowerPlayer, RandomPlayer, SimpleHeuristicsPlayer
from poke_env.ps_client import AccountConfiguration, ServerConfiguration
from src.llm import LLMPlayer
from src.policy_player import BatchPolicyPlayer
from src.teams import RandomTeamBuilder, calc_team_similarity_score, get_team_paths
from src.test_teams import TestTeamBuilder, calc_team_similarity_score, get_team_paths
from src.utils import format_map
from stable_baselines3 import PPO
from tensorboard.backend.event_processing import event_accumulator

def cross_eval_simple(
    battle_format: str,
    num_teams_1: int,
    num_teams_2: int,
    port: int,
    device: str,
    num_battles: int,
    num_llm_battles: int,
):
    agent = SimpleHeuristicsPlayer(
        account_configuration=AccountConfiguration("SHPlayer1", None),
        server_configuration=ServerConfiguration(
            f"ws://localhost:{port}/showdown/websocket",
            "https://play.pokemonshowdown.com/action.php?",
        ),
        battle_format="gen9vgc2026regf",
        log_level=25,
        max_concurrent_battles=10,
        accept_open_team_sheet=True,
        open_timeout=None,
        team=TestTeamBuilder(1, num_teams_1, battle_format, 10, 1),
    )
    opponent = SimpleHeuristicsPlayer(
        account_configuration=AccountConfiguration("SHPlayer2", None),
        server_configuration=ServerConfiguration(
            f"ws://localhost:{port}/showdown/websocket",
            "https://play.pokemonshowdown.com/action.php?",
        ),
        battle_format="gen9vgc2026regf",
        log_level=25,
        max_concurrent_battles=10,
        accept_open_team_sheet=True,
        open_timeout=None,
        team=TestTeamBuilder(1, num_teams_2, battle_format, 11, 42),
    )
    awin = []
    owin = []
    total_battles = 0
    for i in range(5):
        results = asyncio.run(agent.battle_against(opponent, n_battles=num_battles))
        print(f"Agent won {agent.n_won_battles} out of {agent.n_finished_battles} played")
        print(f"Opponent won {opponent.n_won_battles} out of {opponent.n_finished_battles} played")
        awin.append(agent.n_won_battles)
        owin.append(opponent.n_won_battles)
    for i in range(5):
        print(f"Agent won {agent.n_won_battles} out of {agent.n_finished_battles} played")
        print(f"Opponent won {opponent.n_won_battles} out of {opponent.n_finished_battles} played")
        

def cross_eval_advanced(
    battle_format: str,
    num_teams: int,
    port: int,
    device: str,
    num_battles: int,
    num_llm_battles: int,
):
    num_runs = 5
    for run_id in range(1, num_runs + 1):
        best_checkpoints = asyncio.run(
            get_best_checkpoints(battle_format, run_id, num_teams, port, device, num_battles)
        )
        method = best_checkpoints[0]
        checkpoint = best_checkpoints[1]
        agent = BatchPolicyPlayer(
            account_configuration=AccountConfiguration(f"{run_id}/{method}/{checkpoint}", None),
            server_configuration=ServerConfiguration(
                f"ws://localhost:{port}/showdown/websocket",
                "https://play.pokemonshowdown.com/action.php?",
            ),
            battle_format="gen9vgc2026regf",
            log_level=25,
            max_concurrent_battles=10,
            accept_open_team_sheet=True,
            open_timeout=None,
            team=TestTeamBuilder(1, num_teams_1, battle_format, 10, 1),
        )
        policy_path = f"results{run_id}/saves-{method}"
        if method != "bc":
            policy_path += f"/{num_teams}-teams"
        agent.policy = PPO.load(f"{policy_path}/{checkpoint}", device=device).policy
        opponent = BatchPolicyPlayer(
            account_configuration=AccountConfiguration(f"{run_id}/{method}/{checkpoint}", None),
            server_configuration=ServerConfiguration(
                f"ws://localhost:{port}/showdown/websocket",
                "https://play.pokemonshowdown.com/action.php?",
            ),
            battle_format="gen9vgc2026regf",
            log_level=25,
            max_concurrent_battles=10,
            accept_open_team_sheet=True,
            open_timeout=None,
            team=TestTeamBuilder(1, num_teams_2, battle_format, 11, 42),
        )
        policy_path = f"results{run_id}/saves-{method}"
        if method != "bc":
            policy_path += f"/{num_teams}-teams"
        opponent.policy = PPO.load(f"{policy_path}/{checkpoint}", device=device).policy
        results = asyncio.run(agent.battle_against(opponent, n_battles=num_battles // num_runs))
        print(f"Agent won {agent.n_won_battles} out of {agent.n_finished_battles} played")
        print(f"Opponent won {opponent.n_won_battles} out of {opponent.n_finished_battles} played")



async def get_best_checkpoints(
    battle_format: str,
    run_id: int,
    num_teams: int,
    port: int,
    device: str,
    num_battles: int,
    eval_pool_size: int = 50,
    cutoff: int = 5,
) -> dict[str, int]:
    best_checkpoints = {}
    save_policy = BatchPolicyPlayer(
        server_configuration=ServerConfiguration(
            f"ws://localhost:{port}/showdown/websocket",
            "https://play.pokemonshowdown.com/action.php?",
        ),
        battle_format="gen9vgc2026regf",
        log_level=25,
        max_concurrent_battles=10,
        accept_open_team_sheet=True,
        open_timeout=None,
        team=RandomTeamBuilder(run_id, num_teams, battle_format),
    )
    opponent = BatchPolicyPlayer(
        server_configuration=ServerConfiguration(
            f"ws://localhost:{port}/showdown/websocket",
            "https://play.pokemonshowdown.com/action.php?",
        ),
        battle_format="gen9vgc2026regf",
        log_level=25,
        max_concurrent_battles=10,
        accept_open_team_sheet=True,
        open_timeout=None,
        team=RandomTeamBuilder(run_id, num_teams, battle_format),
    )
    filess = [
        [
            f"results{run_id}/saves-{method}/924-teams/{file}"
            for file in sorted(
                os.listdir(f"results{run_id}/saves-{method}/924-teams"),
                key=lambda f: int(f[:-4]),
            )[cutoff:]
        ]
        for method in ["bc-do"]
    ]
    files = [f for files in filess for f in files]
    eval_pool_files = random.sample(files, eval_pool_size)
    for method in ["bc-do"]:
        data = extract_tb(f"results{run_id}/logs-{method}/924-teams_0", "train/eval")
        eval_scores = [d[1] for d in data]
        min_score = np.percentile(eval_scores, 90)
        best_indices = np.where(eval_scores >= min_score)[0][::-1]
        checkpoints = np.array([d[0] for d in data])[best_indices]
        win_rates = {}
        for checkpoint in checkpoints:
            save_policy.policy = PPO.load(
                f"results{run_id}/saves-{method}/924-teams/{checkpoint}", device=device
            ).policy
            for f in eval_pool_files:
                opponent.policy = PPO.load(f, device=device).policy
                await save_policy.battle_against(opponent, n_battles=num_battles // eval_pool_size)
            win_rates[checkpoint.item()] = save_policy.win_rate
            save_policy.reset_battles()
            opponent.reset_battles()
        print(
            f"comparison of agents with top-10% eval score from {method}: {win_rates}", flush=True
        )
        best_checkpoints[method] = max(list(win_rates.items()), key=lambda tup: tup[1])[0]
    print(f"best of run #{run_id}:", best_checkpoints, flush=True)
    return best_checkpoints


def extract_tb(event_file: str, tag_prefix: str) -> list[tuple[int, float]]:
    """
    Extract (x, y) pairs from TensorBoard event file's `tag_prefix` data,
    keeping only the most recent recording for each step (last occurrence)
    """
    ea = event_accumulator.EventAccumulator(event_file)
    ea.Reload()
    for tag in ea.Tags()["scalars"]:
        if tag.startswith(tag_prefix):
            scalars = ea.Scalars(tag)
            last_per_step: dict[int, float] = {}
            for s in scalars:
                last_per_step[int(s.step)] = round(s.value, ndigits=5)
            return sorted(last_per_step.items(), key=lambda kv: kv[0])
    raise FileNotFoundError()


def print_team_statistics(battle_format: str, num_teams: int):
    num_runs = 5
    all_teams = [path.read_text() for path in get_team_paths(battle_format)]
    sim_scores = [
        max(
            [
                calc_team_similarity_score(all_teams[i], all_teams[j])
                for i in range(len(all_teams))
                if i != j
            ]
        )
        for j in range(len(all_teams))
    ]
    print(
        "worst-case team similarities for each team across all teams:",
        f"mean = {round(mean(sim_scores), ndigits=3)},",
        f"median = {round(median(sim_scores), ndigits=4)},",
        f"min = {min(sim_scores)},",
        f"max = {max(sim_scores)}",
    )
    print(
        "worst-case team similarities of out-of-distribution teams",
        f"across in-distribution {num_teams} team set in...",
    )
    for run_id in range(1, num_runs + 1):
        teams = list(range(len(all_teams)))
        random.Random(run_id).shuffle(teams)
        sim_scores = [
            max([calc_team_similarity_score(all_teams[i], all_teams[j]) for i in teams[:num_teams]])
            for j in teams[num_teams:]
        ]
        print(
            f"run #{run_id}:",
            f"mean = {round(mean(sim_scores), ndigits=3)},",
            f"median = {round(median(sim_scores), ndigits=4)},",
            f"min = {min(sim_scores)},",
            f"max = {max(sim_scores)}",
        )

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Evaluate a Pokémon AI model")
    parser.add_argument("--reg", type=str, default="gen9vgc2025regh", help="VGC regulation to eval on, i.e. G")
    parser.add_argument("--num_teams_1", type=int, default=42, help="Number of teams to eval with")
    parser.add_argument("--num_teams_2", type=int, default=192, help="Number of teams to eval with")
    parser.add_argument("--port", type=int, default=8000, help="Port to run showdown server on")
    parser.add_argument(
        "--device",
        type=str,
        default="cuda:0",
        choices=["cuda:0", "cuda:1", "cuda:2", "cuda:3"],
        help="CUDA device to use for eval",
    )
    args = parser.parse_args()
    battle_format = args.reg.lower()
    #print_team_statistics(battle_format, args.num_teams)
    cross_eval_simple(battle_format, args.num_teams_1, args.num_teams_2, args.port, args.device, 8064, 100)

