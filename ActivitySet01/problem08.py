h=input("Enter the file name:")
try:
    f=open(h)
except:
    print(h,"Not Found")
count=0
s=0
for i in f:
    if i.startswith('X-DSPAM-Confidence:'):
        count=count+1
        x=i.find('0')
        l=i[x:]
        c=float(l)
        s=s+c
    else:
        continue
average=s/count
print('Average spam confidence:',average)
 