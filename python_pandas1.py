import pandas as pd

csvfile=pd.read_csv('/home/arvind/Desktop/Malu_learn_python/cars.csv')

#print(csvfile)

#print(csvfile.head())
#print(csvfile.columns)
#print(csvfile.Car)
#print(csvfile.Car + csvfile.MPG)
#print(csvfile.Cylinders)
'''
for i in len(csvfile.Cylinders):
	if((csvfile.Cylinders[i])==8):
		print("8 cylinder Engine",csvfile.Car)
'''
#elif((csvfile.Cylinders)==4)):
#	print("4 cylinder engine",csvfile.Car)
#print(csvfile.tail(5))
#print(csvfile.Cylinders[10] + csvfile.Cylinders[10] )
#print(csvfile.add(csvfile.Car[10],csvfile.Cylinders[10] ))
'''
a=csvfile.Cylinders
b=csvfile.Car
print(pd.concat(a,b))
'''

print(csvfile.shape)
#print(csvfile.row)
print(csvfile.columns)
print(pd.to_numeric(csvfile.Model,errors='coerce')+pd.to_numeric(csvfile.Weight,errors='coerce'))


#print(csvfile[csvfile.columns['Model']].sum(axis=1))
