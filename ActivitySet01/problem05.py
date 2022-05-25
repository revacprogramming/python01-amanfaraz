grade=float(input("Enter the grade between 0.0 and 1.0"))
if 0>grade>1:
    print("ERROR")
elif grade>=0.9:
    print("A")
elif grade>=0.8:
    print("B")
elif grade>=0.7:
    print("C")
elif grade>=0.6:
    print("D")
else:
  print("F")
    
