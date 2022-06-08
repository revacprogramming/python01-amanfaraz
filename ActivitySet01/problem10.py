fname=input("Enter the file name:")
count=0
try:
    f=open(fname)
except:
    print("Invalid File")
for lines in f:
    if lines.startswith("From") and "From:" not in lines:
        b=lines.split()
        print(b[1])
        count+=1
print("There were",count,"lines in the file with From as the first word")

    
    
     
        
    
    
    
     
        
    
        
    