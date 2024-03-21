s1= ['GFg', 'is', 'best', 'for', 'geeks',]
n=s1
for i in n:
    n=eval(input())
    print(n)

#problrm1

n= int(input())
integer=[]
float_value=[]
string=[]

for val in range(n):
    value= eval(input("enter the value:"))
    if type(value)==int:
        integer.append(value)
    elif type(value)==float:
        float_value.append(value)
    elif type(value)==str:
        string.append(value)

    else:
         print("pls provide data in int, float, string")

print(integer)
print(float_value)
