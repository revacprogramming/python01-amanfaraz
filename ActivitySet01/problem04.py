hr= int(input("Enter the no of hours"))
nph= float(input("Enter pay per hour"))
if hr<40:
    pay=hr*nph
else:
    s=hr-40
    pay=40*nph+s*1.5*nph
print(pay)
    