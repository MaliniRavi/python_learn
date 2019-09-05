class number():
  def __init__(num,num1,num2):
    num.NUM1=num1
    num.NUM2=num2

N1=number(11,22)

def sqr(x):
  print('The square of number',x, 'is ',x*x)

sqr(N1.NUM1)
sqr(N1.NUM2)

sqr(10)
A=N1.NUM1
B=N1.NUM2
#comment
if(N1.NUM1 < N1.NUM2):
  print("yes.It is lesser than other number")
else:
  print("No.It is greater than other number")

for i in range(15,B):
  print("A is less than B",i)
  
else:
  print("Loop os over")

