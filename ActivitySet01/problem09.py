fname = input("Enter file name: ")
a=[]
try:
    fname="romeo.txt"
except:
    print("Invalid File")
f=open(fname)
for lines in f:
    b=lines.split()
    for word in b:
        if word in a:
            continue
        else:
            a.append(word)
a.sort()
print(a)