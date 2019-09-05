import pandas as pd
import numpy as np
#import matplotlib as matlib

csvfile=pd.read_csv('/home/arvind/Desktop/Malu_learn_python/appl_1980_2014.csv')

#print (csvfile.columns)

#print (csvfile.head)

#convert datetime in order to use resample method

csvfile.Date=pd.to_datetime(csvfile.Date)

#print (csvfile.Date.head)

#set the date as index

csvfile=csvfile.set_index('Date')

#print (csvfile.head)

#allign as per date (in ascending order)

csvfile=csvfile.sort_index(ascending = True)

#print (csvfile.head)

#get the last business day of each month

csvfile_month=csvfile.resample('BM').mean()

print(csvfile_month.head)

#difference between first and last days..to calculate the total no. of days considered

csvfile_diff=(csvfile.index.max()-csvfile.index.min())

print(csvfile_diff)
