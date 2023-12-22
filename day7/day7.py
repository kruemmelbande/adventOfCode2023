with open("day7dataset.txt","r") as f:
    dataset=f.readlines()
dataset=[i.replace("\n","") for i in dataset]

def evalCard(card):
    sames={"x":0}
    for i in card:
        same=0
        for k in card:
            if i==k:
                same+=1
        if same!=1:
            sames[str(i)]=same
    samesarr= [sames[i] for i in sames]
    highest=max(samesarr)
    #print(card, sames)
    if highest == 5:
        return 6
    if highest == 4:
        return 5
    if 3 in samesarr and 2 in samesarr:
        return 4
    if highest == 3:
        return 3
    if len(samesarr)==3:
        return 2
    if highest == 2:
        return 1
    return 0

def compareCards(card1,card2):
    if evalCard(card1)<evalCard(card2):
        return False
    if evalCard(card1)>evalCard(card2):
        return True
    else:
        # i am sad
        card1=[i for i in card1]
        card2=[i for i in card2]
        special=["T","J","Q","K","A"]
        card1b=[0 for i in card1]
        card2b=[0 for i in card1]
        for num,i in enumerate(card1):
            if i in special:
                for a in enumerate(special):
                    if a[1] == i:
                        #print("converted", i, " to ",a[0]+10, " at position ", num)
                        card1b[num]=a[0]+10
                        
                        break
            else:
                card1b[num]=int(i)     

        #print(card1b)    
        for num,i in enumerate(card2):
            if i in special:
                for a in enumerate(special):
                    if a[1] == i:
                        #print("converted", i, " to ",a[0]+10, " at position ", num)
                        card2b[num]=a[0]+10
                        
                        break
            else:
                card2b[num]=int(i)   
                                 
        for a,b in zip(card1b,card2b):
            if a<b:
                #print(card1,"<",card2)
                return False
            if a>b:
                #print(card1,">",card2)
                return True
        print("You tried to compare a card with itself.... thats probably not right")
        
    
    
#print(evalCard(dataset[0].split()[0]))

for _ in range(len(dataset)):
    for i in range(len(dataset)-1):
        card1=dataset[i].split()
        card2=dataset[i+1].split()
        #print(card1,card2,evalCard(card1[0]),evalCard(card2[0]))
        if compareCards(card1[0],card2[0]):
            dataset[i],dataset[i+1]=dataset[i+1],dataset[i]
#print(dataset)

sm=0
for mult,i in enumerate(dataset):
    sm+=int(i.split()[1])*(mult+1)
print(sm)