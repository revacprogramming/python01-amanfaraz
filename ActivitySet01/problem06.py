largest=None
smallest=None
while True:
    a=input("Enter a Number")
    if a=="done":
        break
    try:
        a=int(a)
    except:
        print("Invalid input")
        continue
    if largest== None:
        largest=a
    elif largest<a:
        largest=a
    if smallest==None:
        smallest=a
    elif smallest>a:
        smallest=a
print("Maximum is",largest)
print("Minimum is",smallest)
        