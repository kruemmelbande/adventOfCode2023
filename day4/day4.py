
with open("day4dataset.txt","r") as f:
    games=f.readlines()

total=0
for game in games:
    winning=game.split("|")[0].split(":")[1].split()
    actual=game.split("|")[1].split()
    points=0
    for number in actual:
        if number in winning:
            if points==0:
                points=1
            else:
                points=points*2
    total+=points
print(total)