class Person:
  def __init__(self0,name,age,sex,a,b):
    self0.NAME=name
    self0.AGE=age
    self0.SEX=sex
    self0.AA=a
    self0.BB=b

  def myfunc(self1,job):
    self1.JOB=job
    print("These are my personal details",self1.NAME,self1.AGE,self1.SEX)

P1=Person('ROCKY',23,'MALE',11,22)
print (P1.NAME)
print (P1.AGE)
print (P1.SEX)

print(P1.AA)
print(P1.BB)

A=P1.AA
B=P1.BB
print(A+B)

P1.NAME='JOHNY'

P1.myfunc()

def myfunc1():
    print("These are my personal details",P1.NAME,P1.AGE,P1.SEX)

myfunc1()


'''Print(NAME,AGE,SEX)'''
