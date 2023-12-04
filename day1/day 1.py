with open("day1fixed.txt","r") as f:
    text=f.readlines()

calibration=[]
for line in text:
    currentline=[]
    for letter in line:
        try:
            currentline.append(int(letter))
        except:
            pass
    calibration.append(currentline[0]*10+currentline[-1])

print(calibration)
print(len(calibration))
print(sum(calibration))
        