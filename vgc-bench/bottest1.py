import numpy as np

team_1 = """
Incineroar @ Assault_Vest
Ability: Intimidate
Level: 50
Tera Type: Normal
EVs: 244 HP / 4 Atk / 76 Def / 0 SpA / 124 SpD / 60 Spe
Impish Nature
IVs: 31 HP / 31 Atk / 31 Def / 31 SpA / 31 SpD / 31 Spe
- Fake_Out
- Knock_Off
- Flare_Blitz
- U-turn

Primarina @ Focus_Sash
Ability: Liquid_Voice
Level: 50
Tera Type: Normal
EVs: 4 HP / 0 Atk / 0 Def / 252 SpA / 0 SpD / 252 Spe
Timid Nature
IVs: 31 HP / 0 Atk / 31 Def / 31 SpA / 31 SpD / 31 Spe
- Hyper_Voice
- Dazzling_Gleam
- Calm_Mind
- Water_Pledge

Sinistcha @ Rocky_Helmet
Ability: Hospitality
Level: 50
Tera Type: Normal
EVs: 252 HP / 0 Atk / 68 Def / 4 SpA / 180 SpD / 4 Spe
Calm Nature
IVs: 31 HP / 0 Atk / 31 Def / 31 SpA / 31 SpD / 31 Spe
- Matcha_Gotcha
- Trick_Room
- Life_Dew
- Strength_Sap

Gholdengo @ Life_Orb
Ability: Good_as_Gold
Level: 50
Tera Type: Normal
EVs: 4 HP / 0 Atk / 0 Def / 252 SpA / 0 SpD / 252 Spe
Timid Nature
IVs: 31 HP / 0 Atk / 31 Def / 31 SpA / 31 SpD / 31 Spe
- Make_It_Rain
- Shadow_Ball
- Nasty_Plot
- Power_Gem

Garchomp @ Leftovers
Ability: Rough_Skin
Level: 50
Tera Type: Normal
EVs: 44 HP / 212 Atk / 0 Def / 0 SpA / 0 SpD / 252 Spe
Jolly Nature
IVs: 31 HP / 31 Atk / 31 Def / 31 SpA / 31 SpD / 31 Spe
- Earthquake
- Stomping_Tantrum
- Dragon_Claw
- Protect

Armarouge @ Power_Herb
Ability: Flash_Fire
Level: 50
Tera Type: Normal
EVs: 160 HP / 0 Atk / 20 Def / 200 SpA / 28 SpD / 100 Spe
Modest Nature
IVs: 31 HP / 0 Atk / 31 Def / 31 SpA / 31 SpD / 31 Spe
- Trick_Room
- Heat_Wave
- Wide_Guard
- Meteor_Beam
"""
import asyncio

from poke_env.player import RandomPlayer
from poke_env import AccountConfiguration, ShowdownServerConfiguration
from poke_env.player import Player
from poke_env.data import GenData

def teampreview_performance(mon_a, mon_b):
    # We evaluate the performance on mon_a against mon_b as its type advantage
    a_on_b = b_on_a = -np.inf
    for type_ in mon_a.types:
        if type_:
            a_on_b = max(
                a_on_b,
                type_.damage_multiplier(
                    *mon_b.types, type_chart=GenData.from_gen(9).type_chart
                ),
            )
    # We do the same for mon_b over mon_a
    for type_ in mon_b.types:
        if type_:
            b_on_a = max(
                b_on_a,
                type_.damage_multiplier(
                    *mon_a.types, type_chart=GenData.from_gen(9).type_chart
                ),
            )
    # Our performance metric is the different between the two
    return a_on_b - b_on_a

class MaxDamagePlayer(Player):
    def choose_move(self, battle):
        if battle.available_moves:
            print(move)
            best_move = max(battle.available_moves, key=lambda move: move.base_power)
            return self.create_order(best_move)
        else:
            return self.choose_random_move(battle)

class MaxDamagePlayerWithTeampreview(MaxDamagePlayer):
    def teampreview(self, battle):
        mon_performance = {}

        # For each of our pokemons
        for i, mon in enumerate(battle.team.values()):
            # We store their average performance against the opponent team
            mon_performance[i] = np.mean(
                [
                    teampreview_performance(mon, opp)
                    for opp in battle.opponent_team.values()
                ]
            )

        # We sort our mons by performance
        ordered_mons = sorted(mon_performance, key=lambda k: -mon_performance[k])

        # We start with the one we consider best overall
        # We use i + 1 as python indexes start from 0
        #  but showdown's indexes start from 1
        return "/team " + "".join([str(i + 1) for i in ordered_mons])


async def main():
    # We create a random player
    p1 = MaxDamagePlayerWithTeampreview(account_configuration=AccountConfiguration("vgcteambuilder0976", "password"),battle_format="gen9vgc2025regi", team=team_1)
    p2 = MaxDamagePlayerWithTeampreview(account_configuration=AccountConfiguration("vgcteambuilder0853", "password"),battle_format="gen9vgc2025regi", team=team_1)
    
    await p1.battle_against(p2, n_battles=10)

    print(f"Player {p1.username} won {p1.n_won_battles} out of {p1.n_finished_battles} played")
    print(f"Player {p2.username} won {p2.n_won_battles} out of {p2.n_finished_battles} played")

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
    












