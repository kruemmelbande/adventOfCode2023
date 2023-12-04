with open("day2dataset.txt","r") as f:
    data=f.readlines()
betterdata=[]
gamesum=0
for line in data:
    game=[0,0,0]
    isValid=True
    for subgame in line.split(":")[1].split(";"):
        for subsubgame in subgame.split(","):
            if subsubgame.split()[1]=="red":
                game=[max(game[0],int(subsubgame.split()[0])),game[1],game[2]]
            if subsubgame.split()[1]=="green":
                game=[game[0],max(game[1],int(subsubgame.split()[0])),game[2]]
            if subsubgame.split()[1]=="blue":
                game=[game[0],game[1], max(game[2],int(subsubgame.split()[0]))]
    gamesum+=game[0]*game[1]*game[2]
print(gamesum)