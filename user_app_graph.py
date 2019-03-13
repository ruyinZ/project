# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 22:47:01 2019

@author: Administrator
"""

import pandas as pd
import numpy as np

data = pd.read_csv('dataframe_mapped.txt',sep = " " ,  header=None) 

# Create 2 dataframes to read and store app values.
dataframe1 = pd.DataFrame(columns = ['user','app','score'])
dataframe2 = pd.DataFrame(columns = ['user','app','score'])

# Let datafrme1 equals to the first 3 lines in data. 
dataframe1['user'] = data.ix[:,0]
dataframe1['app'] = data.ix[:,1]
dataframe1['score'] = data.ix[:,2]

# For the rest of lines in data, repeatly store 3 lines to dataframe2 and then concatenate dataframe1.
for i in range (2,596):
    dataframe2['user'] = data.ix[:,0]
    dataframe2['app'] = data.ix[:,i*2-1]
    dataframe2['score'] = data.ix[:,i*2]
    dataframe1 = pd.concat([dataframe1,dataframe2])
    print (i)

# Reset the index for dataframe1 to make it continuous
dataframe1.index = range(len(dataframe1))
 
# If app number equlals to NaN, then drop this row.
array = np.where(np.isnan(dataframe1['app']))[0]
array_list = array.tolist()
dataframe1.drop(index = array_list)

# Sort dataframe1 by user number
sorted_df1 = dataframe1.sort_values(by='user')
# reset the index for sorted_df1
sorted_df1.index = range(len(sorted_df1))