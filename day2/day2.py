cubes={
    "green":13,
    "red":12,
    "blue":14
}

with open("day2dataset.txt","r") as f:
    data=f.readlines()
betterdata=[]
gamesum=0
for line in data:
    game=[]
    isValid=True
    for subgame in line.split(":")[1].split(";"):
        for subsubgame in subgame.split(","):
            if cubes[subsubgame.split()[1]]<int(subsubgame.split()[0]):
                isValid=False
    if isValid:
        gamesum += int(line.split(":")[0].split()[1])
        
print(gamesum)
