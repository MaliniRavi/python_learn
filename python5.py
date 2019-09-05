
num=[]


for n in range(2000,3201):
   if n%7==0 and n%5!=0:
      #print("The number",num,"is divisible by 7 and not by 5")
      num.append(str(n))
   else:    
      #print("The number",num,"is not divisible by 7 but by 5")	

print(num)
