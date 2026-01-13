

i = 0
delline = False

#filetoread = "data/generatedteamsd5d5x5.txt"
#with open(filetoread, encoding="utf-8") as file:
    #monnumber = -1
    #for line in file:
        #if "@" in line:
            #monnumber += 1
        #if line == "Now Testing:\n":
            #monnumber = 0
            #delline = True
            #i += 1
        #elif delline == True:
            #delline = False
        #else:
            #filetowrite = "data/teamstotest/1/testfile" + str(i) + ".txt"
            #with open(filetowrite, "a", encoding="utf-8") as teamfile:
                #teamfile.write(line)

filetoread = "data/betterteams.txt"
with open(filetoread, encoding="utf-8") as file:
    monnumber = -1
    for line in file:
        if "@" in line:
            monnumber += 1
        if monnumber >= 6:
            monnumber = 0
            i += 1
        filetowrite = "data/teamstotest/1/testfile" + str(i) + ".txt"
        with open(filetowrite, "a", encoding="utf-8") as teamfile:
            teamfile.write(line)

i += 1

filetoread = "data/goodteams.txt"
with open(filetoread, encoding="utf-8") as file:
    monnumber = -1
    for line in file:
        if "@" in line:
            monnumber += 1
        if monnumber >= 6:
            monnumber = 0
            i += 1
        filetowrite = "data/teamstotest/2/testfile" + str(i) + ".txt"
        with open(filetowrite, "a", encoding="utf-8") as teamfile:
            teamfile.write(line)


















