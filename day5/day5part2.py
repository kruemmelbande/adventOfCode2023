import json
with open("day5dataset.txt","r") as f:
    dataset=[line.replace("\n","") for line in f.readlines()]

seeds=list(map(int, dataset[0].split()[1:]))
ogseeds=[int(seed) for seed in seeds]
seeds=[]
ammount=0
for i in range(0,len(ogseeds),2):
    ammount+=ogseeds[i+1]
print(ammount)
results=[]
maps=[[]]
for i,line in enumerate(dataset):
    if i<3:
        continue
    if "map" in line:
        maps.append([])
    else:
        if line != "":
            curline= (list(map(int, line.split())))
            if len(curline)==3:
                maps[-1].append(curline)
            #print(curline)
print("done parsing map")
for amongus in range(100):
    print("iteration :",amongus)
        #print(i)
        #print(ogseeds[i])
        #print(ogseeds[i+1])
    seeds=[]
    for i in range(0,len(ogseeds),2):
        for k in range(ogseeds[i]+amongus,ogseeds[i]+ogseeds[i+1]-amongus,100):
            seeds.append(k)
        #print(k)
    leogseeds=[int(seed) for seed in seeds]
    print(f"done generating {len(seeds)} seeds")
    #print(seeds)

    for i,seed in enumerate(seeds):
        for category in maps:
            for themap in category:
                #print(themap)
                destination, source, lerange=themap
                if seed >=source and seed <=source+lerange:
                    #print(seed, end="->")
                    seeds[i]+=destination-source
                    seed=seeds[i]
                    #print(seed)
                    break

    print("done mapping seeds")       
    #print(seeds)
    bestseed=min(seeds)
    print(bestseed)
    
    try:
        with open("backup.json","r") as f:
            backup=json.load(f)["backup"]
    except:
        backup=[]
        print("No backup?")
    try:
        backup.append(bestseed)
        with open("backup.json","w") as f:
            json.dump({"backup":backup},f)   
    except Exception as E:
        print(f"unable to back up shit, ah well. Error: {E}")
        print(backup)
        print(bestseed)
    #results.append(bestseed)
        
print(results)
print(min(results))