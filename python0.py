# Hello World program in Python
'''    
print "Hello World!\n"

#FActorial
def fact(x):
    if x==0:
        return 1
    else:
        return x*fact(x-1)
        
num=fact(0)
print("The factorial is",num)
'''    
   
#fibonocci series:Using generator method:yield,next and iter
'''
def fib(x):
    #initial 2 series
    a,b=0,1
    
    while(a<x):
        yield a
        a,b=b,a+b#discuss with arvind..below step gives different output
        
        #a=b
        #b=a+b
        
out=fib(5)

#print("The fibonocci series using next method")
#print(out.next())
#print(out.next())
#print(out.next())
#print(out.next())
#print(out.next())


for i in fib(5):
    print("The fibonocci series with for and next method",out.next())

for i in fib(5):
    print("The fibonocci series is with for loop",i)
    
'''  
#list comprehension
'''
x=[i for i in range(10)]
print ("List comprehension",x)


my_list=[]
print("Appending List using for loop",)
for i in range(1,10,2):
    my_list.append(i)
print(my_list)
    
    
print("Computinglist in simgle line",list(range(1,10,3)))
'''

#combining 2 lists
'''
num=[1,2,3,4,5]
letters=['A','B','C','D','E']
num_letters=[[n,l] for n in num for l in letters]
print ("The result of (n,l) is ",num_letters)
'''

string="python is very interesting"
'''
print(string.upper())
print(string.lower())
print(len(string))
for i in string:
    print(i)
#out=[i for i in string if i!=""]
out=[x for x in string if x!=""]
print(out)
'''
#dict comprehension
'''
dict_comp={x : x+10 for x in range(10)}
print(dict_comp)
sample=['a','b','c','d','e']
dict_comp={i : i+'s' for i in sample }
print(dict_comp)
'''

#Generator expression for list
'''
my_list=[x for x in range(0,15,2) if x%2==0]
print(my_list)


def my_func(*args):
    #result=x+y+z
    print("the addition of generator expressions are",args)
    
my_func(*my_list)
'''

#Generator expression for dict------NOT WORKING
'''
my_dict={x:x+5 for x in range(10)}
print(my_dict)

def my_func(**kwargs):
    print("Generated DICT is",kwargs)
    
my_func(**my_dict)
    
'''

#using iter and next function
'''
li=[x for x in range(5)]
print(li)

print(iter(li))
for i in iter(li):
    print(i)

my_iter=iter(li)


print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))

for i in my_iter:
    print(next(my_iter))
'''
#yield generator
'''
def my_func():
    yield (1)
    yield (2)
    yield (3)
    yield (4)
    
#x=my_func()
for i in my_func():
    print(i)

'''
# String operations

'''
my_str="PYTHON"
a=[i for i in my_str if i!='']
print(a)

for x,y in enumerate(my_str):
    print x,y

#creating a dict from str
b={c:d for c,d in enumerate(my_str)}
print b



def reverse(text):
    return text[::-1]


print (reverse("BOOK"))

'''
#encode and decode


#list operations


#Dict operations


#tuple operations
'''
my_tuple=(1,2,3)
print(my_tuple)
a=(i for i in range(5))
print tuple(a)
'''

#set operations


#OOPs concept

'''

class my_class():
    
    def __init__(self,a,b,c):
        self.aa=a
        self.bb=b
        self.cc=c
        if(a>1):
            print("a>1")
        
    
    def addition(self,x,y,z):
        return (z+x+y+self.aa)
        #return (z)
        
obj=my_class(2,4,6)
print(obj.aa)
print(obj.bb)
print(obj.cc)

add=obj.addition(1,2,3)
li=[i for i in range(3)]
print(li)
print(obj.addition(*li))
print(add)

'''

#inheritance

'''
class parent():
    
    def __init__(self,mom,dad):
        self.mommy=mom
        self.daddy=dad
        
    def parentclass(self,mom_age,dad_age):
        print("The age of",self.mommy,"is",mom_age)
        print("The age of",self.daddy,"is",dad_age)
        
        
p=parent("Malu","Arvi")
        
class son(parent):
    
    def __init__(self,mom,dad,son):
        parent.__init__(self,mom,dad)
        self.son_name=son
        
    
    def sonclass(self,son_age):
        print("The age of",self.son_name,"is",son_age)
        print(self.son_name,"is the son of",p.mommy,"and",p.daddy)
        


s=son("Malini","Arvind","Abinav")

p.parentclass(30,35)
s.sonclass(3)

'''
#encapsulation

'''
class my_class():
    
    __var=0#hidden variable
    
    def __init__(self):
        self.__var=20
        print(self.__var)
        
    def usevar(self):
        print(self.__var+5)
        
    def __chgvar(self):
        self.__var=30
        print(self.__var)
        
m=my_class()
m.usevar()

#m.__chgvar(self)#hideen function
m._my_class__chgvar()#alternate way to acess hidden function

'''
#polymorphism

#

#import pandas as pd

#pandas



#numpy


#find max value from the list


li=[2,1,4,9,5,7]

def maxvalue(nums):
    maxval=0
    for i in nums:
        if i>maxval:
            maxval=i
    print("The max value from the list is",maxval)  
    
maxvalue(li)
