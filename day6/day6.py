import math
with open("day6dataset.txt","r") as f:
    dataset=f.readlines()

times = list(map(int, dataset[0].split(":")[1].split()))
distances = list(map(int, dataset[1].split(":")[1].split()))

timeswon=[]
for time,distance in zip(times,distances):
    timesingame=0
    for timehelddown in range(1, time+1):
        gametime=timehelddown
        gametime+=math.ceil(distance/timehelddown)
        if gametime<=time:
            timesingame+=1
    timeswon.append(timesingame)

print(timeswon)  
result=1
for i in timeswon:
    result*=i
print(result)