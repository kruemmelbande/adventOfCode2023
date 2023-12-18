import math
with open("day6dataset.txt","r") as f:
    dataset=f.readlines()

time = int(dataset[0].split(":")[1].replace("\n","").replace(" ",""))
distance = int(dataset[1].split(":")[1].replace("\n","").replace(" ",""))

timeswon=[]
timesingame=0
for timehelddown in range(1, time+1):
    gametime=timehelddown
    gametime+=math.ceil(distance/timehelddown)
    if gametime<=time:
        timesingame+=1
print(timesingame)