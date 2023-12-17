with open("day5dataset.txt","r") as f:
    dataset=[line.replace("\n","") for line in f.readlines()]

seeds=list(map(int, dataset[0].split()[1:]))
ogseeds=[int(seed) for seed in seeds]

print("done generating seeds")
print(seeds)
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
for i,seed in enumerate(seeds):
    for category in maps:
        for themap in category:
            #print(themap)
            destination, source, lerange=themap
            if seed >=source and seed <=source+lerange:
                print(seed, end="->")
                seeds[i]+=destination-source
                seed=seeds[i]
                print(seed)
                break

print("done mapping seeds")       
#print(seeds)
print(min(seeds))
for i in zip(seeds,ogseeds):
    if i[0]==min(seeds):
        print(i)

        