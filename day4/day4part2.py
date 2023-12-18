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
  #  print("Spawned card", card)
    global cardsUsed
    if card>len(games):
    #    print("Finished")
        return 0
    cardsUsed +=1
    score=total[card]
    if score==0:
       # print("finished")
        return 0
    for i in range(card+1,card+score+1):
        calculateTotalOfCard(i)
   # print("finish")

for i in range(len(total)):
    calculateTotalOfCard(i)
    print(f"Calculated {i} of {len(total)}", end = "\r")
print()
print(cardsUsed)