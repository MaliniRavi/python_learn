'''

def fact(x):
   if x==0:
      return 1
   return x*fact(x-1)

print fact(5)


#x=input("Enter the number to calculate the factorial")



a=[1,1,22,22,33,44,44,66,33,77,66]

print 	set(a)
'''

import numpy 
print('NUMPY: {}',format(numpy.__version__))
import scipy 
print('SCIPY: {}',format(scipy.__version__))
#import matplotlib 
#print('matplotlib: {}',format(matplotlib.__version__))
import pandas 
print('pandas: {}',format(pandas.__version__))
import sklearn 
print('sklearn: {}',format(sklearn.__version__))

'''
m=numpy.array([(1,2,3),(4,5,6)])
print(numpy.shape(m))
print(numpy.std(m))
print(m[0,2],m[0,1])
print(m*m)
'''
'''
print(matrix)
print("\n")
print(numpy.transpose(matrix))
print(numpy.dot(matrix,3))
#matrix_3=matrix*3
#print(matrix_3)
'''
