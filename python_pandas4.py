#creating series and dataframe

import pandas as pd
import numpy as np

'''
a=pd.Series([11,22,33,44,np.nan])
print(a)

b=pd.DataFrame({'States':['Karnataka','TamilNadu','Andrapradesh','Kerala',],'Capital':['Bangalore','Chennai','Hyderabad','Cochin']})
print(b)

print(b.States[2])

for i in b.index:
	print("The Capital of",b.States[i],"is",b.Capital[i])


c=pd.DataFrame({'a':range(5),'b':range(4,9)})
print(c)
'''
'''
#isin
df1=pd.DataFrame({'As':['a','aa','aaa'],'Bs':['b','bb','bbb'],'Cs':['c','cc','ccc']})
df2=pd.DataFrame({'Bs':['b','bb','bbb'],'Ds':['d','dd','ddd'],'Es':['e','ee','eee']})
print(df1)
print(df2)
print(df1['Bs'].isin(df2['Es'])) 
print(df1['Bs'][2])
'''

#boolean indexing

df1=pd.DataFrame({'1s':[1,11,111,1111],'Bs':['b','bb','bbb'],'Cs':['c','cc','ccc']})
df2=pd.DataFrame({'Bs':['b','bb','bbb'],'Ds':['d','dd','ddd'],'Es':['e','ee','eee']})

print (df1)
print (df2)

