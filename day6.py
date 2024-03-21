n= 128
temp = n
str1 = " "
f1=0
while n!=0:
    rem = n%10
    check = temp%rem
    if check==0:
        print("yes")
    else:
        print("no")
    n= n//10

if f1==0:
    print("yes")
else:
    print("no")


'''

chareterstics of set
1. set can be created using{}
2. the elements inside set are not indexed
3. does not allow duplicate values
4. its unordered
5. heterogenous
6. mutable or changable

'''

#eg;1

s1={9, 9, 89, 7.76, 8+7j, (8,9,5), "truck", "e"}
print(s1)


#eg:2

#s2 = {5, 8, 98, [9,0]}
#print(s2)

#eg:3
#s1 = {8, 78, 67, 'u'}
#add()
#s1.add(43)
#print(s1)

s1={8, 7, 78, 67, "u"}
s1.pop()
print(s1)


s1={4, 5, 6}


# get()
d1={1:100, 2:200, 3:300, 4:400}
print(d1[90])
print(d1.get(90))
s2={5, 6, 7, 8}
print(s1.intersection(s2))

print(s1.difference(s2))
print(s2.difference(s1))
print(s1.symmetric_difference(s2))

#isdisjoint(), issubset(), issuperset()
s1={8, 9, 0}
s2={6, 7, 8, 9, 0}
print(s1.issubset(s2))
print(s2.issubset(s1))

for val in s1:
    if val in s2:
        str1 = "its joint set"
print(str1)


#-----> dictionary
#eg:1
d1 = {1:100, 'a':200, 4.5:"hello"}
print(d1)
print(len(d1))




mech_name = ["name1", "name2", "name3"]
mech_age = [23,22,24]
mech_mark = [89, 78, 60]
mech_mail = ["name2@gmail.com","name3@gmail.com"]

mech        
    
