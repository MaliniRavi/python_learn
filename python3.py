stringA='Malini'

print(stringA*2)

print(stringA[0:-1])

X=input("enter the number")


print("you have entered",(X))

mylist=[11,22,33,44,55]

mytuple1=(12,34,56)
mytuple2=(78,90)

mydict={
'A':'aaa@gmail.com',
'B':'bbb@gmail.com',
'C':'ccc@gmail.com'	
}
print("My list is",mylist)
while (len(mylist)>2):
   print("Length of my list is ",len(mylist))
   del(mylist[0])   
   print("Length of my list is ",len(mylist))
   print("My list is ",(mylist))

def printtuple():
  mytuple3=(00,mytuple1,mytuple2)
  print("My 3rd tuple",mytuple3)
  print(mytuple3[1][2])

printtuple()

print(mydict['A'])


