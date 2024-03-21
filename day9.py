# write a code print the 8th fibanochi number
'''
c=0
for val in set1, set2: 
    c=c+1
    if c==1:
        for element in val:
            if element not in set2:
                set3.add(element)
    elif c==2:
        for element in val:
            if element not in set1:
'''
'''
num=8
n1=0
n2=1
for val in range(num):
    ans = n1+n2
    n1=n2
    n2=ans
print(ans)

'''

'''
class profile:
    def __init__(self):
        print("hello world")

obj=profile()
obj.__init__()

'''
'''
class profile:
    def __init__(self, id, name, age):
        print(id, name, age)

obj = profile(1, "sai", 21)
'''
'''
class c1:
    name="sid"
    place="cbe"

    def m1(self):
        print(self.name, self.place)

object = c1()
object.m1()
'''
'''
class c1:
    email = "venkatasai2143jen@gmail.com"
    def m1(self):
     name= "sai"
     place="mech"
     print(name, place)
     print(self.email)
object = c1()
object.m1()
'''
'''
class class1:
    def __init__(self):
        self.name="sai"
        self.99email="sid@gmail.com"

    def display(self):
        print(self.name, self.email)

c1=class1()
c1.display()

'''

'''
----> inheritance
the process of utilizing the methods and attributes of parent class through the object of child class called as inheritance.
'''
'''
class parent:
    name="name1"

    def display(self):
        print(self.name)

d=child()
d.display()

'''
'''
-------> multilevel heritance
'''

class voice:
    def sound(self):
        print("all the animals have their own voices")
class dog(voice):
    def dog_voice(self):
        print("bark")

class cat(voice):
    def cat_voice(self):
        print("meow")

class parrot(voice):
    def parrot_voice(self):
        print("speak")

all= parrot()
all.dog_voice()
all.cat_voice()
all.sound()
all.parrot_voice()

'''
-----> hybrid inheritance
'''

'''
------> polymorphysim











                
    
