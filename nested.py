a=[]
n=int(input("Enter number of integer:"))
while a in range(1,n+1):
    b=int(input("Enter integer:"))
    a.append(b)
even=[]
odd=[]
for j in a:
    if(j%2==0):
        even.append(j)
    else:
        odd.append(j)
print("The even list",even)
print("The odd list",odd)