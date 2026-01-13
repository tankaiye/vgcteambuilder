from poke_env.player import Player
import numpy as np

team1 = """
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

from poke_env.player import MaxDamagePlayerWithTeampreview
from poke_env import AccountConfiguration, ShowdownServerConfiguration


# We create a random player
p1 = MaxDamagePlayerWithTeampreview(battle_format="gen9vgc2026regf", team=team_1)
p2 = MaxDamagePlayerWithTeampreview(battle_format="gen9vgc2026regf", team=team_1)

await p1.battle_against(p2, n_battles=1)

print(f"Player {p1.username} won {p1.n_won_battles} out of {p1.n_finished_battles} played")
print(f"Player {p2.username} won {p2.n_won_battles} out of {p2.n_finished_battles} played")














