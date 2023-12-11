numbers= ["0","1","2","3","4","5","6","7","8","9"]
with open("day3dataset.txt","r") as f:
    dataset=f.readlines()
   
         
def getNumber(line,chara,shadow):
    
    print("uwu, i exist")
    if shadow[line][chara] not in numbers:
        print(shadow[line][chara], "is very not a number")
        return (shadow.copy(),0)
    print("found a number!")
    curchar=chara
    while 1:
        if curchar>=0 and shadow[line][curchar] in numbers:
            curchar-=1
            continue
        break
    curchar+=1
    result=0
    while 1:
        if curchar<=len(shadow[0]) and shadow[line][curchar] in numbers:
            result*=10
            result+=int(shadow[line][curchar])
            shadow[line][curchar]='.'
            curchar+=1
            continue
        break
    print("found number" , result)
    
    return (shadow.copy(),result)
        
shadow=[]
for line in dataset.copy():
    newline=[]
    for char in line.replace("\n",""):
        newline.append(char)
    shadow.append(newline.copy())
resultnumbers=[]
ogshadow=shadow.copy()
for line in range(len(shadow)):
    for character in range(len(shadow[0])):
        #print("uwu", line, " ", character, end = " ")
        #print(shadow[line][character])
    
        if shadow[line][character] != "." and shadow[line][character] not in numbers:
            print(shadow[line][character])
            for i in range(-1,1):
                for k in range(-1,1):
                    if line+i <0 or line+i > len(shadow) or character+k < 0 or character + k > len(shadow[0]):
                        continue
                    currentnumber=-1
                    print("trying to parse",shadow[line+i][character+k] ," at ", line+i, " ", character+k)
                    shadow,currentnumber=getNumber(line+i, character+k, shadow)
                    if currentnumber==0:
                        print(shadow[line+1][character+k], "is not a number")
                    if currentnumber==-1:
                        print("something has gone terribly wrong")
                    resultnumbers.append(currentnumber)
print(dataset)
print("---------")
print("\n".join(shadow))
print("---------")
print(ogshadow)
print(resultnumbers)
print(sum(resultnumbers))