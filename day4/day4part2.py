import sys
sys.setrecursionlimit(999999999)
with open("day4dataset.txt","r") as f:
    games=f.readlines()
cardsUsed=0
total=[]
for game in games:
    winning=game.split("|")[0].split(":")[1].split()
    actual=game.split("|")[1].split()
    points=0
    for number in actual:
        if number in winning:
            points+=1
    total.append(points)
def calculateTotalOfCard(card):
    global cardsUsed
    if card>len(games):
        return 0
    score=total[card]
    if score==0:
        return 0
    for i in range(card,card+score):
        calculateTotalOfCard(i)

for i in range(len(total)):
    calculateTotalOfCard(i)
    print(f"Calculated {i} of {len(total)}", end = "\r")
print()
print(cardsUsed)