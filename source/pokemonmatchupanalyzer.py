import math, random
import numpy as np
import matplotlib
import matplotlib as mpl
import matplotlib.pyplot as plt

usagestats = []
movesets = []

# Format for Pokemon is [name, ivs, evs, natures, item, teratype]
# Format for items is [power, type, defcondition, heal, healcondition, effect]

with open("pokemonusages.txt") as usagelist:
    for usage in usagelist:
        if len(usage) > 6:
            usagesep = usage.replace("\n","")
            usagesep = usagesep.replace(" ","")
            usagestat = usagesep.split("|")
            usagestat[1] = float(usagestat[1])
            usagestats.append(usagestat)

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

def findpokemon(name):
    for i in range(0,57):
        if usagestats[i][0].lower() == name.lower():
            return i

#Insert File Name Here
filetoanalyze = "matchupdatad5d5x1.txt"
matchupstats = []

for i in range(0,57):
    matchupstats.append([])
    for j in range(0,57):
        matchupstats[i].append(0)

with open(filetoanalyze) as pokestats:
    for poke in pokestats:
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

p = 0
for i in range(0, 57):
    for j in range(0, 57):
        print(usagestats[i], usagestats[j], matchupstats[i][j] + matchupstats[j][i])
        p += 1
print(p)
print()
p = 0
for i in range(0, 57):
    for j in range(0, 57):
        if matchupstats[i][j] + matchupstats[j][i] > 0.01 or matchupstats[i][j] + matchupstats[j][i] < -0.01:
            print(usagestats[i], usagestats[j], matchupstats[i][j] + matchupstats[j][i])
            p += 1
print(p)

print()
p = 0
for i in range(0, 57):
    for j in range(0, 57):
        if matchupstats[i][j] + matchupstats[j][i] > 0.1 or matchupstats[i][j] + matchupstats[j][i] < -0.1:
            print(usagestats[i], usagestats[j], matchupstats[i][j] + matchupstats[j][i])
            p += 1

print(p)

print()
p = 0
for i in range(0, 57):
    for j in range(0, 57):
        if matchupstats[i][j] + matchupstats[j][i] > 0.1 or matchupstats[i][j] + matchupstats[j][i] < -0.1:
            if i != 32 and j != 32:
                print(usagestats[i], usagestats[j], matchupstats[i][j] + matchupstats[j][i])
                p += 1

print(p)
            

input()

#Data Manipulators
decreasespread = True

if decreasespread:
    for i in range(0,57):
        for j in range(0,57):
            if matchupstats[i][j] >= 0:
                matchupstats[i][j] = math.sqrt(matchupstats[i][j])
            else:
                matchupstats[i][j] = math.sqrt(matchupstats[i][j] * -1) * -1

def getmatchups(mon):
    print(matchupstats[mon])

def getworstmatchups(mon):
    monmatchups = matchupstats[mon]
    #Variable to toggle when needed
    monstocheck = 10
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
    monstocheck = 10
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
    print("Best Counters:")
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
    print(badmatchups)
    print(badmatchupids)
    for i in range(0, monstocheck):
        print(usagestats[badmatchupids[i]][0], badmatchups[i])
    return badmatchupids

def getoverallworstmatchupsagainst(mons):
    matchupsummaries = []
    for i in range(0,57):
        currentmatchup = 0
        for j in range(len(mons)):
            currentmatchup = currentmatchup + matchupstats[mons[j]][i]
        matchupsummaries.append(currentmatchup)
    #Variable to toggle when needed
    monstocheck = 10
    badmatchups = []
    badmatchupids = []
    for i in range(monstocheck):
        badmatchups.append(10)
        badmatchupids.append(0)
    print("Testing:")
    for i in range(len(mons)):
        print(usagestats[mons[i]][0])
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
    print(badmatchups)
    print(badmatchupids)
    matchuptotal = 0
    for i in range(0, monstocheck):
        print(usagestats[badmatchupids[i]][0], badmatchups[i])
        matchuptotal += badmatchups[i]
    print(matchuptotal)
    return [badmatchupids, matchuptotal]


#Pokemon To Test
testpoke = 0
battleteam = [testpoke]
worstmatchupids = getworstmatchups(testpoke)
totest = getoverallbestmatchupsagainst(worstmatchupids)
for i in range(5):
    for j in range(4, -1, -1):
        if totest[j] not in battleteam:
            battleteam.append(totest[j])
            break
    worstmatchupids = getoverallworstmatchupsagainst(battleteam)[0]
    totest = getoverallbestmatchupsagainst(worstmatchupids)

pokemonanalyzed = []
bestteam = []
for i in range(6):
    bestteam.append(battleteam[i])
    pokemonanalyzed.append(bestteam[i])


print(bestteam)
while True:
    print("")
    print("_____________________")
    print("")
    print("")
    extraone = testpoke
    for j in range(4, -1, -1):
        if totest[j] not in pokemonanalyzed:
            extraone = totest[j]
            break
    if extraone == testpoke:
        break
    teamslist = []
    oldteam = []
    for i in range(6):
        oldteam.append(bestteam[i])
    teamslist.append(oldteam)
    for i in range(1, 6):
        newteam = []
        for j in range(6):
            newteam.append(bestteam[j])
        newteam[i] = extraone
        teamslist.append(newteam)
    bestteamnumber = 0
    bestmatchupsum = getoverallworstmatchupsagainst(oldteam)
    monstocheck = bestmatchupsum[0]
    bestmatchupsum = bestmatchupsum[1]
    for i in range(1, 6):
        worstmatchupstats = getoverallworstmatchupsagainst(teamslist[i])
        if bestmatchupsum < worstmatchupstats[1]:
            bestteamnumber = i
            bestmatchupsum = worstmatchupstats[1]
            monstocheck = worstmatchupstats[0]
    bestteam = []
    for i in range(6):
        bestteam.append(teamslist[bestteamnumber][i])
    pokemonanalyzed.append(extraone)
    totest = getoverallbestmatchupsagainst(monstocheck)

    
    
print("Battle Team:")
for i in range(len(bestteam)):
    print(usagestats[bestteam[i]][0])

print("")
print("_____________________")
print("")
print("")
monstocheck = getoverallworstmatchupsagainst(bestteam)[0]
getoverallbestmatchupsagainst(monstocheck)
            
matchupstats = np.array(matchupstats)
fig, ax = plt.subplots()
im = ax.imshow(matchupstats, cmap="vanimo")
ax.set_ylabel('Attacking Pokemon ID')
ax.set_xlabel('Defending Pokemon ID')

ax.set_title("Matchup stats for file: " + filetoanalyze + " (Higher Values are Better)")
fig.tight_layout()
#plt.show()




















                
