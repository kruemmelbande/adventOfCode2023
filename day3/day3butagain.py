numbers=[str(i) for i in range(0,10)]
print(numbers)

def isInbounds(x,y,arr):
    try:
        if x>=0 and y>=0:
            amongus=arr[x][y]
            return True
    except Exception:
        pass
    return False

def findNumber(x,y,arr):
    if not isInbounds(x,y,arr.copy()):
        print("Something has gone very wrong")
        return (0, arr.copy())
    if arr[x][y] not in numbers:
        print("this not a number bro ", arr[x][y])
        return (0, arr.copy())
    if arr[x][y] in numbers:
        print(arr[x][y], " is a number")
    while isInbounds(x,y,arr) and arr[x][y] in numbers:
        y-=1
    y+=1
    result=0
    while isInbounds(x,y,arr) and arr[x][y] in numbers:
        result=result*10
        result+=int(arr[x][y])
        y+=1
        arr[x]=arr[x][:y-1] + "." + arr[x][y:]
    print("Found a number ", result)
    return (result,arr.copy())
    
    
with open("day3dataset.txt","r") as f:
        dataset=f.readlines()
arr=[line.replace("\n","") for line in dataset]    
results=[]
for x in range(len(arr)):
    for y in range(len(arr[x])):
        if arr[x][y] not in ["\n","."," "] and arr[x][y] not in numbers:
            print(arr[x][y], "is a special character")
            for i in range(-1,2):
                for k in range(-1,2):
                    if isInbounds(x+i,y+i, arr):
                        result,arr=findNumber(x+i,y+k,arr.copy())
                        results.append(result)

print(results)
print(sum(results))
                        
            