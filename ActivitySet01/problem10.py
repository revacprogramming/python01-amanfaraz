fname=input("Enter the file name:")
a=[]
count=0
f=open(fname)
try:
    f="mbox-short.txt"
except:
    print("Invalid File")
for lines in f:
    if lines.startswith("From"):
        b=lines.split()
        a.append(b[1])
        count+=1
    else:
        continue
for i in a:
    print(i)
print("There were",count,"lines in the file with From as the first word")

    
    
     
        
    