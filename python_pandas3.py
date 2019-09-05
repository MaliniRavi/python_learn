import pandas as pd

csvfile=pd.read_csv('/home/arvind/Desktop/Malu_learn_python/cars.csv')
#print(csvfile.shape)
csvlen=csvfile.index
#print(csvlen)
#print(csvfile.head(5))
#print(csvfile.Car[5])
#print(csvfile.MPG[0] + csvfile.Model[0])

a= (pd.to_numeric(csvfile.MPG,errors='coerce'))
#print (a)
#print (a.mean())
'''

for i in csvlen:

	if(csvfile.Origin[i]=='Europe'):
		print('The',i,'car is originated from Europe')
	else:
		print('The',i,' car is originated from US')
'''
#to append new column

new_column = pd.DataFrame({'new_column': [11,22,33,44,55,66,77,88,99,111,222,333,444,555,666,777,888,999,1111]})
csvfile = csvfile.merge(new_column, left_index = True, right_index = True)
#csvfile.to_csv('cars.csv')
#print(csvfile)
csvfile=csvfile.set_index("new_column")
print(csvfile.iloc[:5])
print(csvfile.loc[66:88,['Car','Weight','Model']])
print(csvfile.loc[111],'Car')
print(csvfile.iloc[3])
print(csvfile.Car)
print(csvfile['Cylinders'])
