import random, time

randomslots = []
chosenslots = []
randomslotsimpt = []
chosenslotsimpt = []
usagestats = []
movesets = []
teamsets = []
naturestats = []

with open("internal_data/pokemonusages.txt") as usagelist:
    for usage in usagelist:
        if len(usage) > 6:
            usagesep = usage.replace("\n","")
            usagesep = usagesep.replace(" ","")
            usagestat = usagesep.split("|")
            usagestat[1] = float(usagestat[1])
            usagestats.append(usagestat)

with open("internal_data/pokemonnatures.txt") as naturelist:
    counter = 0
    for nature in naturelist:
        if len(nature) > 3:
            naturesep = nature.replace("\n","")
            naturestat = naturesep.split(" ")
            naturestat.append(counter)
            naturestats.append(naturestat)
            counter += 1
            
with open("internal_data/pokemonmovesets.txt") as movesetlist:
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

with open("internal_data/vgcteams.txt", encoding="utf-8") as teamslist:
    storedteam = []
    for team in teamslist:
        if len(team) > 1:
            if len(team) == 5:
                if storedteam != []:
                    teamsets.append(storedteam)
                    storedteam = []
            else:
                storedteam.append(team)

def findpokemon(name):
    for i in range(0,57):
        if usagestats[i][0].lower() == name.lower():
            return i

def getnaturefromname(naturename):
    for naturestat in naturestats:
        if naturestat[0].lower() == naturename.lower():
            return naturestat[3]
    return False

def getnamefromnature(natureplus, natureminus):
    return naturestats[(natureplus - 1) * 5 + natureminus - 1][0]

def getnaturefromid(natureid):
    return [naturestats[natureid][1],naturestats[natureid][2]]

for i in range(33):
    randomslotsimpt.append(i)
    
for i in range(160):
    randomslots.append(i + 33)
    
for i in range(7):
    chosennumber = random.randint(0, len(randomslotsimpt) - 1)
    chosenslotsimpt.append(randomslotsimpt[chosennumber])
    randomslotsimpt.pop(chosennumber)

for i in range(32):
    chosennumber = random.randint(0, len(randomslots) - 1)
    chosenslots.append(randomslots[chosennumber])
    randomslots.pop(chosennumber)

print(len(teamsets))

#Time To Start Sorting



for i in range(len(randomslots)):
    selectionorders = []
    for j in range(6):
        currentorder = [0,1,2,3,4,5]
        neworder = []
        for k in range(6):
            randomorder = random.randint(0, len(currentorder) - 1)
            neworder.append(currentorder[randomorder])
            currentorder.pop(randomorder)
        selectionorders.append(neworder)
    chosenteam = teamsets[randomslots[i]]
    teammons = []
    teampokes = []
    for j in range(len(chosenteam)):
        teamline = chosenteam[j]
        if "@" in teamline:
            currentmon = (teamline.split("@")[0]).replace(" ", "")
            teammons.append(currentmon)
            teampokes.append(findpokemon(currentmon))
    orderedteams = []
    for j in range(6):
        orderedteams.append([])
    for j in range(6):
        currentmon = teampokes[j]
        currentorder = selectionorders[j]
        currentspreads = movesets[currentmon][2]
        pokes = []
        for k in range(len(currentspreads)):
            poke = []
            poke.append(currentspreads[k][0][1:7])
            assignednature = getnaturefromid(getnaturefromname(currentspreads[k][0][0]))
            ivs = [31,31,31,31,31,31]
            minusnature = int(assignednature[1])
            if poke[0][1] == 0 and minusnature == 1:
                ivs[1] = 0
            if poke[0][5] == 0 and minusnature == 5:
                ivs[5] = 0
            poke.append(currentspreads[k][0][0])
            poke.append(ivs)
            pokes.append(poke)
        orderedpokes = []
        if len(pokes) < 6:
            for k in range(6):
                if currentorder[k] >= len(pokes):
                    currentorder[k] = currentorder[k] - len(pokes)
        for k in range(6):
            orderedpokes.append(pokes[currentorder[k]])
        for k in range(6):
            orderedteams[k].append(orderedpokes[k])
    for j in range(6):
        focusteam = orderedteams[j]
        monnumber = -1
        filetowrite = "data/teams/regh/goodteams/testfile" + str(i) + str(j) + ".txt"
        with open(filetowrite, "a", encoding="utf-8") as file:
            for k in range(len(chosenteam)):
                teamline = chosenteam[k]
                if "@" in teamline:
                    monnumber += 1
                    file.write("\n")
                if "Tera Type" in teamline:
                    file.write(teamline)  
                    montoformat = focusteam[monnumber]
                    file.write("EVs: " + str(montoformat[0][0]) + " HP / " + str(montoformat[0][1]) + " Atk / " + str(montoformat[0][2]) + " Def / " + str(montoformat[0][3]) + " SpA / " + str(montoformat[0][4]) + " SpD / " + str(montoformat[0][5]) + " Spe")
                    file.write("\n")
                    file.write(montoformat[1])
                    file.write(" Nature")
                    file.write("\n")
                    file.write("IVs: " + str(montoformat[2][0]) + " HP / " + str(montoformat[2][1]) + " Atk / " + str(montoformat[2][2]) + " Def / " + str(montoformat[2][3]) + " SpA / " + str(montoformat[2][4]) + " SpD / " + str(montoformat[2][5]) + " Spe")
                    file.write("\n")
                else:
                    file.write(teamline)
                


for i in range(len(randomslotsimpt)):
    selectionorders = []
    for j in range(6):
        currentorder = [0,1,2,3,4,5]
        neworder = []
        for k in range(6):
            randomorder = random.randint(0, len(currentorder) - 1)
            neworder.append(currentorder[randomorder])
            currentorder.pop(randomorder)
        selectionorders.append(neworder)
    
    chosenteam = teamsets[randomslotsimpt[i]]
    teammons = []
    teampokes = []
    for j in range(len(chosenteam)):
        teamline = chosenteam[j]
        if "@" in teamline:
            currentmon = (teamline.split("@")[0]).replace(" ", "")
            teammons.append(currentmon)
            teampokes.append(findpokemon(currentmon))
    orderedteams = []
    for j in range(6):
        orderedteams.append([])
    for j in range(6):
        currentmon = teampokes[j]
        currentorder = selectionorders[j]
        currentspreads = movesets[currentmon][2]
        pokes = []
        for k in range(len(currentspreads)):
            poke = []
            poke.append(currentspreads[k][0][1:7])
            assignednature = getnaturefromid(getnaturefromname(currentspreads[k][0][0]))
            ivs = [31,31,31,31,31,31]
            minusnature = int(assignednature[1])
            if poke[0][1] == 0 and minusnature == 1:
                ivs[1] = 0
            if poke[0][5] == 0 and minusnature == 5:
                ivs[5] = 0
            poke.append(currentspreads[k][0][0])
            poke.append(ivs)
            pokes.append(poke)
        orderedpokes = []
        if len(pokes) < 6:
            for k in range(6):
                if currentorder[k] >= len(pokes):
                    currentorder[k] = currentorder[k] - len(pokes)
        for k in range(6):
            orderedpokes.append(pokes[currentorder[k]])
        for k in range(6):
            orderedteams[k].append(orderedpokes[k])
    for j in range(6):
        focusteam = orderedteams[j]
        monnumber = -1
        filetowrite = "data/teams/regh/betterteams/testfile" + str(i) + str(j) + ".txt"
        with open(filetowrite, "a", encoding="utf-8") as file:
            for k in range(len(chosenteam)):
                teamline = chosenteam[k]
                if "@" in teamline:
                    monnumber += 1
                    file.write("\n")
                if "Tera Type" in teamline:
                    file.write(teamline)  
                    montoformat = focusteam[monnumber]
                    file.write("EVs: " + str(montoformat[0][0]) + " HP / " + str(montoformat[0][1]) + " Atk / " + str(montoformat[0][2]) + " Def / " + str(montoformat[0][3]) + " SpA / " + str(montoformat[0][4]) + " SpD / " + str(montoformat[0][5]) + " Spe")
                    file.write("\n")
                    file.write(montoformat[1])
                    file.write(" Nature")
                    file.write("\n")
                    file.write("IVs: " + str(montoformat[2][0]) + " HP / " + str(montoformat[2][1]) + " Atk / " + str(montoformat[2][2]) + " Def / " + str(montoformat[2][3]) + " SpA / " + str(montoformat[2][4]) + " SpD / " + str(montoformat[2][5]) + " Spe")
                    file.write("\n")
                else:
                    file.write(teamline)


for i in range(len(chosenslots)):
    selectionorders = []
    for j in range(6):
        currentorder = [0,1,2,3,4,5]
        neworder = []
        for k in range(6):
            randomorder = random.randint(0, len(currentorder) - 1)
            neworder.append(currentorder[randomorder])
            currentorder.pop(randomorder)
        selectionorders.append(neworder)
    
    chosenteam = teamsets[chosenslots[i]]
    teammons = []
    teampokes = []
    for j in range(len(chosenteam)):
        teamline = chosenteam[j]
        if "@" in teamline:
            currentmon = (teamline.split("@")[0]).replace(" ", "")
            teammons.append(currentmon)
            teampokes.append(findpokemon(currentmon))
    orderedteams = []
    for j in range(6):
        orderedteams.append([])
    for j in range(6):
        currentmon = teampokes[j]
        currentorder = selectionorders[j]
        currentspreads = movesets[currentmon][2]
        pokes = []
        for k in range(len(currentspreads)):
            poke = []
            poke.append(currentspreads[k][0][1:7])
            assignednature = getnaturefromid(getnaturefromname(currentspreads[k][0][0]))
            ivs = [31,31,31,31,31,31]
            minusnature = int(assignednature[1])
            if poke[0][1] == 0 and minusnature == 1:
                ivs[1] = 0
            if poke[0][5] == 0 and minusnature == 5:
                ivs[5] = 0
            poke.append(currentspreads[k][0][0])
            poke.append(ivs)
            pokes.append(poke)
        orderedpokes = []
        if len(pokes) < 6:
            for k in range(6):
                if currentorder[k] >= len(pokes):
                    currentorder[k] = currentorder[k] - len(pokes)
        for k in range(6):
            orderedpokes.append(pokes[currentorder[k]])
        for k in range(6):
            orderedteams[k].append(orderedpokes[k])
    for j in range(6):
        focusteam = orderedteams[j]
        monnumber = -1
        filetowrite = "data/goodteams.txt"
        with open(filetowrite, "a", encoding="utf-8") as file:
            for k in range(len(chosenteam)):
                teamline = chosenteam[k]
                if "@" in teamline:
                    monnumber += 1
                    file.write("\n")
                if "Tera Type" in teamline:
                    file.write(teamline)  
                    montoformat = focusteam[monnumber]
                    file.write("EVs: " + str(montoformat[0][0]) + " HP / " + str(montoformat[0][1]) + " Atk / " + str(montoformat[0][2]) + " Def / " + str(montoformat[0][3]) + " SpA / " + str(montoformat[0][4]) + " SpD / " + str(montoformat[0][5]) + " Spe")
                    file.write("\n")
                    file.write(montoformat[1])
                    file.write(" Nature")
                    file.write("\n")
                    file.write("IVs: " + str(montoformat[2][0]) + " HP / " + str(montoformat[2][1]) + " Atk / " + str(montoformat[2][2]) + " Def / " + str(montoformat[2][3]) + " SpA / " + str(montoformat[2][4]) + " SpD / " + str(montoformat[2][5]) + " Spe")
                    file.write("\n")
                else:
                    file.write(teamline)


for i in range(len(chosenslotsimpt)):
    selectionorders = []
    for j in range(6):
        currentorder = [0,1,2,3,4,5]
        neworder = []
        for k in range(6):
            randomorder = random.randint(0, len(currentorder) - 1)
            neworder.append(currentorder[randomorder])
            currentorder.pop(randomorder)
        selectionorders.append(neworder)
    
    chosenteam = teamsets[chosenslotsimpt[i]]
    teammons = []
    teampokes = []
    for j in range(len(chosenteam)):
        teamline = chosenteam[j]
        if "@" in teamline:
            currentmon = (teamline.split("@")[0]).replace(" ", "")
            teammons.append(currentmon)
            teampokes.append(findpokemon(currentmon))
    orderedteams = []
    for j in range(6):
        orderedteams.append([])
    for j in range(6):
        currentmon = teampokes[j]
        currentorder = selectionorders[j]
        currentspreads = movesets[currentmon][2]
        pokes = []
        for k in range(len(currentspreads)):
            poke = []
            poke.append(currentspreads[k][0][1:7])
            assignednature = getnaturefromid(getnaturefromname(currentspreads[k][0][0]))
            ivs = [31,31,31,31,31,31]
            minusnature = int(assignednature[1])
            if poke[0][1] == 0 and minusnature == 1:
                ivs[1] = 0
            if poke[0][5] == 0 and minusnature == 5:
                ivs[5] = 0
            poke.append(currentspreads[k][0][0])
            poke.append(ivs)
            pokes.append(poke)
        orderedpokes = []
        if len(pokes) < 6:
            for k in range(6):
                if currentorder[k] >= len(pokes):
                    currentorder[k] = currentorder[k] - len(pokes)
        for k in range(6):
            orderedpokes.append(pokes[currentorder[k]])
        for k in range(6):
            orderedteams[k].append(orderedpokes[k])
    for j in range(6):
        focusteam = orderedteams[j]
        monnumber = -1
        filetowrite = "data/betterteams.txt"
        with open(filetowrite, "a", encoding="utf-8") as file:
            for k in range(len(chosenteam)):
                teamline = chosenteam[k]
                if "@" in teamline:
                    monnumber += 1
                    file.write("\n")
                if "Tera Type" in teamline:
                    file.write(teamline)  
                    montoformat = focusteam[monnumber]
                    file.write("EVs: " + str(montoformat[0][0]) + " HP / " + str(montoformat[0][1]) + " Atk / " + str(montoformat[0][2]) + " Def / " + str(montoformat[0][3]) + " SpA / " + str(montoformat[0][4]) + " SpD / " + str(montoformat[0][5]) + " Spe")
                    file.write("\n")
                    file.write(montoformat[1])
                    file.write(" Nature")
                    file.write("\n")
                    file.write("IVs: " + str(montoformat[2][0]) + " HP / " + str(montoformat[2][1]) + " Atk / " + str(montoformat[2][2]) + " Def / " + str(montoformat[2][3]) + " SpA / " + str(montoformat[2][4]) + " SpD / " + str(montoformat[2][5]) + " Spe")
                    file.write("\n")
                else:
                    file.write(teamline)
















