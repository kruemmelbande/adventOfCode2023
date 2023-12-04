with open("day1dataset.txt","r") as f:
    text=f.read()
newtext=text.lower().replace("one","o1e").replace("two","t2o").replace("three","t3e").replace("four","f4r").replace("five","f5e").replace("six","s6x").replace("seven","s7n").replace("eight","e8t").replace("nine","n9n")
print(newtext)
with open("day1fixed.txt","w") as f:
    f.write(newtext)
