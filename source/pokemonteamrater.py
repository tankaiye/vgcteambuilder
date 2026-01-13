import math, random
#import numpy as np
#import matplotlib
#import matplotlib as mpl
#import matplotlib.pyplot as plt
#Impt. Variables
dsum1weight = 10
dsum2weight = 10

typechart = [1,1,1,1,1,0.5,1,0,0.5,1,1,1,1,1,1,1,1,1,
2,1,0.5,0.5,1,2,0.5,0,2,1,1,1,1,0.5,2,1,2,0.5,
1,2,1,1,1,0.5,2,1,0.5,1,1,2,0.5,1,1,1,1,1,
1,1,1,0.5,0.5,0.5,1,0.5,0,1,1,2,1,1,1,1,1,2,
1,1,0,2,1,2,0.5,1,2,2,1,0.5,2,1,1,1,1,1,
1,0.5,2,1,0.5,1,2,1,0.5,2,1,1,1,1,2,1,1,1,
1,0.5,0.5,0.5,1,1,1,0.5,0.5,0.5,1,2,1,2,1,1,2,0.5,
0,1,1,1,1,1,1,2,1,1,1,1,1,2,1,1,0.5,1,
1,1,1,1,1,2,1,1,0.5,0.5,0.5,1,0.5,1,2,1,1,2,
1,1,1,1,1,0.5,2,1,2,0.5,0.5,2,1,1,2,0.5,1,1,
1,1,1,1,2,2,1,1,1,2,0.5,0.5,1,1,1,0.5,1,1,
1,1,0.5,0.5,2,2,0.5,1,0.5,0.5,2,0.5,1,1,1,0.5,1,1,
1,1,2,1,0,1,1,1,1,1,2,0.5,0.5,1,1,0.5,1,1,
1,2,1,2,1,1,1,1,0.5,1,1,1,1,0.5,1,1,0,1,
1,1,2,1,2,1,1,1,0.5,0.5,0.5,2,1,1,0.5,2,1,1,
1,1,1,1,1,1,1,1,0.5,1,1,1,1,1,1,2,1,0,
1,0.5,1,1,1,1,1,2,1,1,1,1,1,2,1,1,0.5,0.5,
1,2,1,0.5,1,1,1,1,0.5,0.5,1,1,1,1,1,2,2,1]

pokestats = []
movestats = []
naturestats = []
usagestats = []
weightstats = []
movesets = []
fhitmoves = ["Bonemerang", "Double_Hit", "Double_Iron_Bash","Beat_Up", "Double_Kick", "Dragon_Darts", "Dual_Chop", "Dual_Wingbeat", "Gear_Grind", "Surging_Strikes", "Tachyon Cutter", "Triple_Dive", "Twin_Beam", "Twineedle"]
mhitmoves = ["Arm_Thrust","Barrage","Bone_Rush","Bullet_Seed","Comet_Punch","Double_Slap","Fury_Attack","Fury_Swipes","Icicle_Spear","Pin_Missile","Rock_Blast","Scale_Shot","Spike_Cannon","Tail_Slap","Water_Shuriken"]
manyothermoves = []
plateitems = []
soundmoves = []
slicemoves = []
bulletmoves = []
halfspeed = ["Iron_Ball","Macho_Brace","Power_Anklet","Power_Band","Power_Belt","Power_Bracer","Power_Lens","Power_Weight"]
for i in range(18):
    plateitems.append("")

# Format for Pokemon is [name, ivs, evs, natures, item, teratype]
# Format for items is [power, type, defcondition, heal, healcondition, effect]

with open("pokemonstats.txt") as pokemonlist:
    for pokemon in pokemonlist:
        if len(pokemon) > 6:
            pokesep = pokemon.replace("\n","")
            pokestat = pokesep.split(" ")
            pokestats.append(pokestat)

with open("pokemonmoves.txt") as movelist:
    for move in movelist:
        if len(move) > 6:
            movesep = move.replace("\n","")
            movestat = movesep.split(" ")
            movestats.append(movestat)

with open("pokemonnatures.txt") as naturelist:
    counter = 0
    for nature in naturelist:
        if len(nature) > 3:
            naturesep = nature.replace("\n","")
            naturestat = naturesep.split(" ")
            naturestat.append(counter)
            naturestats.append(naturestat)
            counter += 1

with open("pokemonusages.txt") as usagelist:
    for usage in usagelist:
        if len(usage) > 6:
            usagesep = usage.replace("\n","")
            usagesep = usagesep.replace(" ","")
            usagestat = usagesep.split("|")
            usagestat[1] = float(usagestat[1])
            usagestats.append(usagestat)

with open("pokemonweights.txt") as weightlist:
    for weight in weightlist:
        if len(weight) > 6:
            weightsep = weight.replace("\n","")
            weightsep = weightsep.replace(" ","")
            weightstat = weightsep.split("|")
            weightstat[1] = float(weightstat[1])
            weightstats.append(weightstat)

with open("manyothersmoves.txt") as movelist:
    for move in movelist:
        if len(move) > 6:
            movesep = move.replace("\n","")
            movestat = movesep.replace(" ","_")
            manyothermoves.append(movestat)

with open("plateitems.txt") as platelist:
    for plate in platelist:
        if len(plate) > 6:
            platesep = plate.replace("\n","")
            platesep = platesep.replace(" ","_")
            platestat = platesep.split("!")
            plateitems[int(platestat[1])] = platestat[0]

with open("soundmoves.txt") as soundlist:
    for sound in soundlist:
        if len(sound) > 2:
            soundsep = sound.replace("\n","")
            soundsep = soundsep.replace(" ","_")
            soundmoves.append(soundsep)

with open("slicemoves.txt") as slicelist:
    for slicemove in slicelist:
        if len(slicemove) > 2:
            slicesep = slicemove.replace("\n","")
            slicesep = slicesep.replace(" ","_")
            slicemoves.append(slicesep)

with open("bulletmoves.txt") as bulletlist:
    for bulletmove in bulletlist:
        if len(bulletmove) > 2:
            bulletsep = bulletmove.replace("\n","")
            bulletsep = bulletsep.replace(" ","_")
            bulletmoves.append(bulletsep)

with open("pokemonmovesets.txt") as movesetlist:
    counter = -1
    stage = 0
    movesrecorded = 0
    for moveset in movesetlist:
        setname = moveset.replace("\n","")
        namecheck = None
        if counter <= 55:
            namecheck = usagestats[counter + 1][0].lower()
        else:
            namecheck = ""
        if setname.lower() == namecheck:
            counter += 1
            movesets.append([[],[],[],[],[]])
        elif setname.lower() == "abilities":
            stage = 0
        elif setname.lower() == "items":
            stage = 1
        elif setname.lower() == "spreads":
            stage = 2
        elif setname.lower() == "moves":
            movesrecorded = 0
            stage = 3
        elif setname.lower() == "tera_types":
            #print([usagestats[counter][0], movesrecorded])
            stage = 4
        elif setname.lower() == "":
            stage = 5
        else:
            if stage == 0:
                if float(setname.split(" ")[1]) > 2:
                    movesets[counter][0].append(setname.split(" "))
                    movesets[counter][0][len(movesets[counter][0]) - 1][1] = float(movesets[counter][0][len(movesets[counter][0]) - 1][1])
            elif stage == 1:
                if setname.split(" ")[0] != "Other" and float(setname.split(" ")[1]) > 1:
                    movesets[counter][1].append(setname.split(" "))
                    movesets[counter][1][len(movesets[counter][1]) - 1][1] = float(movesets[counter][1][len(movesets[counter][1]) - 1][1])
            elif stage == 2:
                if setname.split(" ")[0].split(":")[0] != "Other" and float(setname.split(" ")[1]) > 1:
                    setname = setname.replace(":","/")
                    setnatures = setname.split(" ")
                    setnatures[0] = setnatures[0].split("/")
                    for i in range(1, len(setnatures[0])):
                        setnatures[0][i] = int(setnatures[0][i])
                    setnatures[1] = float(setnatures[1])
                    movesets[counter][2].append(setnatures)
            elif stage == 3:
                if setname.split(" ")[0] != "Other" and float(setname.split(" ")[1]) > 1:
                    movesets[counter][3].append(setname.split(" "))
                    movesets[counter][3][len(movesets[counter][3]) - 1][1] = float(movesets[counter][3][len(movesets[counter][3]) - 1][1])
                movesrecorded += 1
            elif stage == 4:
                if setname.split(" ")[0] != "Other" and float(setname.split(" ")[1]) > 1:
                    movesets[counter][4].append(setname.split(" "))
                    movesets[counter][4][len(movesets[counter][4]) - 1][1] = float(movesets[counter][4][len(movesets[counter][4]) - 1][1])
            else:
                counter = counter
                #do nothing

def effectiveness(attacktype, deftype1, deftype2):
    stab1effectiveness = typechart[attacktype * 18 + deftype1]
    if deftype2 != False:
        stab2effectiveness = typechart[attacktype * 18 + deftype2]
    else:
        stab2effectiveness = 1
    return stab1effectiveness * stab2effectiveness

def calculatebase(level, power, attack, defense, effectiveness, stab):
    rawdamage = ((0.4 * level) + 2) * power * (attack/defense)
    rawdamage = rawdamage / 50
    rawdamage = rawdamage + 2
    multiplier = 1
    multiplier = multiplier * effectiveness
    if stab:
        multiplier *= 1.5
    damage = rawdamage * multiplier
    return damage

def getbasestats(basestats, ivalues, effortvalues, nature, natureminus, statstagechanges):
    finalstats = [0,0,0,0,0,0]
    health = basestats[0]
    stathealth = math.floor((2 * health + ivalues[0] + math.floor(effortvalues[0]/4))/2 + 60)
    finalstats[0] = stathealth
    for i in range(1,6):
        statnumber = basestats[i]
        basestat = math.floor((2 * statnumber + ivalues[i] + math.floor(effortvalues[i]/4))/2 + 5)
        if i == nature - 1:
            basestat = math.floor(basestat * 1.1)
        if i == natureminus - 1:
            basestat = math.floor(basestat * 0.9)
        basestat = math.floor(basestat * statstagechanges[i])
        finalstats[i] = basestat
    return finalstats

def getstatstages(rawstatstagechanges):
    statstages = []
    for i in range(len(rawstatstagechanges)):
        if rawstatstagechanges[i] >= 0:
            statstages.append(rawstatstagechanges[i]/2 + 1)
        else:
            statstages.append(1/(rawstatstagechanges[i]/(-2) + 1))
    return statstages

def abilitystatstages(ability1, ability2, statstages1, statstages2, item1, item2, targetattack = 0):
    if ability1 == "Intimidate":
        if ability2 == "Guard_Dog" or ability2 == "Defiant" or ability2 == "Contary":
            mstats1 = statstages1
            mstats2 = statstages2
            if mstats2[1]!= 6:
                mstats2[1] = mstats2[1] + 1
            if item1 == "Mirror_Herb":
                if mstats1[1]!= 6:
                    mstats1[1] = mstats1[1] + 2
            return [mstats1, mstats2]
        elif ability2 == "Competitive":
            mstats1 = statstages1
            mstats2 = statstages2
            if mstats2[3] < 4.5:
                mstats2[3] = mstats2[3] + 2
            if item1 == "Mirror_Herb":
                if mstats1[3] < 4.5:
                    mstats1[3] = mstats1[3] + 2
            if mstats2[1]!= -6:
                mstats2[1] = mstats2[1] - 1
            return [mstats1, mstats2]
        elif (ability2 not in ["Clear_Body", "Hyper_Cutter", "White_Smoke", "Oblivious", "Own_Tempo", "Inner_Focus", "Scrappy"]):
            mstats1 = statstages1
            mstats2 = statstages2
            if mstats2[1]!= -6:
                mstats2[1] = mstats2[1] - 1
            if ability2 == "Rattled":
                if mstats2[5]!= 6:
                    mstats2[5] = mstats2[5] + 1
                    if item1 == "Mirror_Herb":
                        if mstats1[5]!= 6:
                            mstats1[5] = mstats1[5] + 1
            return [mstats1, mstats2]
        else:
            return [statstages1, statstages2]
    elif ability1 == "Speed_Boost":
        mstats1 = statstages1
        mstats2 = statstages2
        if mstats1[5]!= 6:
            mstats1[5] = mstats1[5] + 1
        if item2 == "Mirror_Herb":
            if mstats2[5]!= 6:
                mstats2[5] = mstats2[5] + 1
        return [mstats1, mstats2]
    elif ability1 == "Stamina":
        mstats1 = statstages1
        mstats2 = statstages2
        if mstats1[2]!= 6:
            mstats1[2] = mstats1[2] + 1
        if item2 == "Mirror_Herb":
            if mstats2[2]!= 6:
                mstats2[2] = mstats2[2] + 1
        return [mstats1, mstats2]
    elif ability1 == "Download":
        mstats1 = statstages1
        mstats2 = statstages2
        if mstats1[1]!= 6:
            mstats1[1] = mstats1[1] + 0.5
        if mstats1[3]!= 6:
            mstats1[3] = mstats1[3] + 0.5
        if item2 == "Mirror_Herb":
            if mstats2[1]!= 6:
                mstats2[1] = mstats2[1] + 0.5
            if mstats2[3]!= 6:
                mstats2[3] = mstats2[3] + 0.5
        return [mstats1, mstats2]
    elif ability1 == "Weak_Armor" and targetattack == 1:
        mstats1 = statstages1
        mstats2 = statstages2
        if mstats1[2]!= -6:
            mstats1[2] = mstats1[2] - 1
        if mstats1[5] < 4.5:
            mstats1[5] = mstats1[5] + 2
        if item2 == "Mirror_Herb":
            if mstats2[5] < 4.5:
                mstats2[5] = mstats2[5] + 2
        return [mstats1, mstats2]
    else:
        return [statstages1, statstages2]

def prstatrange(rawstat):
    statrange = []
    for i in range(85,101,1):
        statrange.append(rawstat * i * 0.01)
    return statrange

def getpokemon(name):
    for pokemon in pokestats:
        if pokemon[0].lower() == name.lower():
            if len(pokemon) == 8:
                return [int(pokemon[1]),int(pokemon[2]),int(pokemon[3]),int(pokemon[4]),int(pokemon[5]),int(pokemon[6]),getnumfromtype(pokemon[7])]
            else:
                return [int(pokemon[1]),int(pokemon[2]),int(pokemon[3]),int(pokemon[4]),int(pokemon[5]),int(pokemon[6]),getnumfromtype(pokemon[7]),getnumfromtype(pokemon[8])]

def findpokemon(name):
    for i in range(0,57):
        if usagestats[i][0].lower() == name.lower():
            return i
        
def getnumfromtype(pktype):
    pkt = pktype.lower()
    if "normal" in pkt:
        return 0
    elif "fight" in pkt:
        return 1
    elif "flying" in pkt:
        return 2
    elif "poison" in pkt:
        return 3
    elif "ground" in pkt:
        return 4
    elif "rock" in pkt:
        return 5
    elif "bug" in pkt:
        return 6
    elif "ghost" in pkt:
        return 7
    elif "steel" in pkt:
        return 8
    elif "fire" in pkt:
        return 9
    elif "water" in pkt:
        return 10
    elif "grass" in pkt:
        return 11
    elif "electric" in pkt:
        return 12
    elif "psychic" in pkt:
        return 13
    elif "ice" in pkt:
        return 14
    elif "dragon" in pkt:
        return 15
    elif "dark" in pkt:
        return 16
    else:
        return 17

def getmove(name):
    for move in movestats:
        if move[1].lower() == name.lower():
            if move[3].lower() == "physical":
                attackkind = 1
            else:
                attackkind = 2
            return [getnumfromtype(move[2]), attackkind, int(move[4]),int(move[5]),int(move[6])]
    if move == "Super_Fang":
        return [0, 1, 0, 0, 100]
    else:
        return [0, 0, 0, 0, 100]


def calculaterawdamage(pokemon1, ivs1, evs1, natures1, pokemon2, ivs2, evs2, natures2, move, statstagechanges1, statstagechanges2, itemset):
    pokemonstats1 = getpokemon(pokemon1)
    stats1 = getbasestats(pokemonstats1[0:6], ivs1, evs1, natures1[0], natures1[1], getstatstages(statstagechanges1))
    pokemonstats2 = getpokemon(pokemon2)
    stats2 = getbasestats(pokemonstats2[0:6], ivs2, evs2, natures2[0], natures2[1], getstatstages(statstagechanges2))
    if len(pokemonstats2) == 7:  
        typematchup = effectiveness(getmove(move)[0], pokemonstats2[6], False)
    else:
        typematchup = effectiveness(getmove(move)[0], pokemonstats2[6], pokemonstats2[7])
    movestab = False
    if getmove(move)[0] == pokemonstats1[6]:
        movestab = True
    if len(pokemonstats1) == 8:
        if getmove(move)[0] == pokemonstats1[7]:
            movestab = True
    if getmove(move)[1] == 1:
        damage = calculatebase(50, getmove(move)[3], stats1[1], stats2[2], typematchup, movestab)
    else:
        damage = calculatebase(50, getmove(move)[3], stats1[3], stats2[4], typematchup, movestab)
    statrange = prstatrange(damage)
    return statrange[0]
      

def calculatedamage(pokemon1, ivs1, evs1, natures1, pokemon2, ivs2, evs2, natures2, move, statstagechanges1, statstagechanges2, healthpenalties, fieldconditions, itemset):
    #fieldconditons[0] is weather
    #1 is sun
    #2 is rain
    #3 is sand
    #4 is hail
    #fieldconditons[1] is terrain
    #1 is grassy
    #2 is psychic
    #3 is electric
    #4 is misty
    pokemonstats1 = getpokemon(pokemon1)
    pokemonstats2 = getpokemon(pokemon2)
    stats1 = getbasestats(pokemonstats1[0:6], ivs1, evs1, natures1[0], natures1[1], getstatstages(statstagechanges1))
    if move == "Sacred_Sword":
        stats2 = getbasestats(pokemonstats2[0:6], ivs2, evs2, natures2[0], natures2[1], [1,1,1,1,1,1])
    else:
        stats2 = getbasestats(pokemonstats2[0:6], ivs2, evs2, natures2[0], natures2[1], getstatstages(statstagechanges2))
    #Eviolite Check
    if itemset[1] == "Eviolite":
        stats2[2] *= 1.5
        stats2[4] *= 1.5
    if itemset[1] == "Assault_Vest":
        stats2[4] *= 1.5
    if itemset[0] == "Flame_Orb":
        stats1[1] *= 1.5
        if move == "Facade":
            move = "Facade_Guts"
    if move == "Weather_Ball":
        if fieldconditions[0] == 1:
            move = "Weather_Ball_Sun"
        elif fieldconditions[0] == 2:
            move = "Weather_Ball_Rain"
        elif fieldconditions[0] == 3:
            move = "Weather_Ball_Sand"
        elif fieldconditions[0] == 4:
            move = "Weather_Ball_Snow"
    if move == "Low_Kick":
        pokemonweight = weightstats[findpokemon(pokemon2)][1]
        if pokemonweight <= 9.9:
            move = "Low_Kick_20"
        elif pokemonweight <= 24.9:
            move = "Low_Kick_40"
        elif pokemonweight <= 49.9:
            move = "Low_Kick_60"
        elif pokemonweight <= 99.9:
            move = "Low_Kick_80"
        elif pokemonweight <= 199.9:
            move = "Low_Kick_100"
        else:
            move = "Low_Kick_120"
    #Liquid Voice Check
    if move == "Hyper_Voice" and itemset[2] == "Liquid_Voice":
        move = "Hyper_Voice_Liquid"
    affectedbysandstorm = True
    isrocktype = False
    isflyingtype = False
    weaktosalt = False
    canbepoisoned = True
    #typematchups
    if len(pokemonstats2) == 7:  
        typematchup = effectiveness(getmove(move)[0], pokemonstats2[6], False)
        if pokemonstats2[6] in [4, 5, 8]:
            affectedbysandstorm = False
        if pokemonstats2[6] in [8, 10]:
            weaktosalt = True
        if pokemonstats2[6] in [3, 8]:
            canbepoisoned = False
        if pokemonstats2[6] == 5:
            isrocktype = True
        if pokemonstats2[6] == 2:
            isflyingtype = True
    else:
        typematchup = effectiveness(getmove(move)[0], pokemonstats2[6], pokemonstats2[7])
        if pokemonstats2[6] in [4, 5, 8]:
            affectedbysandstorm = False
        if pokemonstats2[7] in [4, 5, 8]:
            affectedbysandstorm = False
        if pokemonstats2[6] in [8, 10]:
            weaktosalt = True
        if pokemonstats2[7] in [8, 10]:
            weaktosalt = True
        if pokemonstats2[6] in [3, 8]:
            canbepoisoned = False
        if pokemonstats2[7] in [3, 8]:
            canbepoisoned = False
        if pokemonstats2[6] == 5 or pokemonstats2[7] == 5:
            isrocktype = True
        if pokemonstats2[6] == 2 or pokemonstats2[7] == 2:
            isflyingtype = True
    #Normal/Fighting Bypass Check
    if itemset[2] == "Scrappy" or itemset[2] == "Mind's_Eye":
        if (getmove(move)[0] == 0 or getmove(move)[0] == 1) and typematchup == 0:
            if len(pokemonstats2) == 7:
                typematchup = 1
            else:
                if pokemonstats2[6] == 7:
                    typematchup = effectiveness(getmove(move)[0], 4, pokemonstats2[7])
                else:
                    typematchup = effectiveness(getmove(move)[0], pokemonstats2[6], 4)
    #Technician Bonus Check
    if itemset[2] == "Technician":
        if getmove(move)[3] <= 60:
            typematchup *= 1.5
    #Heatproof + Thermal Exchange Check
    if getmove(move)[0] == 9 and itemset[3] in ["Heatproof", "Thermal_Exchange"]:
        typematchup *= 0.5
    #Flash Fire Check
    if getmove(move)[0] == 9 and itemset[3] == "Flash_Fire":
        typematchup = 0
        return [0, 100]
    #Sap Sipper Check
    if getmove(move)[0] == 11 and itemset[3] == "Sap_Sipper":
        typematchup = 0
        return [0, 100]
    #Salt Check
    if getmove(move)[0] == 7 and itemset[3] == "Purifying_Salt":
        typematchup *= 0.5
    #Soundproof, Bulletproof Check
    if move in bulletmoves and itemset[3] == "Bulletproof":
        typematchup = 0
        return [0, 100]
    if move in soundmoves and itemset[3] == "Soundproof":
        typematchup = 0
        return [0, 100]
    #Sharpness Check
    if move in slicemoves and itemset[2] == "Sharpness":
        typematchup *= 1.5
    #Levitate Check
    if getmove(move)[0] == 4 and itemset[3] == "Levitate":
        typematchup = 0
        return [0, 100]
    #Solar Power Check
    if fieldconditions[0] == 1 and itemset[2] == "Solar_Power":
        stats1[3] *= 1.5
    #Sand Check
    if isrocktype and fieldconditions[0] == 3:
        stats2[4] *= 1.5
    #Sand Force Check
    if itemset[2] == "Sand_Force" and fieldconditions[0] == 3 and getmove(move)[0] in [4,5,8]:
        typematchup *= 1.3 
    #Damage Booster Checks:
    if typematchup >= 2 and itemset[0] == "Expert_Belt":
        typematchup *= 1.2
    if itemset[0] == "Wise_Glasses":
        stats1[3] *= 1.1
    if itemset[0] == "Muscle_Band":
        stats1[1] *= 1.1
    if itemset[0] == "Life_Orb":
        typematchup *= 1.3
    if itemset[0] == plateitems[getmove(move)[0]]:
        typematchup *= 1.2
    #Rain and Sun Checks
    if getmove(move)[0] == 9 and fieldconditions[0] == 1:
        typematchup *= 1.5
    if getmove(move)[0] == 10 and fieldconditions[0] == 1:
        typematchup *= 0.5
    if getmove(move)[0] == 9 and fieldconditions[0] == 2:
        typematchup *= 0.5
    if getmove(move)[0] == 10 and fieldconditions[0] == 2:
        typematchup *= 1.5
    #Terrain Checks
    if getmove(move)[0] == 15 and fieldconditions[1] == 4 and not isflyingtype:
        typematchup *= 0.5
    if getmove(move)[0] == 11 and fieldconditions[1] == 1:
        typematchup *= 1.3
        if move == "Earthquake":
            typematchup *= 0.5
    if getmove(move)[0] == 13 and fieldconditions[1] == 2:
        typematchup *= 1.3
        if move == "Expanding_Force":
            typematchup *= 2
    if getmove(move)[0] == 12 and fieldconditions[1] == 3:
        typematchup *= 1.3
    #Seed Checks
    seedactive = False
    if fieldconditions[1] == 1 and itemset[0] == "Grassy_Seed":
        stats1[2] *= 1.5
        seedactive = True
    if fieldconditions[1] == 2 and itemset[0] == "Psychic_Seed":
        stats1[4] *= 1.5
        seedactive = True
    if fieldconditions[1] == 3 and itemset[0] == "Electric_Seed":
        stats1[2] *= 1.5
        seedactive = True
    if fieldconditions[1] == 4 and itemset[0] == "Misty_Seed":
        stats1[4] *= 1.5
        seedactive = True
    if fieldconditions[1] == 1 and itemset[1] == "Grassy_Seed":
        stats2[2] *= 1.5
    if fieldconditions[1] == 2 and itemset[1] == "Psychic_Seed":
        stats2[4] *= 1.5
    if fieldconditions[1] == 3 and itemset[1] == "Electric_Seed":
        stats2[2] *= 1.5
    if fieldconditions[1] == 4 and itemset[1] == "Misty_Seed":
        stats2[4] *= 1.5
    movestab = False
    if getmove(move)[0] == pokemonstats1[6]:
        movestab = True
    if len(pokemonstats1) == 8:
        if getmove(move)[0] == pokemonstats1[7]:
            movestab = True
    if movestab == True and itemset[2] == "Adaptability":
        typematchup *= (2/1.5)
    if move == "Acrobatics" and itemset[0] == None or seedactive == True:
        typematchup *= 2
    if getmove(move)[1] == 1:
        if move == "Body_Press":
            damage = calculatebase(50, getmove(move)[3], stats1[2], stats2[2], typematchup, movestab)
        elif move == "Foul_Play":
            damage = calculatebase(50, getmove(move)[3], stats2[1], stats2[2], typematchup, movestab)
        else:
            damage = calculatebase(50, getmove(move)[3], stats1[1], stats2[2], typematchup, movestab)
    else:
        damage = calculatebase(50, getmove(move)[3], stats1[3], stats2[4], typematchup, movestab)
    if move == "Poison_Gas":
        if canbepoisoned:
            damage = math.floor(stats2[0]/4)
        else:
            return [0, 100]
    if move == "Mortal_Spin" and canbepoisoned and itemset[1] != "Covert_Cloak":
        damage += math.floor(stats2[0]/4)
    #Sand, Grassy, Lefties, and LO Check
    chipdamage = 0
    if fieldconditions[0] == 3 and affectedbysandstorm and itemset[1] != "Safety_Goggles" and itemset[3] not in ["Sand Force", "Sand Rush", "Sand Veil", "Magic Guard", "Overcoat"]:
        chipdamage += math.floor(stats2[0]/16)
    if fieldconditions[1] == 1 and not isflyingtype:
        chipdamage -= math.floor(stats2[0]/16)
    if itemset[1] == "Leftovers":
        chipdamage -= math.floor(stats2[0]/16)
    if itemset[1] == "Life_Orb":
        chipdamage += math.floor(stats2[0]/10)
    if itemset[1] == "Flame_Orb":
        chipdamage += math.floor(stats2[0]/16)
    if itemset[0] == "Rocky_Helmet" and stats2[1] > stats2[3]:
        chipdamage += math.floor(stats2[0]/6)
    if itemset[2] == "Rough_Skin" and stats2[1] > stats2[3]:
        chipdamage += math.floor(stats2[0]/8)
    if fieldconditions[0] == 1 and itemset[3] == "Solar_Power":
        chipdamage += math.floor(stats2[0]/8)
    #Salt Cure
    if move == "Salt_Cure" and itemset[1] != "Covert_Cloak":
        if weaktosalt:
            chipdamage += math.floor(stats2[0]/4)
        else:
            chipdamage += math.floor(stats2[0]/8)
    statrange = prstatrange(damage + chipdamage)
    #print([pokemon1, move, damage])
    #for type-2 multi-hit moves]
    if itemset[0] == "Wide_Lens":
        accuracy = 100/(getmove(move)[4] * 1.1)
    else:
        accuracy = 100/getmove(move)[4]
    #Hail Check
    if fieldconditions[0] == 4 and move == "Blizzard":
        accuracy = 1
    if fieldconditions[0] == 2 and move == "Hurricane":
        accuracy = 1
    if fieldconditions[0] == 2 and move == "Thunder":
        accuracy = 1
    localhealth = stats2[0] - healthpenalties
    if itemset[3] == "Hospitality":
        localhealth = localhealth + math.floor(stats2[0] * 0.21875)
    if itemset[3] == "Friend_Guard":
        localhealth = localhealth + math.floor(stats2[0] * 0.33333)
    if accuracy < 1:
        accuracy = 1
    if statrange[15]/stats2[0] > 0.01 or statrange[0]/stats2[0] > 0.01:
        if move in mhitmoves:
            if itemset[1] == "Sitrus_Berry":
                localhealth = localhealth + math.floor(stats2[0]/4)
            if itemset[1] in ["Aguav_Berry", "Figy_Berry", "Iapapa_Berry", "Mago_Berry", "Wiki_Berry"]:
                localhealth = localhealth + math.floor(stats2[0]/3)
            maxhits = math.ceil(localhealth/(statrange[15] * 3.1))
            minhits = math.ceil((localhealth/(statrange[0] * 2.5)) * (accuracy))
            if itemset[0] == "Loaded_Dice":
                maxhits = math.ceil(localhealth/(statrange[15] * 4.5))
                minhits = math.ceil((localhealth/(statrange[0] * 4)) * (accuracy))
            if itemset[1] == "Maranga_Berry" and getmove(move)[1] == 2:
                maxhits = math.ceil(localhealth/(statrange[15] * 3.1/1.5))
                minhits = math.ceil((localhealth/(statrange[0] * 2.5/1.5)) * (accuracy))
        elif move in ["Triple_Axel", "Triple_Kick", "Population_Bomb"]:
            if itemset[1] == "Sitrus_Berry":
                localhealth = localhealth + math.floor(stats2[0]/4)
            if itemset[1] in ["Aguav_Berry", "Figy_Berry", "Iapapa_Berry", "Mago_Berry", "Wiki_Berry"]:
                localhealth = localhealth + math.floor(stats2[0]/3)
            maxhits = math.ceil(localhealth/(statrange[15] * 6))
            minhits = math.ceil((localhealth/(statrange[0] * 5.3)) * (accuracy))
            if itemset[0] == "Wide_Lens":
                maxhits = math.ceil(localhealth/(statrange[15] * 6))
                minhits = math.ceil((localhealth/(statrange[0] * 6)) * (accuracy))
                if move == "Population_Bomb":
                    maxhits = math.ceil(localhealth/(statrange[15] * 10))
                    minhits = math.ceil((localhealth/(statrange[0] * 9)) * (accuracy)) 
        elif move in manyothermoves:
            maxhits = math.ceil(localhealth/(statrange[15] * 0.75))
            minhits = math.ceil((localhealth/(statrange[0] * 0.75)) * (accuracy))
            #Multiscale Check
            if itemset[3] == "Multiscale" and healthpenalties <= 0:
                localhealth = localhealth + (statrange[7] * 0.75)/2
                maxhits = math.ceil(localhealth/(statrange[15] * 0.75))
                minhits = math.ceil((localhealth/(statrange[0] * 0.75)) * (accuracy))
            if maxhits >= 2 and itemset[1] == "Sitrus_Berry":
                localhealth = localhealth + math.floor(stats2[0]/4)
                maxhits = math.ceil(localhealth/(statrange[15] * 0.75))
                minhits = math.ceil((localhealth/(statrange[0] * 0.75)) * (accuracy))
            if maxhits >= 3 and itemset[1] in ["Aguav_Berry", "Figy_Berry", "Iapapa_Berry", "Mago_Berry", "Wiki_Berry"]:
                localhealth = localhealth + math.floor(stats2[0]/3)
                maxhits = math.ceil(localhealth/(statrange[15] * 0.75))
                minhits = math.ceil((localhealth/(statrange[0] * 0.75)) * (accuracy))
            if maxhits >= 2 and itemset[1] == "Maranga_Berry" and getmove(move)[1] == 2:
                localhealth = localhealth - statrange[7]/4
                statrange[0] = statrange[0]/1.5
                statrange[7] = statrange[7]/1.5
                statrange[15] = statrange[15]/1.5
                maxhits = math.ceil(localhealth/(statrange[15] * 0.75))
                minhits = math.ceil((localhealth/(statrange[0] * 0.75)) * (accuracy))
            if maxhits >= 2 and move == "Make_It_Rain":
                localhealth = localhealth - (statrange[7] * 0.75)
                maxhits = math.ceil(localhealth/(statrange[15] * 0.5)) + 1
                minhits = math.ceil((localhealth/(statrange[0] * 0.5)) * (accuracy)) + 1
                if maxhits >= 3:
                    localhealth = localhealth - (statrange[7]* 0.75)/2
                    maxhits = math.ceil(localhealth/(statrange[15] * 0.375)) + 2
                    minhits = math.ceil((localhealth/(statrange[0] * 0.375)) * (accuracy)) + 2
            if maxhits >= 2 and itemset[0] == "Throat_Spray":
                if move in soundmoves:
                    if itemset[3] != "Multiscale" or healthpenalties > 0:
                        localhealth = localhealth - (statrange[7] * 0.75)
                    maxhits = math.ceil(localhealth/(statrange[15] * 1.5 * 0.75)) + 1
                    minhits = math.ceil((localhealth/(statrange[0] * 1.5 * 0.75)) * (accuracy)) + 1
                else:
                    if minhits >= 3:
                        maxhits = math.ceil(localhealth/(statrange[15] * 1.5 * 0.75)) + 1
                        minhits = math.ceil((localhealth/(statrange[0] * 1.5 * 0.75)) * (accuracy)) + 1
            if maxhits < 2 and (itemset[1] == "Focus_Sash" or itemset[3] == "Sturdy") and chipdamage <= 0 and healthpenalties <= 0:
                maxhits = 2
                minhits = 2
            maxhits *= 0.5
            minhits *= 0.5
        else:
            if move == "Knock_Off" and itemset[1] == "":
                if itemset[3] == "Multiscale" and healthpenalties <= 0:
                    localhealth = localhealth - statrange[0]/4
                else:
                    localhealth = localhealth - statrange[0]/2
            maxhits = math.ceil(localhealth/statrange[15]) 
            minhits = math.ceil((localhealth/statrange[0]) * (accuracy))
            #Multiscale Check
            if itemset[3] == "Multiscale" and healthpenalties <= 0:
                localhealth = localhealth + statrange[7]/2
                maxhits = math.ceil(localhealth/(statrange[15]))
                minhits = math.ceil((localhealth/(statrange[0])) * (accuracy))
            if maxhits >= 2 and itemset[1] == "Sitrus_Berry":
                localhealth = localhealth + math.floor(stats2[0]/4)
                maxhits = math.ceil(localhealth/(statrange[15]))
                minhits = math.ceil((localhealth/(statrange[0])) * (accuracy))
            if maxhits >= 3 and itemset[1] in ["Aguav_Berry", "Figy_Berry", "Iapapa_Berry", "Mago_Berry", "Wiki_Berry"]:
                localhealth = localhealth + math.floor(stats2[0]/3)
                maxhits = math.ceil(localhealth/(statrange[15]))
                minhits = math.ceil((localhealth/(statrange[0])) * (accuracy))
            if maxhits >= 2 and itemset[1] == "Maranga_Berry" and getmove(move)[1] == 2:
                localhealth = localhealth - statrange[7]/3
                statrange[0] = statrange[0]/1.5
                statrange[7] = statrange[7]/1.5
                statrange[15] = statrange[15]/1.5
                maxhits = math.ceil(localhealth/(statrange[15]))
                minhits = math.ceil((localhealth/(statrange[0])) * (accuracy))
            #Draco Check
            if maxhits >= 2 and move in ["Draco_Meteor", "Overheat"]:
                localhealth = localhealth - statrange[7]
                maxhits = math.ceil(localhealth/(statrange[15]/2)) + 1
                minhits = math.ceil((localhealth/(statrange[0]/2)) * (accuracy)) + 1
                if maxhits >= 3:
                    localhealth = localhealth - statrange[7]/2
                    maxhits = math.ceil(localhealth/(statrange[15]/3)) + 2
                    minhits = math.ceil((localhealth/(statrange[0]/3)) * (accuracy)) + 2
            soundcheck = 1
            if maxhits >= 2 and itemset[0] == "Throat_Spray":
                if move in soundmoves:
                    localhealth = localhealth - statrange[7]
                    maxhits = math.ceil(localhealth/(statrange[15] * 1.5)) + 1
                    minhits = math.ceil((localhealth/(statrange[0] * 1.5)) * (accuracy)) + 1
                else:
                    if minhits >= 3:
                        maxhits = math.ceil(localhealth/(statrange[15] * 1.5)) + 1
                        minhits = math.ceil((localhealth/(statrange[0] * 1.5)) * (accuracy)) + 1
            if move in ["Electro_Shot", "Meteor_Beam"]:
                if itemset[3] == "Multiscale" and healthpenalties <= 0:
                    localhealth = localhealth + statrange[7]/4
                if itemset[0] == "Power_Herb":
                    maxhits = math.ceil(localhealth/(statrange[15] * 1.5))
                    minhits = math.ceil((localhealth/(statrange[0] * 1.5)) * (accuracy))
                    if maxhits >= 2:
                        localhealth = localhealth - statrange[7] * 1.5
                        maxhits = math.ceil(localhealth/(statrange[15] * 1.5)) * 2 + 1
                        minhits = math.ceil((localhealth/(statrange[0] * 1.5)) * (accuracy)) * 2 + 1
                else:
                    maxhits = math.ceil(localhealth/(statrange[15] * 1.5)) * 2
                    minhits = math.ceil((localhealth/(statrange[0] * 1.5)) * (accuracy)) * 2
            else:
                if itemset[0] == "Power_Herb":
                    if minhits >= 3:
                        maxhits = math.ceil(localhealth/(statrange[15] * 1.5)) + 1
                        minhits = math.ceil((localhealth/(statrange[0] * 1.5)) * (accuracy)) + 1
            if move == "Hyper_Beam":
                if maxhits >= 2:
                    maxhits = math.ceil(localhealth/(statrange[15] * 1.5)) * 2 + 1
                    minhits = math.ceil((localhealth/(statrange[0] * 1.5)) * (accuracy)) * 2 + 1
            if (move == "Solar_Blade" and fieldconditions[0] != 1) or (move == "Solar_Beam" and fieldconditions[0] != 1):
                maxhits = maxhits * 2
                minhits = minhits * 2
            if maxhits < 2 and (itemset[1] == "Focus_Sash" or itemset[3] == "Sturdy") and chipdamage <= 0 and healthpenalties <= 0:
                maxhits = 2
                minhits = 2
        if itemset[1] == "Air_Balloon" and getmove(move)[0] == 4:
            maxhits += 1
            minhits += 1
        if minhits <= 0:
            minhits = 1
        if maxhits <= 0:
            maxhits = 1
    else:
        return [0, 100]
    if maxhits == minhits:
        return [damage + chipdamage, maxhits, getmove(move)[0]]
    else:
        return [damage + chipdamage, minhits - 0.1, getmove(move)[0]]
    #returns integer if guaranteed, returns integer + 0.9 if not

def speedcheck(pokemon1, ivs1, evs1, natures1, pokemon2, ivs2, evs2, natures2, statstagechanges, multiplier):
    pokemonstats1 = getpokemon(pokemon1)
    stats1 = getbasestats(pokemonstats1[0:6], ivs1, evs1, natures1[0], natures1[1], getstatstages(statstagechanges[0]))
    pokemonstats2 = getpokemon(pokemon2)
    stats2 = getbasestats(pokemonstats2[0:6], ivs2, evs2, natures2[0], natures2[1], getstatstages(statstagechanges[1]))
    speed1 = int(stats1[5]) * multiplier
    speed2 = int(stats2[5])
    #print(speed1, speed2)
    if speed1 > speed2:
        if speed1 > speed2 * 2:
            return 3
        elif speed1 > speed2 * 1.5:
            return 2
        else:
            return 1
    elif speed1 < speed2:
        if speed2 > speed1 * 2:
            return -3
        elif speed2 > speed1 * 1.5:
            return -2
        else:
            return -1
    else:
        return 0
    #3 if Pokemon of interest outspeeds target even under Tailwind from target
    #2 if Pokemon of interest outspeeds target at -1 speed
    #1 if Pokemon of interest outspeeds target
    #0 if Pokemon speed ties

def getnaturefromid(natureid):
    return [naturestats[natureid][1],naturestats[natureid][2]]

def getnaturefromname(naturename):
    for naturestat in naturestats:
        if naturestat[0].lower() == naturename.lower():
            return naturestat[3]
    return False

def getnamefromnature(natureplus, natureminus):
    return naturestats[(natureplus - 1) * 5 + natureminus - 1][0]

def checkfakeout(pokemon1, ivs1, evs1, natures1, pokemon2, ivs2, evs2, natures2, moves1, moves2, statstagechanges, itemset):
    fakeout1 = 0
    fakeout2 = 0
    for i in range(len(moves1)):
        if moves1[i][0] == "Fake_Out":
            fakeout1 = moves1[i][1]/100
    for i in range(len(moves2)):
        if moves2[i][0] == "Fake_Out":
            fakeout2 = moves2[i][1]/100
    if fakeout1 == 0 and fakeout2 == 0:
        return [0,0]
    elif fakeout1 >= 0 and fakeout2 == 0:
        return [calculaterawdamage(pokemon1, ivs1, evs1, natures1, pokemon2, ivs2, evs2, natures2, "Fake_Out", statstagechanges[0], statstagechanges[1], itemset), 1]
    elif fakeout1 == 0 and fakeout2 >= 0:
        itemset = [itemset[1], itemset[0]]
        return [calculaterawdamage(pokemon2, ivs2, evs2, natures2, pokemon1, ivs1, evs1, natures1, "Fake_Out", statstagechanges[1], statstagechanges[0], itemset), 2]
    else:
        speeddiff = speedcheck(pokemon1, ivs1, evs1, natures1, pokemon2, ivs2, evs2, natures2, [[0,0,0,0,0,0],[0,0,0,0,0,0]], 1)
        if speeddiff > 0:
            return [calculaterawdamage(pokemon1, ivs1, evs1, natures1, pokemon2, ivs2, evs2, natures2, "Fake_Out", statstagechanges[0], statstagechanges[1], itemset), 1]
        elif speeddiff < 0:
            itemset = [itemset[1], itemset[0]]
            return [calculaterawdamage(pokemon2, ivs2, evs2, natures2, pokemon1, ivs1, evs1, natures1, "Fake_Out", statstagechanges[1], statstagechanges[0], itemset), 2]
        else:
            return [0,0]

def getbestmove(pokemon1, ivs1, evs1, natures1, pokemon2, ivs2, evs2, natures2, moves1, moves2, statstagechanges, healthpenalties, fieldconditions = [0,0], itemset = None, recoil = False):
    #damagecheck
    weightedrolls = [] 
    for i in range(0, len(moves1)):    
        rolls = calculatedamage(pokemon1, ivs1, evs1, natures1, pokemon2, ivs2, evs2, natures2, moves1[i][0], statstagechanges[0], statstagechanges[1], healthpenalties, fieldconditions, itemset)[1]
        if rolls <= 10:
            if monhasmove(moves1, "Super_Fang"):
                rollsnew = calculatedamage(pokemon1, ivs1, evs1, natures1, pokemon2, ivs2, evs2, natures2, moves1[i][0], statstagechanges[0], statstagechanges[1], healthpenalties + monmovepercent(moves2, "Super_Fang") * 0.45, fieldconditions, itemset)[1] + 1
                if rollsnew < rolls:
                    rolls = rollsnew
            weightedrolls.append([rolls, moves1[i][1], moves1[i][0]])
        else:
            if getmove(moves1[i][0])[3] > 0:
                weightedrolls.append([10, moves1[i][1], moves1[i][0]])
    #print(statstagechanges, healthpenalties, itemset)
    dsum = 0
    selfdamage = 0
    defenselower = 0
    spdlower = 0
    totalweight = 0
    #print(weightedrolls)
    while totalweight < 100 and len(weightedrolls) > 0:  
        minhits = 100
        minweight = 0
        for i in range(0, len(weightedrolls)):
            if weightedrolls[i][0] <= minhits:
                minhits = weightedrolls[i][0]
                minweight = weightedrolls[i][1]
                movename = weightedrolls[i][2]
                if movename in manyothermoves or movename == "Earthquake":
                    minweight = minweight * ((100 - monmovepercent(moves2, "Wide_Guard"))/100)
                    weightedrolls[i][1] = minweight
                if movename in soundmoves:
                    minweight = minweight * ((100 - monmovepercent(moves2, "Throat_Chop"))/100)
                    weightedrolls[i][1] = minweight
        #print([minhits, minweight, movename])
        weightedrolls.remove([minhits, minweight, movename])
        if minweight + totalweight <= 100:
            totalweight += minweight
            dsum += minhits * minweight / 100
            if movename in ["Flare_Blitz","Wood_Hammer","Brave_Bird","Wave_Crash"]:
                selfdamage += minweight * 0.33
            if movename == "Head_Smash":
                selfdamage += minweight * 0.5
            if movename in ["Drain_Punch", "Matcha_Gotcha"]:
                selfdamage -= minweight * 0.5
            if movename in ["Armor_Cannon", "Headlong_Rush", "Glave_Rush", "Close_Combat", "Scale_Shot", "Clanging_Scales"]:
                defenselower -= minweight / 100
            if movename in ["Armor_Cannon", "Headlong_Rush", "Glave_Rush", "Close_Combat"]:
                spdlower -= minweight / 100
        else:
            modweight = 100 - totalweight
            totalweight = 100
            dsum += minhits * modweight / 100
            if movename in ["Flare_Blitz","Wood_Hammer","Brave_Bird","Wave_Crash"]:
                selfdamage += modweight * 0.33
            if movename == "Head_Smash":
                selfdamage += modweight * 0.5
            if movename in ["Drain_Punch", "Matcha_Gotcha"]:
                selfdamage -= modweight * 0.5
    if totalweight < 100:
        dsum += 10 * (100 - totalweight) / 100
    if dsum == 0:
        dsum = 100
    modweight = 0
    extraturns = 0
    extrarecoil = 0
    selfstagechanges = [0,0,0,0,0,0]
    if itemset[0] != "Assault_Vest" and itemset[0] != "Choice_Specs" and itemset[0] != "Choice_Scarf" and itemset[0] != "Choice_Band":
        if monmovepercent(moves1, "Nasty_Plot") > 0:
            modweight = monmovepercent(moves1, "Nasty_Plot")
            selfstagechanges[3] = selfstagechanges[3] + (0.02 * modweight)
            extraturns += modweight/100
        if monmovepercent(moves1, "Swords_Dance") > 0:
            modweight = monmovepercent(moves1, "Swords_Dance")
            selfstagechanges[1] = selfstagechanges[1] + (0.02 * modweight)
            extraturns += modweight/100
        if monmovepercent(moves1, "Bulk_Up") > 0:
            modweight = monmovepercent(moves1, "Bulk_Up")
            selfstagechanges[1] = selfstagechanges[1] + (0.01 * modweight)
            selfstagechanges[2] = selfstagechanges[2] + (0.01 * modweight)
            extraturns += modweight/100
        if monmovepercent(moves1, "Coaching") > 0:
            modweight = monmovepercent(moves1, "Coaching")
            if monmovepercent(moves1, "Coaching") + monmovepercent(moves1, "Bulk_Up") + monmovepercent(moves1, "Swords_Dance") > 100:
                modweight = 100 - monmovepercent(moves1, "Bulk_Up") - monmovepercent(moves1, "Swords_Dance")
            selfstagechanges[1] = selfstagechanges[1] + (0.01 * modweight)
            selfstagechanges[2] = selfstagechanges[2] + (0.01 * modweight)
            extraturns += modweight/100
        if monmovepercent(moves1, "Calm_Mind") > 0:
            modweight = monmovepercent(moves1, "Calm_Mind")
            selfstagechanges[3] = selfstagechanges[3] + (0.01 * modweight)
            selfstagechanges[4] = selfstagechanges[4] + (0.01 * modweight)
            extraturns += modweight/100
        if monmovepercent(moves1, "Quiver_Dance") > 0:
            modweight = monmovepercent(moves1, "Quiver_Dance")
            selfstagechanges[3] = selfstagechanges[3] + (0.01 * modweight)
            selfstagechanges[4] = selfstagechanges[4] + (0.01 * modweight)
            selfstagechanges[5] = selfstagechanges[5] + (0.01 * modweight)
            extraturns += modweight/100
        if monmovepercent(moves1, "Clangorous_Soul") > 0:
            modweight = monmovepercent(moves1, "Clangorous_Soul")
            selfstagechanges[1] = selfstagechanges[1] + (0.01 * modweight)
            selfstagechanges[2] = selfstagechanges[2] + (0.01 * modweight)
            selfstagechanges[3] = selfstagechanges[3] + (0.01 * modweight)
            selfstagechanges[4] = selfstagechanges[4] + (0.01 * modweight)
            selfstagechanges[5] = selfstagechanges[5] + (0.01 * modweight)
            extrarecoil = getbasestats(getpokemon(pokemon1)[0:6], ivs1, evs1, natures1[0], natures1[1], [1,1,1,1,1,1])[0]/3
            extrarecoil = extrarecoil * (0.01 * modweight)
            extraturns += modweight/100
        if monmovepercent(moves1, "Iron_Defense") > 0:
            modweight = monmovepercent(moves1, "Iron_Defense")
            selfstagechanges[2] = selfstagechanges[2] + (0.02 * monmovepercent(moves1, "Iron_Defense"))
            extraturns += modweight/100
    if recoil == True:
        if selfdamage != 0:
            health = getbasestats(getpokemon(pokemon2)[0:6], ivs2, evs2, natures2[0], natures2[1], [1,1,1,1,1,1])[0]
            selfdamage = selfdamage * health / 100
            return [dsum, selfdamage, defenselower, spdlower, selfstagechanges, extraturns, extrarecoil]
        else:
            return [dsum, 0, defenselower, spdlower, selfstagechanges, extraturns, extrarecoil]
    else:
        return dsum

def monhasmove(monmoves, move):
    ismonmove = False
    movepercentage = 0
    for i in range(len(monmoves)):
        if monmoves[i][0] == move:
            movepercentage = monmoves[i][1]
            if movepercentage >= 50:
                ismonmove = True
            if movepercentage >= 33.3 and move == "Taunt":
                ismonmove = True
    return ismonmove

def monmovepercent(monmoves, move):
    ismonmove = False
    movepercentage = 0
    for i in range(len(monmoves)):
        if monmoves[i][0] == move:
            movepercentage = monmoves[i][1]
    return movepercentage

def getrecovery(pokemon1, pokemon2, moves1, moves2, matchup1, matchup2, itemset):
    #damagecheck
    recoveryweight1 = (monmovepercent(moves1, "Recover") + monmovepercent(moves1, "Pollen_Puff") + monmovepercent(moves1, "Life_Dew") + monmovepercent(moves1, "Roost"))/100 - monmovepercent(moves2, "Taunt")/100
    recoveryweight2 = (monmovepercent(moves2, "Recover") + monmovepercent(moves2, "Pollen_Puff") + monmovepercent(moves2, "Life_Dew") + monmovepercent(moves2, "Roost"))/100 - monmovepercent(moves1, "Taunt")/100
    weightedrolls = []
    turnstoko1 = dsum1weight/matchup1
    turnstoko2 = dsum2weight/matchup2
    if recoveryweight1 > 0 and recoveryweight2 > 0:
        combinedweight = recoveryweight1 * recoveryweight2
        return [(dsum1weight/10) * combinedweight + matchup1 * (1 - combinedweight), (dsum2weight/10) * combinedweight + matchup2 * (1 - combinedweight)]
    if turnstoko2 >= 2.95 and recoveryweight1 > 0:
        freeturns = turnstoko2 - 3
        if freeturns > 0:
            matchupmultiplier = (freeturns + 2)/freeturns
        else:
            matchupmultiplier = 10
        if turnstoko1 * matchupmultiplier <= 10:
            matchupmultiplier = 10/turnstoko1
        if not monhasmove(moves1, "Salt_Cure") or itemset[1] == "Covert_Cloak":
            return [(dsum1weight/(turnstoko1 * matchupmultiplier)) * recoveryweight1 + matchup1 * (1 - recoveryweight1), (dsum2weight/10) * recoveryweight1 + matchup2 * (1 - recoveryweight1)]
        else:
            #4HKO for Salt Cure on Water/Steel
            #5.3HKO for Salt Cure on Water/Steel with Leftovers
            #8HKO for Salt Cure
            #10HKO for Salt Cure with Leftovers
            salthits = 0
            pokemonstats2 = getpokemon(pokemon2)
            weaktosalt = False
            #typematchups
            if len(pokemonstats2) == 7:  
                if pokemonstats2[6] in [8, 10]:
                    weaktosalt = True
            else:
                if pokemonstats2[6] in [8, 10]:
                    weaktosalt = True
                if pokemonstats2[7] in [8, 10]:
                    weaktosalt = True
            if weaktosalt:
                if itemset[1] == "Leftovers":
                    salthits = 16/3
                else:
                    salthits = 4
            else:
                if itemset[1] == "Leftovers":
                    salthits = 16
                else:
                    salthits = 8
            turnstoko1 = 1/((1/matchupmultiplier)/turnstoko1 + (1 - 1/matchupmultiplier)/salthits)
            if turnstoko1 > 10:
                turnstoko1 = 10
            return [(dsum1weight/turnstoko1) * recoveryweight1 + matchup1 * (1 - recoveryweight1), (dsum2weight/10) * recoveryweight1 + matchup2 * (1 - recoveryweight1)]
    if turnstoko1 >= 2.95 and recoveryweight2 > 0:
        freeturns = turnstoko1 - 3
        if freeturns > 0:
            matchupmultiplier = (freeturns + 2)/freeturns
        else:
            matchupmultiplier = 10
        if turnstoko2 * matchupmultiplier <= 10:
            matchupmultiplier = 10/turnstoko2
        if not monhasmove(moves2, "Salt_Cure") or itemset[0] == "Covert_Cloak":
            return [(dsum1weight/10) * recoveryweight2 + matchup1 * (1 - recoveryweight2), (dsum2weight/(turnstoko2 * matchupmultiplier)) * recoveryweight2 + matchup2 * (1 - recoveryweight2)]
        else:
            #4HKO for Salt Cure on Water/Steel
            #5.3HKO for Salt Cure on Water/Steel with Leftovers
            #8HKO for Salt Cure
            #10HKO for Salt Cure with Leftovers
            salthits = 0
            pokemonstats1 = getpokemon(pokemon1)
            weaktosalt = False
            #typematchups
            if len(pokemonstats1) == 7:  
                if pokemonstats1[6] in [8, 10]:
                    weaktosalt = True
            else:
                if pokemonstats1[6] in [8, 10]:
                    weaktosalt = True
                if pokemonstats1[7] in [8, 10]:
                    weaktosalt = True
            if weaktosalt:
                if itemset[0] == "Leftovers":
                    salthits = 16/3
                else:
                    salthits = 4
            else:
                if itemset[0] == "Leftovers":
                    salthits = 16
                else:
                    salthits = 8
            turnstoko2 = 1/((1/matchupmultiplier)/turnstoko2 + (1 - 1/matchupmultiplier)/salthits)
            if turnstoko2 > 10:
                turnstoko2 = 10
            return [(dsum1weight/10) * recoveryweight2 + matchup1 * (1 - recoveryweight2), (dsum2weight/turnstoko2) * recoveryweight2 + matchup2 * (1 - recoveryweight2)]
    return [matchup1, matchup2]

def getmatchupsum(poke1, poke2, moves1, moves2):
    pokemon1 = poke1[0]
    ivs1 = poke1[1]
    evs1 = poke1[2]
    natures1 = poke1[3]
    ability1 = poke1[4]
    item1 = poke1[5]
    pokemon2 = poke2[0]
    ivs2 = poke2[1]
    evs2 = poke2[2]
    natures2 = poke2[3]
    ability2 = poke2[4]
    item2 = poke2[5]
    statstagechanges = [[0,0,0,0,0,0],[0,0,0,0,0,0]]
    pokemonstrongerattack1 = 0
    pokemonstrongerattack2 = 0
    physicalmoves = []
    specialmoves = []
    for i in range(len(moves2)):
        if getmove(moves2[i][0])[1] == 1:
            physicalmoves.append(0)
        elif getmove(moves2[i][0])[1] == 2:
            specialmoves.append(0)
    if len(physicalmoves) > len(specialmoves):
        pokemonstrongerattack2 = 1
    else:
        pokemonstrongerattack2 = 2
    physicalmoves = []
    specialmoves = []
    for i in range(len(moves1)):
        if getmove(moves1[i][0])[1] == 1:
            physicalmoves.append(0)
        elif getmove(moves1[i][0])[1] == 2:
            specialmoves.append(0)
    if len(physicalmoves) > len(specialmoves):
        pokemonstrongerattack1 = 1
    else:
        pokemonstrongerattack1 = 2
    if ability1 != "Neutralizing_Gas" and ability2 != "Neutralizing_Gas":
        statstagechanges = abilitystatstages(ability1, ability2, statstagechanges[0], statstagechanges[1], item1, item2, pokemonstrongerattack2)
        statstagechanges = abilitystatstages(ability2, ability1, statstagechanges[1], statstagechanges[0], item2, item1, pokemonstrongerattack1)
    else:
        ability1 = None
        ability2 = None
    if item1 == "Mirror_Herb":
        for i in range(6):
            if statstagechanges[0][i] > 0:
                item1 == None
    if item2 == "Mirror_Herb":
        for i in range(6):
            if statstagechanges[1][i] > 0:
                item2 == None
    #Speed/Stat Control
    if monmovepercent(moves1, "Icy_Wind") > 0:
        statstagechanges[0][5] = statstagechanges[0][5] - (monmovepercent(moves1, "Icy_Wind"))/100
    if monmovepercent(moves2, "Icy_Wind") > 0:
        statstagechanges[1][5] = statstagechanges[1][5] - (monmovepercent(moves2, "Icy_Wind"))/100   
    if monmovepercent(moves1, "Electroweb") > 0:
        statstagechanges[0][5] = statstagechanges[0][5] - (monmovepercent(moves1, "Electroweb"))/100
    if monmovepercent(moves2, "Electroweb") > 0:
        statstagechanges[1][5] = statstagechanges[1][5] - (monmovepercent(moves2, "Electroweb"))/100
    if monmovepercent(moves1, "Snarl") > 0:
        statstagechanges[0][3] = statstagechanges[0][3] - (monmovepercent(moves1, "Snarl"))/100
    if monmovepercent(moves2, "Snarl") > 0:
        statstagechanges[1][3] = statstagechanges[1][3] - (monmovepercent(moves2, "Snarl"))/100
    if monmovepercent(moves1, "Struggle_Bug") > 0:
        statstagechanges[0][3] = statstagechanges[0][3] - (monmovepercent(moves1, "Struggle_Bug"))/100
    if monmovepercent(moves2, "Struggle_Bug") > 0:
        statstagechanges[1][3] = statstagechanges[1][3] - (monmovepercent(moves2, "Struggle_Bug"))/100   
    if monmovepercent(moves1, "Spirit_Break") > 0:
        statstagechanges[0][3] = statstagechanges[0][3] - (monmovepercent(moves1, "Spirit_Break"))/100
    if monmovepercent(moves2, "Spirit_Break") > 0:
        statstagechanges[1][3] = statstagechanges[1][3] - (monmovepercent(moves2, "Spirit_Break"))/100
    if item2 == "Clear_Amulet" or item2 == "White_Herb":
        herbconsumed = False
        for i in range(0,6):
            if statstagechanges[0][i] < 0:
                statstagechanges[0][i] = 0
                herbconsumed = True
        if item2 == "White_Herb" and herbconsumed:
            item2 == None
    if item1 == "Clear_Amulet" or item1 == "White_Herb":
        herbconsumed = False
        for i in range(0,6):
            if statstagechanges[1][i] < 0:
                statstagechanges[1][i] = 0
                herbconsumed = True
        if item1 == "White_Herb" and herbconsumed:
            item1 == None
    if item1 == "Adrenaline Orb" and ability2 == "Intimidate":
        statstagechanges[0][5] = statstagechanges[0][5] + 1
    if item2 == "Adrenaline Orb" and ability1 == "Intimidate":
        statstagechanges[1][5] = statstagechanges[1][5] + 1
    if ability1 == "Unaware":
        statstagechanges[1] = [0,0,0,0,0,statstagechanges[1][5]]
    if ability2 == "Unaware":
        statstagechanges[0] = [0,0,0,0,0,statstagechanges[0][5]]
    speedmultiplier = 1
    if item1 in halfspeed:
        speedmultiplier *= 0.5
    if item2 in halfspeed:
        speedmultiplier *= 2
    if ability1 == "Sand_Rush" and ability2 == "Sand_Stream":
        speedmultiplier *= 2
    if ability1 == "Sand_Stream" and ability2 == "Sand_Rush":
        speedmultiplier *= 0.5
    if ability1 == "Swift_Swim" and ability2 == "Drizzle":
        speedmultiplier *= 2
    if ability1 == "Drizzle" and ability2 == "Swift_Swim":
        speedmultiplier *= 0.5
    if ability1 == "Chlorophyll" and ability2 == "Drought":
        speedmultiplier *= 2
    if ability1 == "Drought" and ability2 == "Chlorophyll":
        speedmultiplier *= 0.5
    speedsum = speedcheck(pokemon1, ivs1, evs1, natures1, pokemon2, ivs2, evs2, natures2, statstagechanges, speedmultiplier)
    #Get Field Conditions
    fieldconditions = [0,0]
    if ability1 in ["Sand_Stream", "Drought","Drizzle","Snow_Warning"] and ability2 in ["Sand_Stream", "Drought","Drizzle","Snow_Warning"]:
        if speedsum > 0:
            if ability2 == "Sand_Stream":
                fieldconditions[0] = 3
            elif ability2 == "Drought":
                fieldconditions[0] = 1
            elif ability2 == "Drizzle":
                fieldconditions[0] = 2
            elif ability2 == "Snow_Warning":
                fieldconditions[0] = 4
        elif speedsum < 0:
            if ability1 == "Sand_Stream":
                fieldconditions[0] = 3
            elif ability1 == "Drought":
                fieldconditions[0] = 1
            elif ability1 == "Drizzle":
                fieldconditions[0] = 2
            elif ability1 == "Snow_Warning":
                fieldconditions[0] = 4
        else:
            if random.randint(1,2) == 1:
                if ability1 == "Sand_Stream":
                    fieldconditions[0] = 3
                elif ability1 == "Drought":
                    fieldconditions[0] = 1
                elif ability1 == "Drizzle":
                    fieldconditions[0] = 2
                elif ability1 == "Snow_Warning":
                    fieldconditions[0] = 4
            else:
                if ability2 == "Sand_Stream":
                    fieldconditions[0] = 3
                elif ability2 == "Drought":
                    fieldconditions[0] = 1
                elif ability2 == "Drizzle":
                    fieldconditions[0] = 2
                elif ability2 == "Snow_Warning":
                    fieldconditions[0] = 4
    else:
        if ability1 == "Sand_Stream" or ability2 == "Sand_Stream":
            fieldconditions[0] = 3
        elif ability1 == "Drought" or ability2 == "Drought":
            fieldconditions[0] = 1
        elif ability1 == "Drizzle" or ability2 == "Drizzle":
            fieldconditions[0] = 2
        elif ability1 == "Snow_Warning" or ability2 == "Snow_Warning":
            fieldconditions[0] = 4
    if ability1 in ["Psychic_Surge", "Grassy_Surge","Electric_Surge","Misty_Surge"] and ability2 in ["Psychic_Surge", "Grassy_Surge","Electric_Surge","Misty_Surge"]:
        if speedsum > 0:
            if ability2 == "Psychic_Surge":
                fieldconditions[1] = 2
            elif ability2 == "Grassy_Surge":
                fieldconditions[1] = 1
            elif ability2 == "Electric_Surge":
                fieldconditions[1] = 3
            elif ability2 == "Misty_Surge":
                fieldconditions[1] = 4
        elif speedsum < 0:
            if ability1 == "Psychic_Surge":
                fieldconditions[1] = 2
            elif ability1 == "Grassy_Surge":
                fieldconditions[1] = 1
            elif ability1 == "Electric_Surge":
                fieldconditions[1] = 3
            elif ability1 == "Misty_Surge":
                fieldconditions[1] = 4
        else:
            if random.randint(1,2) == 1:
                if ability1 == "Psychic_Surge":
                    fieldconditions[1] = 2
                elif ability1 == "Grassy_Surge":
                    fieldconditions[1] = 1
                elif ability1 == "Electric_Surge":
                    fieldconditions[1] = 3
                elif ability1 == "Misty_Surge":
                    fieldconditions[1] = 4
            else:
                if ability2 == "Psychic_Surge":
                    fieldconditions[1] = 2
                elif ability2 == "Grassy_Surge":
                    fieldconditions[1] = 1
                elif ability2 == "Electric_Surge":
                    fieldconditions[1] = 3
                elif ability2 == "Misty_Surge":
                    fieldconditions[1] = 4
    else:
        if ability1 == "Psychic_Surge" or ability2 == "Psychic_Surge":
            fieldconditions[1] = 2
        elif ability1 == "Grassy_Surge" or ability2 == "Grassy_Surge":
            fieldconditions[1] = 1
        elif ability1 == "Electric_Surge" or ability2 == "Electric_Surge":
            fieldconditions[1] = 3
        elif ability1 == "Misty_Surge" or ability2 == "Misty_Surge":
            fieldconditions[1] = 4
    #Check For Fake Out
    itemset = [item1, item2, ability1, ability2]
    healthpenalties = []
    if ability1 != "Psychic_Surge" and ability2 != "Psychic_Surge":
        fakeoutcheck = checkfakeout(pokemon1, ivs1, evs1, natures1, pokemon2, ivs2, evs2, natures2, moves1, moves2, statstagechanges, itemset)
        if fakeoutcheck[1] == 1 and item2 != "Covert_Cloak" and ability2 != "Armor_Tail" and ability2 != "Shield_Dust":
            healthpenalties.append(0)
            healthpenalties.append(fakeoutcheck[0])
        elif fakeoutcheck[1] == 2 and item1 != "Covert_Cloak" and ability1 != "Armor_Tail" and ability1 != "Shield_Dust":
            healthpenalties.append(fakeoutcheck[0])
            healthpenalties.append(0)
        else:
            healthpenalties.append(0)
            healthpenalties.append(0)
    else:
        healthpenalties.append(0)
        healthpenalties.append(0)
    #Check For Knock Off
    if monhasmove(moves1, "Knock_Off"):
        if item2 and not(item2 == "Throat_Spray" or ("Seed" in item2) or ("Herb" in item2) or item2 == "Focus_Sash"):
            item2 = ""
    if monhasmove(moves2, "Knock_Off"):
        if item1 and not(item1 == "Throat_Spray" or ("Seed" in item1) or ("Herb" in item1) or item1 == "Focus_Sash"):
            item1 = ""
    #Get Damage Sums
    itemset = [item1, item2, ability1, ability2]
    #print(itemset)
    itemset = [itemset[1], itemset[0], itemset[3], itemset[2]]
    #print(statstagechanges, healthpenalties, itemset)
    damagestat2 = getbestmove(pokemon2, ivs2, evs2, natures2, pokemon1, ivs1, evs1, natures1, moves2, moves1, statstagechanges, healthpenalties[0], fieldconditions, itemset, True)
    recoil2 = damagestat2[1]
    deflower2 = damagestat2[2]
    spdlower2 = damagestat2[3]
    damagesum2 = dsum2weight/damagestat2[0]
    statstagechanges = [statstagechanges[1],statstagechanges[0]]
    itemset = [itemset[1], itemset[0], itemset[3], itemset[2]]
    damagestat1 = getbestmove(pokemon1, ivs1, evs1, natures1, pokemon2, ivs2, evs2, natures2, moves1, moves2, statstagechanges, healthpenalties[1], fieldconditions, itemset, True)
    recoil1 = damagestat1[1]
    deflower1 = damagestat1[2]
    spdlower1 = damagestat1[3]
    damagesum1 = dsum1weight/damagestat1[0]
    statstagechanges = [statstagechanges[1],statstagechanges[0]]
    #print([damagesum1,damagesum2,speedsum])
    #Take Re-Sum
    mainpenalties = []
    mainstagechanges = []
    moves1new = []
    for i in range(len(moves1)):
        moves1new.append([moves1[i][0], moves1[i][1]])
    for i in range(2):
        mainstagechange = []
        for j in range(6):
            mainstagechange.append(statstagechanges[i][j])
        mainstagechanges.append(mainstagechange)
        mainpenalties.append(healthpenalties[i])
    itemset = [itemset[1], itemset[0], itemset[3], itemset[2]]
    if recoil1 != 0 or deflower1 != 0 or spdlower1 != 0:
        if (deflower1 != 0 or spdlower1 != 0) and itemset[1] == "White_Herb":
            deflower1 = 0
            spdlower1 = 0
            itemset[1] = None
        healthpenalties[0] = healthpenalties[0] + recoil1
        statstagechanges[1][2] = statstagechanges[1][2] + deflower1
        statstagechanges[1][4] = statstagechanges[1][4] + spdlower1
        mainpenalties[0] = mainpenalties[0] + recoil1
        mainstagechanges[1][2] = mainstagechanges[1][2] + deflower1
        mainstagechanges[1][4] = mainstagechanges[1][4] + spdlower1
        damagesum2alt = getbestmove(pokemon2, ivs2, evs2, natures2, pokemon1, ivs1, evs1, natures1, moves2, moves1, mainstagechanges, mainpenalties[0], fieldconditions, itemset)
        damagesum2alt = dsum2weight/damagesum2alt
        if True:
            moves1new = []
            for i in range(len(moves1)):
                if moves1[i][0] not in ["Armor_Cannon", "Headlong_Rush", "Glave_Rush", "Close_Combat", "Scale_Shot", "Clanging_Scales", "Head_Smash", "Flare_Blitz","Wood_Hammer","Brave_Bird","Wave_Crash"]:
                    moves1new.append([moves1[i][0], moves1[i][1]])
            mainstagechanges = [mainstagechanges[1],mainstagechanges[0]]
            itemset = [itemset[1], itemset[0], itemset[3], itemset[2]]
            #print(mainstagechanges, mainpenalties, itemset)
            damagesum1alt = dsum1weight/getbestmove(pokemon1, ivs1, evs1, natures1, pokemon2, ivs2, evs2, natures2, moves1new, moves2, mainstagechanges, mainpenalties[1], fieldconditions, itemset)
            #print(damagesum1, damagesum2, damagesum1alt, damagesum2alt)
            mainstagechanges = [mainstagechanges[1],mainstagechanges[0]]
            itemset = [itemset[1], itemset[0], itemset[3], itemset[2]]
            if damagesum1alt - damagesum2 + speedsum >= damagesum1 - damagesum2alt + speedsum:
                healthpenalties[0] = healthpenalties[0] - recoil1
                statstagechanges[1][2] = statstagechanges[1][2] - deflower1
                statstagechanges[1][4] = statstagechanges[1][4] - spdlower1
            else:
                moves1new = []
                for i in range(len(moves1)):
                    moves1new.append([moves1[i][0], moves1[i][1]])
            mainpenalties[0] = mainpenalties[0] - recoil1
            mainstagechanges[1][2] = mainstagechanges[1][2] - deflower1
            mainstagechanges[1][4] = mainstagechanges[1][4] - spdlower1
    statstagechanges = [statstagechanges[1],statstagechanges[0]]
    mainstagechanges = [mainstagechanges[1],mainstagechanges[0]]
    itemset = [itemset[1], itemset[0], itemset[3], itemset[2]]
    moves2new = []
    #print(mainstagechanges)
    for i in range(len(moves2)):
        moves2new.append([moves2[i][0], moves2[i][1]])
    if recoil2 != 0 or deflower2 != 0 or spdlower2 != 0:
        if (deflower2 != 0 or spdlower2 != 0) and itemset[1] == "White_Herb":
            deflower2 = 0
            spdlower2 = 0
            itemset[1] = None
        healthpenalties[1] = healthpenalties[1] + recoil2
        statstagechanges[1][2] = statstagechanges[1][2] + deflower2
        statstagechanges[1][4] = statstagechanges[1][4] + spdlower2
        mainpenalties[1] = mainpenalties[1] + recoil2
        mainstagechanges[1][2] = mainstagechanges[1][2] + deflower2
        mainstagechanges[1][4] = mainstagechanges[1][4] + spdlower2
        damagesum1alt = getbestmove(pokemon1, ivs1, evs1, natures1, pokemon2, ivs2, evs2, natures2, moves1, moves2, mainstagechanges, mainpenalties[1], fieldconditions, itemset)
        damagesum1alt = dsum1weight/damagesum1alt
        if True:
            moves2new = []
            for i in range(len(moves2)):
                if moves2[i][0] not in ["Armor_Cannon", "Headlong_Rush", "Glave_Rush", "Close_Combat", "Scale_Shot", "Clanging_Scales", "Head_Smash", "Flare_Blitz","Wood_Hammer","Brave_Bird","Wave_Crash"]:
                    moves2new.append([moves2[i][0], moves2[i][1]])
            mainstagechanges = [mainstagechanges[1],mainstagechanges[0]]
            itemset = [itemset[1], itemset[0], itemset[3], itemset[2]]
            damagesum2alt = dsum2weight/getbestmove(pokemon2, ivs2, evs2, natures2, pokemon1, ivs1, evs1, natures1, moves2new, moves1, mainstagechanges, mainpenalties[0], fieldconditions, itemset)
            mainstagechanges = [mainstagechanges[1],mainstagechanges[0]]
            itemset = [itemset[1], itemset[0], itemset[3], itemset[2]]
            #print(damagesum1, damagesum2, damagesum1alt, damagesum2alt)
            if damagesum2alt - damagesum1 + speedsum >= damagesum2 - damagesum1alt + speedsum:
                healthpenalties[1] = healthpenalties[1] - recoil2
                statstagechanges[1][2] = statstagechanges[1][2] - deflower2
                statstagechanges[1][4] = statstagechanges[1][4] - spdlower2
            else:
                moves2new = []
                for i in range(len(moves2)):
                    moves2new.append([moves2[i][0], moves2[i][1]])
            mainpenalties[1] = mainpenalties[1] - recoil2
            mainstagechanges[1][2] = mainstagechanges[1][2] - deflower2
            mainstagechanges[1][4] = mainstagechanges[1][4] - spdlower2
    moves1 = moves1new
    moves2 = moves2new
    statstagechanges = [statstagechanges[1],statstagechanges[0]]
    itemset = [itemset[1], itemset[0], itemset[3], itemset[2]]
    #print(statstagechanges, healthpenalties, itemset)
    damagesum2 = dsum2weight/getbestmove(pokemon2, ivs2, evs2, natures2, pokemon1, ivs1, evs1, natures1, moves2, moves1, statstagechanges, healthpenalties[0], fieldconditions, itemset)
    statstagechanges = [statstagechanges[1],statstagechanges[0]]
    itemset = [itemset[1], itemset[0], itemset[3], itemset[2]]
    damagesum1 = dsum1weight/getbestmove(pokemon1, ivs1, evs1, natures1, pokemon2, ivs2, evs2, natures2, moves1, moves2, statstagechanges, healthpenalties[1], fieldconditions, itemset)
    statstagechanges = [statstagechanges[1],statstagechanges[0]]
    finalsum = damagesum1 - damagesum2 + speedsum
    #print([damagesum1,damagesum2,speedsum])
    #print(itemset)
    #print(statstagechanges)
    #Take Alternate Sum
    extraturns1 = 0
    extraturns2 = 0
    altstages1 = damagestat1[4]
    altstages2 = damagestat2[4]
    extrarecoil1 = damagestat1[6]
    extrarecoil2 = damagestat2[6]
    mainstagechanges = []
    for i in range(2):
        mainstagechange = []
        for j in range(6):
            mainstagechange.append(statstagechanges[i][j])
        mainstagechanges.append(mainstagechange)
    #print(statstagechanges)
    itemset = [itemset[1], itemset[0], itemset[3], itemset[2]]
    if altstages2 != [0,0,0,0,0,0]:
        extraturns2 = damagestat2[5]
        for i in range(6):
            statstagechanges[0][i] = statstagechanges[0][i] + altstages2[i]
            mainstagechanges[0][i] = mainstagechanges[0][i] + altstages2[i]
        mirrorherbused = False
        if itemset[1] == "Mirror_Herb":
            for i in range(6):
                statstagechanges[1][i] = statstagechanges[1][i] + altstages2[i]
                mainstagechanges[1][i] = mainstagechanges[1][i] + altstages2[i]
            mirrorherbused = True
        itemset[1] == None
        healthpenalties[1] = healthpenalties[1] + extrarecoil2
        damagesum2a = getbestmove(pokemon2, ivs2, evs2, natures2, pokemon1, ivs1, evs1, natures1, moves2, moves1, mainstagechanges, healthpenalties[0], fieldconditions, itemset) + extraturns2
        damagesum2a = dsum2weight/damagesum2a
        mainstagechanges = [mainstagechanges[1],mainstagechanges[0]]
        itemset = [itemset[1], itemset[0], itemset[3], itemset[2]]
        damagesum1a = getbestmove(pokemon1, ivs1, evs1, natures1, pokemon2, ivs2, evs2, natures2, moves1, moves2, mainstagechanges, healthpenalties[1], fieldconditions, itemset)
        damagesum1a = dsum1weight/damagesum1a
        mainstagechanges = [mainstagechanges[1],mainstagechanges[0]]
        speedsuma = speedcheck(pokemon1, ivs1, evs1, natures1, pokemon2, ivs2, evs2, natures2, mainstagechanges, speedmultiplier)
        for i in range(6):
            mainstagechanges[0][i] = mainstagechanges[0][i] - altstages2[i]
        if mirrorherbused:
            for i in range(6):
                mainstagechanges[1][i] = mainstagechanges[1][i] - altstages2[i]
        healthpenalties[1] = healthpenalties[1] - extrarecoil2
        if damagesum1a - damagesum2a + speedsuma > damagesum1 - damagesum2 + speedsum:
            extrarecoil2 = 0
            extraturns2 = 0
            for i in range(6):
                statstagechanges[0][i] = statstagechanges[0][i] - altstages2[i]
            if mirrorherbused:
                for i in range(6):
                    statstagechanges[1][i] = statstagechanges[1][i] - altstages2[i]
                itemset[0] = "Mirror_Herb"
        itemset = [itemset[1], itemset[0], itemset[3], itemset[2]]
    if altstages1 != [0,0,0,0,0,0]:
        extraturns1 = damagestat1[5]
        for i in range(6):
            statstagechanges[1][i] = statstagechanges[1][i] + altstages1[i]
            mainstagechanges[1][i] = mainstagechanges[1][i] + altstages1[i]
        mirrorherbused = False
        if itemset[0] == "Mirror_Herb":
            for i in range(6):
                statstagechanges[0][i] = statstagechanges[0][i] + altstages1[i]
                mainstagechanges[0][i] = mainstagechanges[0][i] + altstages1[i]
            mirrorherbused = True
        itemset[0] == None
        healthpenalties[0] = healthpenalties[0] + extrarecoil1
        damagesum2a = getbestmove(pokemon2, ivs2, evs2, natures2, pokemon1, ivs1, evs1, natures1, moves2, moves1, mainstagechanges, healthpenalties[0], fieldconditions, itemset)
        damagesum2a = dsum2weight/damagesum2a
        mainstagechanges = [mainstagechanges[1],mainstagechanges[0]]
        itemset = [itemset[1], itemset[0], itemset[3], itemset[2]]
        damagesum1a = getbestmove(pokemon1, ivs1, evs1, natures1, pokemon2, ivs2, evs2, natures2, moves1, moves2, mainstagechanges, healthpenalties[1], fieldconditions, itemset) + extraturns1
        damagesum1a = dsum1weight/damagesum1a
        mainstagechanges = [mainstagechanges[1],mainstagechanges[0]]
        speedsuma = speedcheck(pokemon1, ivs1, evs1, natures1, pokemon2, ivs2, evs2, natures2, mainstagechanges, speedmultiplier)
        for i in range(6):
            mainstagechanges[1][i] = mainstagechanges[1][i] - altstages1[i]
        if mirrorherbused:
            for i in range(6):
                mainstagechanges[0][i] = mainstagechanges[0][i] - altstages1[i]
        healthpenalties[0] = healthpenalties[0] - extrarecoil1
        if damagesum1a - damagesum2a + speedsuma < damagesum1 - damagesum2 + speedsum:
            extrarecoil1 = 0
            extraturns1 = 0
            for i in range(6):
                statstagechanges[1][i] = statstagechanges[1][i] - altstages1[i]
            if mirrorherbused:
                for i in range(6):
                    statstagechanges[0][i] = statstagechanges[0][i] - altstages1[i]
                itemset[1] = "Mirror_Herb"
        itemset = [itemset[1], itemset[0], itemset[3], itemset[2]]
    #print(statstagechanges, healthpenalties, itemset)
    #print(extraturns1, extraturns2)
    healthpenalties[0] = healthpenalties[0] - extrarecoil1
    healthpenalties[1] = healthpenalties[1] - extrarecoil2
    damagesum2 = getbestmove(pokemon2, ivs2, evs2, natures2, pokemon1, ivs1, evs1, natures1, moves2, moves1, statstagechanges, healthpenalties[0], fieldconditions, itemset) + extraturns2
    damagesum2 = dsum2weight/damagesum2
    statstagechanges = [statstagechanges[1],statstagechanges[0]]
    itemset = [itemset[1], itemset[0], itemset[3], itemset[2]]
    damagesum1 = getbestmove(pokemon1, ivs1, evs1, natures1, pokemon2, ivs2, evs2, natures2, moves1, moves2, statstagechanges, healthpenalties[1], fieldconditions, itemset) + extraturns1
    damagesum1 = dsum1weight/damagesum1
    statstagechanges = [statstagechanges[1],statstagechanges[0]]
    speedsum = speedcheck(pokemon1, ivs1, evs1, natures1, pokemon2, ivs2, evs2, natures2, statstagechanges, speedmultiplier)
    finalsum = damagesum1 - damagesum2 + speedsum
    #print(healthpenalties)
    #print(statstagechanges)
    #print([damagesum1,damagesum2,speedsum])
    #Trick Room Detection
    movepercentage = 0
    istrickroom1 = False
    istrickroom2 = False
    if monhasmove(moves1, "Trick_Room") and not (monhasmove(moves2, "Taunt") and item1 != "Mental_Herb" and ability1 != "Magic_Bounce" and ability1 != "Oblivious"):
        istrickroom1 = True
        statstagechanges = [statstagechanges[1],statstagechanges[0]]
        extraturns1 = extraturns1 + 1
        damagesum1 = dsum1weight/(getbestmove(pokemon1, ivs1, evs1, natures1, pokemon2, ivs2, evs2, natures2, moves1, moves2, statstagechanges, healthpenalties[1], fieldconditions, itemset) + extraturns1)
        statstagechanges = [statstagechanges[1],statstagechanges[0]]
    if monhasmove(moves2, "Trick_Room") and not (monhasmove(moves1, "Taunt") and item2 != "Mental_Herb" and ability2 != "Magic_Bounce" and ability2 != "Oblivious"):
        istrickroom2 = True
        itemset = [itemset[1], itemset[0], itemset[3], itemset[2]]
        extraturns2 = extraturns2 + 1
        damagesum2 = dsum2weight/(getbestmove(pokemon2, ivs2, evs2, natures2, pokemon1, ivs1, evs1, natures1, moves2, moves1, statstagechanges, healthpenalties[0], fieldconditions, itemset) + extraturns2)
        itemset = [itemset[1], itemset[0], itemset[3], itemset[2]]
    #Tailwind Detection
    tailwindmod = 1
    if monmovepercent(moves1, "Tailwind") > 0:
        modweight = monmovepercent(moves1, "Tailwind")
        if item1 != "Mental_Herb" and speedsum <= 0 and ability1 != "Prankster":
            modweight = modweight * (1 - monmovepercent(moves2, "Taunt")/100)
        statstagechanges = [statstagechanges[1],statstagechanges[0]]
        extraturns1 = extraturns1 + modweight/100
        damagesum1 = dsum1weight/(getbestmove(pokemon1, ivs1, evs1, natures1, pokemon2, ivs2, evs2, natures2, moves1, moves2, statstagechanges, healthpenalties[1], fieldconditions, itemset) + extraturns1)
        statstagechanges = [statstagechanges[1],statstagechanges[0]]
        tailwindmod = tailwindmod * (1 + modweight/100)
    if monmovepercent(moves2, "Tailwind") > 0:
        modweight = monmovepercent(moves2, "Tailwind")
        if item2 != "Mental_Herb" and speedsum >= 0 and ability2 != "Prankster":
            modweight = modweight * (1 - monmovepercent(moves1, "Taunt")/100)
        itemset = [itemset[1], itemset[0], itemset[3], itemset[2]]
        extraturns2 = extraturns2 + modweight/100
        damagesum2 = dsum2weight/(getbestmove(pokemon2, ivs2, evs2, natures2, pokemon1, ivs1, evs1, natures1, moves2, moves1, statstagechanges, healthpenalties[0], fieldconditions, itemset) + extraturns2)
        itemset = [itemset[1], itemset[0], itemset[3], itemset[2]]
        tailwindmod = tailwindmod / (1 + modweight/100)
    if tailwindmod != 1:
        speedmultiplier = speedmultiplier * tailwindmod
        #print(tailwindmod, speedmultiplier)
        speedsum = speedcheck(pokemon1, ivs1, evs1, natures1, pokemon2, ivs2, evs2, natures2, statstagechanges, speedmultiplier)
        #print(speedsum)
    #Veil Detection
    if (monhasmove(moves1, "Aurora_Veil") or (monhasmove(moves1, "Reflect") and monhasmove(moves1, "Light_Screen"))) and (monhasmove(moves2, "Aurora_Veil") or (monhasmove(moves2, "Reflect") and monhasmove(moves2, "Light_Screen"))):
        itemset = [itemset[1], itemset[0], itemset[3], itemset[2]]
        damagesum2 = (dsum2weight / 1.5)/(getbestmove(pokemon2, ivs2, evs2, natures2, pokemon1, ivs1, evs1, natures1, moves2, moves1, statstagechanges, healthpenalties[0], fieldconditions, itemset) + extraturns2)
        statstagechanges = [statstagechanges[1],statstagechanges[0]]
        itemset = [itemset[1], itemset[0], itemset[3], itemset[2]]
        damagesum1 = (dsum1weight / 1.5)/(getbestmove(pokemon1, ivs1, evs1, natures1, pokemon2, ivs2, evs2, natures2, moves1, moves2, statstagechanges, healthpenalties[1], fieldconditions, itemset) + extraturns1)
        statstagechanges = [statstagechanges[1],statstagechanges[0]]
    else:
        if monhasmove(moves1, "Aurora_Veil") or (monhasmove(moves1, "Reflect") and monhasmove(moves1, "Light_Screen")):
            itemset = [itemset[1], itemset[0], itemset[3], itemset[2]]
            damagesum2a = (dsum2weight / 1.5)/(getbestmove(pokemon2, ivs2, evs2, natures2, pokemon1, ivs1, evs1, natures1, moves2, moves1, statstagechanges, healthpenalties[0], fieldconditions, itemset) + extraturns2)
            statstagechanges = [statstagechanges[1],statstagechanges[0]]
            itemset = [itemset[1], itemset[0], itemset[3], itemset[2]]
            extraturns1 = extraturns1 + 1
            damagesum1a = dsum1weight/(getbestmove(pokemon1, ivs1, evs1, natures1, pokemon2, ivs2, evs2, natures2, moves1, moves2, statstagechanges, healthpenalties[1], fieldconditions, itemset) + extraturns1)
            statstagechanges = [statstagechanges[1],statstagechanges[0]]
            if damagesum1 - damagesum2 + speedsum <= damagesum1a - damagesum2a + speedsum:
                damagesum1 = damagesum1a
                damagesum2 = damagesum2a
        if monhasmove(moves2, "Aurora_Veil") or (monhasmove(moves2, "Reflect") and monhasmove(moves2, "Light_Screen")):
            statstagechanges = [statstagechanges[1],statstagechanges[0]]
            damagesum1b = (dsum1weight / 1.5)/(getbestmove(pokemon1, ivs1, evs1, natures1, pokemon2, ivs2, evs2, natures2, moves1, moves2, statstagechanges, healthpenalties[1], fieldconditions, itemset) + extraturns1)
            statstagechanges = [statstagechanges[1],statstagechanges[0]]
            itemset = [itemset[1], itemset[0], itemset[3], itemset[2]]
            extraturns2 = extraturns2 + 1
            damagesum2b = dsum2weight/(getbestmove(pokemon2, ivs2, evs2, natures2, pokemon1, ivs1, evs1, natures1, moves2, moves1, statstagechanges, healthpenalties[0], fieldconditions, itemset) + extraturns2)
            itemset = [itemset[1], itemset[0], itemset[3], itemset[2]] 
            if damagesum1 - damagesum2 + speedsum >= damagesum1b - damagesum2b + speedsum:
                damagesum1 = damagesum1b
                damagesum2 = damagesum2b
    #print([damagesum1,damagesum2,speedsum])
    #Recovery Detection
    recoveryweight1 = (monmovepercent(moves1, "Recover") + monmovepercent(moves1, "Pollen_Puff") + monmovepercent(moves1, "Life_Dew") + monmovepercent(moves1, "Roost"))/100 - monmovepercent(moves2, "Taunt")/100
    recoveryweight2 = (monmovepercent(moves2, "Recover") + monmovepercent(moves2, "Pollen_Puff") + monmovepercent(moves2, "Life_Dew") + monmovepercent(moves2, "Roost"))/100 - monmovepercent(moves1, "Taunt")/100
    if recoveryweight1 > 0 or recoveryweight2 > 0:
        recoverycalc = getrecovery(pokemon1, pokemon2, moves1, moves2, damagesum1, damagesum2, itemset)
        if recoveryweight1 > 0 and recoveryweight2 > 0:
            damagesum1 = recoverycalc[0]
            damagesum2 = recoverycalc[1]
        elif recoveryweight1 > 0:
            if recoverycalc[0] - recoverycalc[1] + speedsum >= damagesum1 - damagesum2 + speedsum:
                damagesum1 = recoverycalc[0]
                damagesum2 = recoverycalc[1]
        else:
            if recoverycalc[0] - recoverycalc[1] + speedsum <= damagesum1 - damagesum2 + speedsum:
                damagesum1 = recoverycalc[0]
                damagesum2 = recoverycalc[1]
    #print([damagesum1,damagesum2,speedsum])
    #Paralysis Detection
    if ability1 != "Misty_Surge" and ability2 != "Misty_Surge":
        if monhasmove(moves1, "Thunder_Wave"):
            if ability2 not in ["Good_as_Gold","Purifying_Salt","Misty_Surge","Comatose","Magic_Bounce","Psychic_Surge"] and item2 != "Lum_Berry":
                moveuse = monmovepercent(moves1, "Thunder_Wave")/100
                if len(getpokemon(pokemon2)) == 7:
                    if getpokemon(pokemon2)[6] not in [4, 12, 16]:
                        speedmultiplier = speedmultiplier * (1 + moveuse)
                        speedsumnew = speedcheck(pokemon1, ivs1, evs1, natures1, pokemon2, ivs2, evs2, natures2, statstagechanges, speedmultiplier)
                        if (dsum1weight/(dsum1weight/damagesum1 + moveuse * (10/9)) - damagesum2/(1/3 * moveuse + 1) + speedsumnew) >= (damagesum1 - damagesum2 + speedsum):
                            damagesum1 = dsum1weight/(dsum1weight/damagesum1 + moveuse * (10/9))
                            damagesum2 = damagesum2/(1/3 * moveuse + 1)
                            speedsum = speedcheck(pokemon1, ivs1, evs1, natures1, pokemon2, ivs2, evs2, natures2, statstagechanges, speedmultiplier)
                        else:
                            speedmultiplier = speedmultiplier / (1 + moveuse)
                            speedsum = speedcheck(pokemon1, ivs1, evs1, natures1, pokemon2, ivs2, evs2, natures2, statstagechanges, speedmultiplier)
                if len(getpokemon(pokemon2)) == 8:
                    if getpokemon(pokemon2)[6] not in [4, 12, 16] and getpokemon(pokemon2)[7] not in [4, 12, 16]:
                        speedmultiplier = speedmultiplier * (1 + moveuse)
                        speedsumnew = speedcheck(pokemon1, ivs1, evs1, natures1, pokemon2, ivs2, evs2, natures2, statstagechanges, speedmultiplier)
                        if (dsum1weight/(dsum1weight/damagesum1 + moveuse * (10/9)) - damagesum2/(1/3 * moveuse + 1) + speedsumnew) >= (damagesum1 - damagesum2 + speedsum):
                            damagesum1 = dsum1weight/(dsum1weight/damagesum1 + moveuse * (10/9))
                            damagesum2 = damagesum2/(1/3 * moveuse + 1)
                            speedsum = speedcheck(pokemon1, ivs1, evs1, natures1, pokemon2, ivs2, evs2, natures2, statstagechanges, speedmultiplier)
                        else:
                            speedmultiplier = speedmultiplier / (1 + moveuse)
                            speedsum = speedcheck(pokemon1, ivs1, evs1, natures1, pokemon2, ivs2, evs2, natures2, statstagechanges, speedmultiplier)
        if monhasmove(moves2, "Thunder_Wave"):
            if ability1 not in ["Good_as_Gold","Purifying_Salt","Misty_Surge","Comatose","Magic_Bounce","Psychic_Surge"] and item1 != "Lum_Berry":
                moveuse = monmovepercent(moves2, "Thunder_Wave")/100
                if len(getpokemon(pokemon1)) == 7:
                    if getpokemon(pokemon1)[6] not in [4, 12, 16]:
                        speedmultiplier = speedmultiplier / (1 + moveuse)
                        speedsumnew = speedcheck(pokemon1, ivs1, evs1, natures1, pokemon2, ivs2, evs2, natures2, statstagechanges, speedmultiplier)
                        if (damagesum1/(1/3 * moveuse + 1) - dsum2weight/(dsum2weight/damagesum2 + moveuse * (10/9)) + speedsumnew) <= (damagesum1 - damagesum2 + speedsum):
                            damagesum1 = damagesum1/(1/3 * moveuse + 1)
                            damagesum2 = dsum2weight/(dsum2weight/damagesum2 + moveuse * (10/9))
                            speedsum = speedcheck(pokemon1, ivs1, evs1, natures1, pokemon2, ivs2, evs2, natures2, statstagechanges, speedmultiplier)
                        else:
                            speedmultiplier = speedmultiplier * (1 + moveuse)
                            speedsum = speedcheck(pokemon1, ivs1, evs1, natures1, pokemon2, ivs2, evs2, natures2, statstagechanges, speedmultiplier)
                if len(getpokemon(pokemon1)) == 8:
                    if getpokemon(pokemon1)[6] not in [4, 12, 16] and getpokemon(pokemon1)[7] not in [4, 12, 16]:
                        speedmultiplier = speedmultiplier / (1 + moveuse)
                        speedsumnew = speedcheck(pokemon1, ivs1, evs1, natures1, pokemon2, ivs2, evs2, natures2, statstagechanges, speedmultiplier)
                        if (damagesum1/(1/3 * moveuse + 1) - dsum2weight/(dsum2weight/damagesum2 + moveuse * (10/9)) + speedsumnew) <= (damagesum1 - damagesum2 + speedsum):
                            damagesum1 = damagesum1/(1/3 * moveuse + 1)
                            damagesum2 = dsum2weight/(dsum2weight/damagesum2 + moveuse * (10/9))
                            speedsum = speedcheck(pokemon1, ivs1, evs1, natures1, pokemon2, ivs2, evs2, natures2, statstagechanges, speedmultiplier)
                        else:
                            speedmultiplier = speedmultiplier * (1 + moveuse)
                            speedsum = speedcheck(pokemon1, ivs1, evs1, natures1, pokemon2, ivs2, evs2, natures2, statstagechanges, speedmultiplier)
    #print([damagesum1,damagesum2,speedsum])
    #Burn Detection
    if ability1 != "Misty_Surge" and ability2 != "Misty_Surge":
        if monhasmove(moves1, "Will-O-Wisp") and pokemonstrongerattack2 == 1:
            if ability2 not in ["Good_as_Gold","Purifying_Salt","Misty_Surge","Comatose","Magic_Bounce"] and item2 != "Lum_Berry":
                moveuse = monmovepercent(moves1, "Will-O-Wisp")/100
                if speedsum >= 0 and item2 != "Mental_Herb":
                    moveuse = moveuse - monmovepercent(moves2, "Taunt")/100
                if len(getpokemon(pokemon2)) == 7:
                    if getpokemon(pokemon2)[6] != 9:
                        if dsum1weight/(dsum1weight/damagesum1 + moveuse * (20/17)) - damagesum2/(1 + moveuse) >= damagesum1 - damagesum2:
                            damagesum1 = dsum1weight/(dsum1weight/damagesum1 + moveuse * (20/17))
                            damagesum2 = damagesum2/(1 + moveuse)
                if len(getpokemon(pokemon2)) == 8:
                    if getpokemon(pokemon2)[6] != 9 and getpokemon(pokemon2)[7] != 9:
                        if dsum1weight/(dsum1weight/damagesum1 + moveuse * (20/17)) - damagesum2/(1 + moveuse) >= damagesum1 - damagesum2:
                            damagesum1 = dsum1weight/(dsum1weight/damagesum1 + moveuse * (20/17))
                            damagesum2 = damagesum2/(1 + moveuse)
        if monhasmove(moves2, "Will-O-Wisp") and pokemonstrongerattack1 == 1:
            if ability1 not in ["Good_as_Gold","Purifying_Salt","Misty_Surge","Comatose","Magic_Bounce"] and item1 != "Lum_Berry":
                moveuse = monmovepercent(moves2, "Will-O-Wisp")/100
                if speedsum <= 0 and item1 != "Mental_Herb":
                    moveuse = moveuse - monmovepercent(moves1, "Taunt")/100
                if len(getpokemon(pokemon1)) == 7:
                    if getpokemon(pokemon1)[6] != 9:
                        if damagesum1/(1 + moveuse) - dsum2weight/(dsum2weight/damagesum2 + moveuse * (20/17)) <= damagesum1 - damagesum2:
                            damagesum1 = damagesum1/(1 + moveuse)
                            damagesum2 = dsum2weight/(dsum2weight/damagesum2 + moveuse * (20/17))
                if len(getpokemon(pokemon1)) == 8:
                    if getpokemon(pokemon1)[6] != 9 and getpokemon(pokemon1)[7] != 9:
                        if damagesum1/(1 + moveuse) - dsum2weight/(dsum2weight/damagesum2 + moveuse * (20/17)) <= damagesum1 - damagesum2:
                            damagesum1 = damagesum1/(1 + moveuse)
                            damagesum2 = dsum2weight/(dsum2weight/damagesum2 + moveuse * (20/17))
    #Spore Detection
    #Spore causes 1-3 turns of sleep, resulting in:
    #Mon using Spore can defeat opponent in 1.5x of turns, but opponent needs x3 turns to defeat back
    if ability1 != "Electric_Surge" and ability2 != "Electric_Surge" and ability1 != "Misty_Surge" and ability2 != "Misty_Surge":
        if monhasmove(moves1, "Spore") or monhasmove(moves1, "Sleep_Powder"):
            moveuse = monmovepercent(moves1, "Spore")/100 + monmovepercent(moves1, "Sleep_Powder")/100
            if speedsum <= 0 and item1 != "Mental_Herb":
                moveuse = moveuse - monmovepercent(moves2, "Taunt")/100
            if ability2 not in ["Sap_Sipper", "Good_as_Gold" ,"Vital_Spirit", "Insomnia", "Purifying_Salt", "Electric_Surge", "Misty_Surge","Sweet_Veil","Comatose", "Overcoat", "Magic_Bounce"] and item2 != "Safety_Goggles" and item2 != "Lum_Berry":
                if len(getpokemon(pokemon2)) == 7:
                    if getpokemon(pokemon2)[6] != 11:
                        if monhasmove(moves1, "Spore"):
                            if damagesum1 - damagesum2 <= damagesum1/(1 + 0.5 * moveuse) - damagesum2/(1 + 2 * moveuse):
                                damagesum1 = damagesum1/ (1 + 0.5 * moveuse)
                                damagesum2 = damagesum2/ (1 + 2 * moveuse)
                        else:
                            if damagesum1 - damagesum2 <= damagesum1/(1 + (2/3) * moveuse) - damagesum2/(1 + 1.5 * moveuse):
                                damagesum1 = damagesum1/(1 + (2/3) * moveuse)
                                damagesum2 = damagesum2/(1 + 1.5 * moveuse)
                if len(getpokemon(pokemon2)) == 8:
                    if getpokemon(pokemon2)[6] != 11 and getpokemon(pokemon2)[7] != 11:
                        if monhasmove(moves1, "Spore"):
                            if damagesum1 - damagesum2 <= damagesum1/(1 + 0.5 * moveuse) - damagesum2/(1 + 2 * moveuse):
                                damagesum1 = damagesum1/ (1 + 0.5 * moveuse)
                                damagesum2 = damagesum2/ (1 + 2 * moveuse)
                        else:
                            if damagesum1 - damagesum2 <= damagesum1/(1 + (2/3) * moveuse) - damagesum2/(1 + 1.5 * moveuse):
                                damagesum1 = damagesum1/(1 + (2/3) * moveuse)
                                damagesum2 = damagesum2/(1 + 1.5 * moveuse)
        if monhasmove(moves2, "Spore") or monhasmove(moves2, "Sleep_Powder"):
            moveuse = monmovepercent(moves2, "Spore")/100 + monmovepercent(moves2, "Sleep_Powder")/100
            if speedsum >= 0 and item2 != "Mental_Herb":
                moveuse = moveuse - monmovepercent(moves1, "Taunt")/100
            if ability1 not in ["Sap_Sipper", "Good_as_Gold" ,"Vital_Spirit", "Insomnia", "Purifying_Salt", "Electric_Surge", "Misty_Surge","Sweet_Veil","Comatose", "Overcoat", "Magic_Bounce"] and item1 != "Safety_Goggles" and item1 != "Lum_Berry":
                if len(getpokemon(pokemon1)) == 7:
                    if getpokemon(pokemon1)[6] != 11:
                        if monhasmove(moves2, "Spore"):
                            if damagesum2 - damagesum1 <= damagesum2/(1 + 0.5 * moveuse) - damagesum1/(1 + 2 * moveuse):
                                damagesum2 = damagesum2/ (1 + 0.5 * moveuse)
                                damagesum1 = damagesum1/ (1 + 2 * moveuse)
                        else:
                            if damagesum2 - damagesum1 <= damagesum2/(1 + (2/3) * moveuse) - damagesum1/(1 + 1.5 * moveuse):
                                damagesum2 = damagesum2/(1 + (2/3) * moveuse)
                                damagesum1 = damagesum1/(1 + 1.5 * moveuse)
                if len(getpokemon(pokemon1)) == 8:
                    if getpokemon(pokemon1)[6] != 11 and getpokemon(pokemon1)[7] != 11:
                        if monhasmove(moves2, "Spore"):
                            if damagesum2 - damagesum1 <= damagesum2/(1 + 0.5 * moveuse) - damagesum1/(1 + 2 * moveuse):
                                damagesum2 = damagesum2/ (1 + 0.5 * moveuse)
                                damagesum1 = damagesum1/ (1 + 2 * moveuse)
                        else:
                            if damagesum2 - damagesum1 <= damagesum2/(1 + (2/3) * moveuse) - damagesum1/(1 + 1.5 * moveuse):
                                damagesum2 = damagesum2/(1 + (2/3) * moveuse)
                                damagesum1 = damagesum1/(1 + 1.5 * moveuse)
    if (not (istrickroom1 and istrickroom2)) and (istrickroom1 or istrickroom2):
        if item1 == "Room_Service":
            statstagechanges[0][5] = statstagechanges[0][5] - 1
            speedsum = speedcheck(pokemon1, ivs1, evs1, natures1, pokemon2, ivs2, evs2, natures2, statstagechanges, speedmultiplier)
        if item2 == "Room_Service":
            statstagechanges[1][5] = statstagechanges[1][5] - 1
            speedsum = speedcheck(pokemon1, ivs1, evs1, natures1, pokemon2, ivs2, evs2, natures2, statstagechanges, speedmultiplier)
        if istrickroom1:
            if finalsum <= damagesum1 - damagesum2 - speedsum:
                finalsum = damagesum1 - damagesum2 - speedsum
        else:
            if finalsum >= damagesum1 - damagesum2 - speedsum:
                finalsum = damagesum1 - damagesum2 - speedsum
    else:
        finalsum = damagesum1 - damagesum2 + speedsum
    #print(itemset, statstagechanges)
    #print([damagesum1,damagesum2,speedsum])
    return finalsum

def defivs(poke):
    poke[1] = [31,31,31,31,31,31]
    return poke
  
def subivs(poke, stat):
    poke[1][stat - 1] = poke[1][stat - 1] - 1
    return poke

def addevs(poke, stat):
    if poke[2][stat - 1] == 0:
        poke[2][stat - 1] = 4
    else:
        poke[2][stat - 1] = poke[2][stat - 1] + 8
    return poke

def subevs(poke, stat):
    if poke[2][stat - 1] == 4:
        poke[2][stat - 1] = 0
    else:
        poke[2][stat - 1] = poke[2][stat - 1] - 8
    return poke

def setevs(poke, stat, evsinput):
    poke[2][stat - 1] = evsinput
    return poke

def checkevlimit(poke):
    evcount = 0
    for i in range(0,5):
        evcount += poke[2][i]
    if evcount > 508:
        return True
    else:
        return False

def defaultspreads(pokeid):
    poke = [pokeid, [], [0,0,0,0,0,0], [1, 1]]
    poke = defivs(poke)
    pokestats = getpokemon(pokeid)
    if pokestats[0] > pokestats[5]:
        for i in range(0,32):
            poke = addevs(poke, 1)
        poke = addevs(poke, 6)
    else:
        for i in range(0,32):
            poke = addevs(poke, 6)
        poke = addevs(poke, 1)
    if pokestats[1] > pokestats[3]:
        for i in range(0,32):
            poke = addevs(poke, 2)
        poke[3][1] = 4
        if pokestats[0] < pokestats[5] and pokestats[1] < pokestats[5]:
            poke[3][0] = 6
        else:
            poke[3][0] = 2
    else:
        for i in range(0,32):
            poke = addevs(poke, 4)
        poke[3][1] = 2
        if pokestats[0] < pokestats[5] and pokestats[3] < pokestats[5]:
            poke[3][0] = 6
        else:
            poke[3][0] = 4
    poke.append([])
    poke.append([])
    return poke

def addability(poke, ability):
    poke[4] = ability
    return poke

def additem(poke, item):
    poke[5] = item
    return poke
    
def matchupspreads(numid):
    pokeid = usagestats[numid][0]
    pokestats = getpokemon(pokeid)
    pokes = []
    weight = 0
    for i in range(0, len(movesets[numid][2])):
        for j in range(0, len(movesets[numid][0])):
            for k in range(0, len(movesets[numid][1])): 
                poke = [pokeid, [], [0,0,0,0,0,0], [1, 1], [], []]
                poke = defivs(poke)
                poke[2][0] = movesets[numid][2][i][0][1]
                poke[2][1] = movesets[numid][2][i][0][2]
                poke[2][2] = movesets[numid][2][i][0][3]
                poke[2][3] = movesets[numid][2][i][0][4]
                poke[2][4] = movesets[numid][2][i][0][5]
                poke[2][5] = movesets[numid][2][i][0][6]
                assignednature = getnaturefromid(getnaturefromname(movesets[numid][2][i][0][0]))
                poke[3][0] = int(assignednature[0])
                poke[3][1] = int(assignednature[1])
                if poke[2][1] == 0 and poke[3][1] == 1:
                    poke[1][1] = 0
                if poke[2][5] == 0 and poke[3][1] == 5:
                    poke[1][5] = 0
                poke = addability(poke, movesets[numid][0][j][0])
                poke = additem(poke, movesets[numid][1][k][0])
                weight += movesets[numid][2][i][1] * movesets[numid][0][j][1] * movesets[numid][1][k][1] / 10000
                pokes.append([poke,movesets[numid][2][i][1] * movesets[numid][0][j][1] * movesets[numid][1][k][1] / 10000])
    return [pokes, weight]

def movespreads(numid):
    pokeid = usagestats[numid][0]
    pokes = []
    weight = 0
    for i in range(0, len(movesets[numid][3])):
        weight += movesets[numid][3][i][1]
        pokes.append([movesets[numid][3][i][0],movesets[numid][3][i][1]])
    for i in range(0, len(movesets[numid][3])):
        if pokes[i][1] >= weight/4:
            pokes[i][1] = 100
        else:
            pokes[i][1] = pokes[i][1]/(weight/400)
    return pokes

def getmatchups(poke, matchupid, pokemoves):
    spreadstats = matchupspreads(matchupid)
    spreads = spreadstats[0]
    weight = spreadstats[1]
    currentsum = 0
    for i in range(0,len(spreads)):
        localweight = spreads[i][1]
        localsum = getmatchupsum(poke, spreads[i][0], pokemoves, movesets[matchupid][3])
        currentsum += localsum * (localweight/weight)
    return currentsum

def getstatmatchups(pokeid, matchupid):
    spreadstats = matchupspreads(pokeid)
    spreads = spreadstats[0]
    weight = spreadstats[1]
    currentsum = 0
    for i in range(0,len(spreads)):
        localweight = spreads[i][1]
        localsum = getmatchups(spreads[i][0], matchupid, movesets[pokeid][3])
        currentsum += localsum * (localweight/weight)
    return currentsum

def getdualstatmatchups(pokeid, matchupid):
    spreadstats = matchupspreads(pokeid)
    spreads = spreadstats[0]
    difference = 0
    for i in range(0,len(spreads)):
        localweight = spreads[i][1]
        spreadstats2 = matchupspreads(matchupid)
        spreads2 = spreadstats2[0]
        for j in range(0,len(spreads2)):
            localsum = getmatchupsum(spreads[i][0], spreads2[j][0], movesets[pokeid][3], movesets[matchupid][3])
            localsum2 = getmatchupsum(spreads2[j][0], spreads[i][0], movesets[matchupid][3], movesets[pokeid][3])
            #print(localsum + localsum2)
            difference += localsum + localsum2
        #if difference != 0:
            #break
    return difference
            
def getallmatchups(poke, pokemoves):
    currentsum = 0
    for i in range(0,57):
        matchupsum = getmatchups(poke, i, pokemoves)
        print([usagestats[i][0], matchupsum])
        currentsum += matchupsum * math.sqrt(usagestats[i][1]) / 10
    return currentsum

def getallstatmatchups(pokeid):
    currentsum = 0
    matchupcalcs = []
    for i in range(0,57):
        matchupsum = -getstatmatchups(pokeid, i)
        print([usagestats[i][0], matchupsum])
        currentsum += matchupsum * math.sqrt(usagestats[i][1]) / 10
        matchupcalcs.append(matchupsum)
    return currentsum, matchupcalcs

def speedtest(poke, pokemoves):
    testpoke = poke
    testmatch = getallmatchups(testpoke, pokemoves)
    print(testpoke)
    print(testmatch)
    for i in range(0, 31):
        testpoke = subevs(testpoke, 1)
        testpoke = addevs(testpoke, 6)
        testmatch = getallmatchups(testpoke, pokemoves)
        print(testpoke)
        print(testmatch)

def healthtest(poke, pokemoves):
    testpoke = poke
    for i in range(0, 31):
        testpoke = subevs(testpoke, 1)
        testpoke = addevs(testpoke, 6)
    testmatch = getallmatchups(testpoke, pokemoves)
    print(testpoke)
    print(testmatch)
    for i in range(0, 31):
        testpoke = subevs(testpoke, 4)
        testpoke = addevs(testpoke, 1)
        testmatch = getallmatchups(testpoke, pokemoves)
        print(testpoke)
        print(testmatch)

def dualtest(poke, pokemoves):
    testpoke = poke
    bestpoke = None
    bestmatch = -10000
    testpoke = setevs(testpoke, 6, 252)
    testpoke = setevs(testpoke, 2, 256 - poke[2][0])
    testmatch = getallmatchups(testpoke, pokemoves)
    if testmatch >= bestmatch:
        bestpoke = testpoke
        bestmatch = testmatch
    while testpoke[2][1] != 252:
        testpoke = subevs(testpoke, 6)
        testpoke = addevs(testpoke, 2)
        testmatch = getallmatchups(testpoke, pokemoves)
        if testmatch >= bestmatch:
            bestpoke = testpoke
            bestmatch = testmatch
        print(testpoke)
        print(testmatch)
    print(bestpoke)
    print(bestmatch)
    for i in range(0, 31):
        bestpoke = None
        bestmatch = -10000
        testpoke = subevs(testpoke, 1)
        testpoke = setevs(testpoke, 6, 252)
        testpoke = setevs(testpoke, 2, 256 - poke[2][0])
        testmatch = getallmatchups(testpoke, pokemoves)
        if testmatch >= bestmatch:
            bestpoke = testpoke
            bestmatch = testmatch
        while testpoke[2][1] != 252:
            testpoke = subevs(testpoke, 6)
            testpoke = addevs(testpoke, 2)
            testmatch = getallmatchups(testpoke, pokemoves)
            if testmatch >= bestmatch:
                bestpoke = testpoke
                bestmatch = testmatch
        print(bestpoke)
        print(bestmatch)

def getalldata(filetowrite):
    with open(filetowrite, "a") as file:
        if dsum1weight == dsum2weight:
            for i in range(0, 57):
                for j in range(i + 1, 57):
                    matchupsum = getstatmatchups(i, j)
                    print([usagestats[i][0], usagestats[j][0], matchupsum])
                    file.write(str([usagestats[i][0], usagestats[j][0], matchupsum]))
                    file.write("\n")
        else:
            for i in range(0, 57):
                for j in range(0, 57):
                    matchupsum = getstatmatchups(i, j)
                    print([usagestats[i][0], usagestats[j][0], matchupsum])
                    file.write(str([usagestats[i][0], usagestats[j][0], matchupsum]))
                    file.write("\n")

def getalldatafrom(filetowrite, startpoint):
    with open(filetowrite, "a") as file:
        if dsum1weight == dsum2weight:
            for i in range(startpoint, 57):
                for j in range(i + 1, 57):
                    matchupsum = getstatmatchups(i, j)
                    print([usagestats[i][0], usagestats[j][0], matchupsum])
                    file.write(str([usagestats[i][0], usagestats[j][0], matchupsum]))
                    file.write("\n")
        else:
            for i in range(startpoint, 57):
                for j in range(0, 57):
                    matchupsum = getstatmatchups(i, j)
                    print([usagestats[i][0], usagestats[j][0], matchupsum])
                    file.write(str([usagestats[i][0], usagestats[j][0], matchupsum]))
                    file.write("\n")
    
poke1 = defaultspreads("Garganacl")
poke1 = addability(poke1, "")
poke1 = additem(poke1, "Leftovers")
poke2 = defaultspreads("Dragonite")
poke2 = addability(poke2, "Multiscale")
poke2 = additem(poke2, "Loaded_Dice")
poke3 = defaultspreads("Dragonite")
poke3 = addability(poke3, "Multiscale")
poke3 = additem(poke3, " ")
#print(poke1)
#print(movespreads(45))
#print(getallmatchups(poke1, [["Close_Combat", 100], ["Sleep_Powder", 50]]))
#print(getallmatchups(poke1, [["Close_Combat", 100], ["Sleep_Powder", 100]]))
#print(getmatchups(poke2, 4, [["Spirit_Break", 100]]))
#print(getmatchups(poke2, 4, [["Spirit_Break", 100], ["Thunder_Wave", 100]]))
#print(getallmatchups(poke1, [["Salt_Cure",100]]))
#print(getstatmatchups(33,43))
#print(getstatmatchups(43,33))


#print(getdualstatmatchups(0, 56))
#print(getdualstatmatchups(17, 36))
#print(getdualstatmatchups(17, 45))

#print(getallstatmatchups(50)[0])



#filetowrite = "matchupdatad" + str(dsum1weight) + "d" + str(dsum2weight) + "x1.txt"
#testfile = open(filetowrite, "a")
#getalldata(filetowrite)

#with open(filetowrite, "a") as file:
    #matchupsum = getstatmatchups(7, 0)
    #print([usagestats[7][0], usagestats[0][0], matchupsum])
    #file.write(str([usagestats[7][0], usagestats[0][0], matchupsum]))
    #file.write("\n")
    #matchupsum = getstatmatchups(7, 34)
    #print([usagestats[7][0], usagestats[34][0], matchupsum])
    #file.write(str([usagestats[7][0], usagestats[34][0], matchupsum]))
    #file.write("\n")
    #matchupsum = getstatmatchups(7, 54)
    #print([usagestats[7][0], usagestats[54][0], matchupsum])
    #file.write(str([usagestats[7][0], usagestats[54][0], matchupsum]))
    #file.write("\n")
    #matchupsum = getstatmatchups(12, 0)
    #print([usagestats[12][0], usagestats[0][0], matchupsum])
    #file.write(str([usagestats[12][0], usagestats[0][0], matchupsum]))
    #file.write("\n")
    #matchupsum = getstatmatchups(12, 34)
    #print([usagestats[12][0], usagestats[34][0], matchupsum])
    #file.write(str([usagestats[12][0], usagestats[34][0], matchupsum]))
    #file.write("\n")
    #matchupsum = getstatmatchups(12, 54)
    #print([usagestats[12][0], usagestats[54][0], matchupsum])
    #file.write(str([usagestats[12][0], usagestats[54][0], matchupsum]))
    #file.write("\n")

#print(getmatchupsum(poke1, poke2, [["Knock_Off", 100]], [["Scale_Shot", 100]]))






#input()

















#TEAMBUILDERPORTION#


#Insert File Name Here
filetoanalyze = "matchupdatad" + str(dsum1weight) + "d" + str(dsum2weight) + "x1.txt"
matchupstats = []

for i in range(0,57):
    matchupstats.append([])
    for j in range(0,57):
        matchupstats[i].append(0)

with open(filetoanalyze) as pokematchstats:
    for poke in pokematchstats:
        if len(poke) > 6:
            pokesep = poke.replace("\n","")
            pokesep = pokesep.replace(" ","")
            pokesep = pokesep.replace("'","")
            pokesep = pokesep.replace("[","")
            pokesep = pokesep.replace("]","")
            pokestat = pokesep.split(",")
            pokestat[0] = findpokemon(pokestat[0])
            pokestat[1] = findpokemon(pokestat[1])
            pokestat[2] = float(pokestat[2])
            matchupstats[pokestat[0]][pokestat[1]] = pokestat[2]
            matchupstats[pokestat[1]][pokestat[0]] = pokestat[2] * -1

#Data Manipulators
decreasespread = False

if decreasespread:
    for i in range(0,57):
        for j in range(0,57):
            if matchupstats[i][j] >= 0:
                matchupstats[i][j] = math.sqrt(matchupstats[i][j])
            else:
                matchupstats[i][j] = math.sqrt(matchupstats[i][j] * -1) * -1

def getworstmatchups(mon):
    monmatchups = matchupstats[mon]
    #Variable to toggle when needed
    monstocheck = 5
    badmatchups = []
    badmatchupids = []
    for i in range(monstocheck):
        badmatchups.append(10)
        badmatchupids.append(0)
    print("Testing:")
    print(usagestats[mon][0])
    for i in range(0, 57):
        currentmatchup = matchupstats[mon][i]
        level = -1
        for j in range(monstocheck):
            if currentmatchup <= badmatchups[j]:
                level += 1
            else:
                break
        if level >= 0:  
            badmatchups.pop(0)
            badmatchups.insert(level, currentmatchup)
            badmatchupids.pop(0)
            badmatchupids.insert(level, i)
    print(badmatchups)
    print(badmatchupids)
    for i in range(0, monstocheck):
        print(usagestats[badmatchupids[i]][0], badmatchups[i])
    return badmatchupids

def getbestmatchupsagainst(mon):
    monmatchups = matchupstats[mon]
    #Variable to toggle when needed
    monstocheck = 5
    badmatchups = []
    badmatchupids = []
    for i in range(monstocheck):
        badmatchups.append(-10)
        badmatchupids.append(0)
    print("Testing:")
    print(usagestats[mon][0])
    for i in range(0, 57):
        currentmatchup = matchupstats[i][mon]
        level = -1
        for j in range(monstocheck):
            if currentmatchup >= badmatchups[j]:
                level += 1
            else:
                break
        if level >= 0:  
            badmatchups.pop(0)
            badmatchups.insert(level, currentmatchup)
            badmatchupids.pop(0)
            badmatchupids.insert(level, i)
    print(badmatchups)
    print(badmatchupids)
    for i in range(0, monstocheck):
        print(usagestats[badmatchupids[i]][0], badmatchups[i])

def getoverallbestmatchupsagainst(mons):
    matchupsummaries = []
    for i in range(0,57):
        currentmatchup = 0
        for j in range(len(mons)):
            currentmatchup = currentmatchup + (matchupstats[i][mons[j]] * (j * 0.5 + 3)) 
        matchupsummaries.append(currentmatchup)
    #Variable to toggle when needed
    monstocheck = 5
    badmatchups = []
    badmatchupids = []
    for i in range(monstocheck):
        badmatchups.append(-10)
        badmatchupids.append(0)
    #print("Best Counters:")
    for i in range(0, 57):
        currentmatchup = matchupsummaries[i]
        level = -1
        for j in range(monstocheck):
            if currentmatchup >= badmatchups[j]:
                level += 1
            else:
                break
        if level >= 0:  
            badmatchups.pop(0)
            badmatchups.insert(level, currentmatchup)
            badmatchupids.pop(0)
            badmatchupids.insert(level, i)
    #print(badmatchups)
    #print(badmatchupids)
    #for i in range(0, monstocheck):
        #print(usagestats[badmatchupids[i]][0], badmatchups[i])
    return badmatchupids

def getoverallworstmatchupsagainst(mons):
    matchupsummaries = []
    for i in range(0,57):
        currentmatchup = 0
        for j in range(len(mons)):
            currentmatchup = currentmatchup + matchupstats[mons[j]][i]
        matchupsummaries.append(currentmatchup)
    #Variable to toggle when needed
    monstocheck = 5
    badmatchups = []
    badmatchupids = []
    for i in range(monstocheck):
        badmatchups.append(10)
        badmatchupids.append(0)
    #print("Testing:")
    #for i in range(len(mons)):
        #print(usagestats[mons[i]][0])
    for i in range(0, 57):
        currentmatchup = matchupsummaries[i]
        level = -1
        for j in range(monstocheck):
            if currentmatchup <= badmatchups[j]:
                level += 1
            else:
                break
        if level >= 0:  
            badmatchups.pop(0)
            badmatchups.insert(level, currentmatchup)
            badmatchupids.pop(0)
            badmatchupids.insert(level, i)
    #print(badmatchups)
    #print(badmatchupids)
    matchuptotal = 0
    for i in range(0, monstocheck):
        #print(usagestats[badmatchupids[i]][0], badmatchups[i])
        matchuptotal += badmatchups[i]
    #print(matchuptotal)
    return [badmatchupids, matchuptotal]

def getworstteammatchups(mons, specialmon, monpos, pokemoves):
    matchupsummaries = []
    getbadmatchupids = getoverallworstmatchupsagainst(mons)[0]
    for i in range(len(getbadmatchupids)):
        currentmatchup = 0
        matchupmon = getbadmatchupids[i]
        for j in range(len(mons)):
            if j != monpos:
                currentmatchup = currentmatchup + matchupstats[mons[j]][matchupmon]
            else:
                matchupsum = getmatchups(specialmon, matchupmon, pokemoves)
                currentmatchup = currentmatchup + matchupsum
        matchupsummaries.append(currentmatchup)
    #Variable to toggle when needed
    monstocheck = 5
    badmatchups = []
    badmatchupids = []
    for i in range(monstocheck):
        badmatchups.append(10)
        badmatchupids.append(0)
    for i in range(len(getbadmatchupids)):
        currentmatchup = matchupsummaries[i]
        level = -1
        for j in range(monstocheck):
            if currentmatchup <= badmatchups[j]:
                level += 1
            else:
                break
        if level >= 0:  
            badmatchups.pop(0)
            badmatchups.insert(level, currentmatchup)
            badmatchupids.pop(0)
            badmatchupids.insert(level, getbadmatchupids[i])
    matchuptotal = 0
    for i in range(0, monstocheck):
        #print(usagestats[badmatchupids[i]][0], badmatchups[i])
        matchuptotal += badmatchups[i]
    #print(matchuptotal)
    return [badmatchupids, matchuptotal]

def getoverallworstteammatchups(mons):
    matchupsummaries = []
    for i in range(0,57):
        currentmatchup = 0
        for j in range(len(mons)):
            matchupsum = getmatchups(mons[j][0], i, mons[j][1])
            currentmatchup = currentmatchup + matchupsum
        #print(usagestats[i][0], currentmatchup)
        matchupsummaries.append(currentmatchup)
    #Variable to toggle when needed
    monstocheck = 20
    badmatchups = []
    badmatchupids = []
    for i in range(monstocheck):
        badmatchups.append(10)
        badmatchupids.append(0)
    print("Testing:")
    for i in range(len(mons)):
        print(mons[i][0])
        print(mons[i][1])
    for i in range(0, 57):
        currentmatchup = matchupsummaries[i]
        level = -1
        for j in range(monstocheck):
            if currentmatchup <= badmatchups[j]:
                level += 1
            else:
                break
        if level >= 0:  
            badmatchups.pop(0)
            badmatchups.insert(level, currentmatchup)
            badmatchupids.pop(0)
            badmatchupids.insert(level, i)
    #print(badmatchups)
    #print(badmatchupids)
    matchuptotal = 0
    for i in range(0, monstocheck):
        print(usagestats[badmatchupids[i]][0], badmatchups[i])
        matchuptotal += badmatchups[i]
    print(matchuptotal)
    return [badmatchupids, matchuptotal]

def getallmovespreads(targetmoves, noassaultvest = True):
    allmovespreads = []
    rawmovestats = []
    selectedmoves = []
    for i in range(len(targetmoves)):
        if getmove(targetmoves[i][0])[1] > 0:
            selectedmoves.append(targetmoves[i][0])
        else:
            if targetmoves[i][0] not in ["Protect", "Haze", "Follow_Me"] and noassaultvest:
                selectedmoves.append(targetmoves[i][0])
    if len(selectedmoves) < 4 and noassaultvest:
        counter = 0
        while len(selectedmoves) < 4:
            if targetmoves[counter][0] not in selectedmoves:
                selectedmoves.append(targetmoves[counter][0])
            counter += 1
    elif len(selectedmoves) < 4 and noassaultvest == False: 
        for i in range(len(selectedmoves)):
            selectedmoves[i] = [selectedmoves[i], 100]
        return [selectedmoves]
    movecount = len(selectedmoves)
    for i in range(movecount):
        for j in range(i + 1, movecount):
            for k in range(j + 1, movecount):
                for l in range(k + 1, movecount):
                    allmovespreads.append([[selectedmoves[i], 100], [selectedmoves[j], 100], [selectedmoves[k], 100], [selectedmoves[l], 100]])
    return allmovespreads

def formatfromshowdown(filetoread):
    teamtoformat = []
    montoformat = [0,[],[],0,0,0,0]
    movesettoformat = []
    with open(filetoread, encoding = "utf+8") as file:
        linecount = 0
        for line in file:
            if len(line) >= 5:
                formattedline = line.replace("\n", "")
                formattedline = formattedline.replace(" ", "_")
                formattedline = formattedline.replace("’", "'")
                if linecount == 0:
                    formattedline = formattedline.split("_@_")
                    montoformat[0] = formattedline[0]
                    montoformat[5] = formattedline[1]
                    linecount += 1
                elif linecount == 1:
                    montoformat[4] = formattedline.replace("Ability:_", "")
                    linecount += 1
                elif linecount == 2:
                    linecount += 1
                elif linecount == 3:
                    formattedline = formattedline.replace("Tera_Type:_", "")
                    linecount += 1
                elif linecount == 4:
                    formattedline = formattedline.replace("EVs:_", "")
                    formattedline = formattedline.replace("_HP", "")
                    formattedline = formattedline.replace("_Atk", "")
                    formattedline = formattedline.replace("_Def", "")
                    formattedline = formattedline.replace("_SpA", "")
                    formattedline = formattedline.replace("_SpD", "")
                    formattedline = formattedline.replace("_Spe", "")
                    formattedline = formattedline.split("_/_")
                    for i in range(len(formattedline)):
                        montoformat[2].append(int(formattedline[i]))
                    linecount += 1
                elif linecount == 5:
                    formattedline = formattedline.replace("_Nature", "")
                    montoformat[3] = getnaturefromid(getnaturefromname(formattedline))
                    montoformat[3] = [int(montoformat[3][0]), int(montoformat[3][1])]
                    linecount += 1
                elif linecount == 6:
                    formattedline = formattedline.replace("IVs:_", "")
                    formattedline = formattedline.replace("_HP", "")
                    formattedline = formattedline.replace("_Atk", "")
                    formattedline = formattedline.replace("_Def", "")
                    formattedline = formattedline.replace("_SpA", "")
                    formattedline = formattedline.replace("_SpD", "")
                    formattedline = formattedline.replace("_Spe", "")
                    formattedline = formattedline.split("_/_")
                    for i in range(len(formattedline)):
                        montoformat[1].append(int(formattedline[i]))
                    linecount += 1
                elif linecount > 6:
                    formattedline = formattedline.replace("-_", "")
                    movesettoformat.append([formattedline, 100])
                    linecount += 1
                    if linecount == 11:
                        teamtoformat.append([montoformat, movesettoformat])
                        linecount = 0
                        montoformat = [0,[],[],0,0,0,0]
                        movesettoformat = []
    return teamtoformat

def formattoshowdown(teamtoformat):
    with open(filetowrite, "a") as file:
        for i in range(len(teamtoformat)):
            montoformat = teamtoformat[i][0]
            file.write(montoformat[0] + " @ " + montoformat[5].replace("_", " "))
            file.write("\n")
            if montoformat[4] == "Commander":
                file.write("Ability: Storm Drain")
            else:
                file.write("Ability: " + montoformat[4].replace("_", " "))
            file.write("\n")
            file.write("Level: 50")
            file.write("\n")
            file.write("Tera Type: " + str(movesets[findpokemon(montoformat[0])][4][0][0]))
            file.write("\n")
            file.write("EVs: " + str(montoformat[2][0]) + " HP / " + str(montoformat[2][1]) + " Atk / " + str(montoformat[2][2]) + " Def / " + str(montoformat[2][3]) + " SpA / " + str(montoformat[2][4]) + " SpD / " + str(montoformat[2][5]) + " Spe")
            file.write("\n")
            file.write(getnamefromnature(montoformat[3][0], montoformat[3][1]) + " Nature")
            file.write("\n")
            file.write("IVs: " + str(montoformat[1][0]) + " HP / " + str(montoformat[1][1]) + " Atk / " + str(montoformat[1][2]) + " Def / " + str(montoformat[1][3]) + " SpA / " + str(montoformat[1][4]) + " SpD / " + str(montoformat[1][5]) + " Spe")
            file.write("\n")
            movestoformat = teamtoformat[i][1]
            for j in range(len(movestoformat)):
                currentmove = movestoformat[j][0]
                currentmove = currentmove.replace("_", " ")
                file.write("- " + currentmove)
                file.write("\n")
            file.write("\n")

            
with open("rawresultsd" + str(dsum1weight) + "d" + str(dsum2weight) + "x1.txt", "a") as file:
    for i in range(0, 1):
        filetoread = "testfile" + str(i) + ".txt"
        evalresults = getoverallworstteammatchups(formatfromshowdown(filetoread))
        file.write(str(evalresults[1]))
        with open("resultsd" + str(dsum1weight) + "d" + str(dsum2weight) + "x1.txt", "a") as otherfile:
            otherfile.write(str(evalresults[0]))





























        
