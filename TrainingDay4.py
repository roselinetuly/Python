import pandas as pd
import pyodbc as db
from matplotlib import pyplot as plt
import numpy as np
import math  # needed for definition of pi

# ##create database connection
# connection=db.connect('DRIVER={SQL Server};'
#                       'SERVER=137.116.139.217;'
#                       'DATABASE=ARCHIVESKF;'
#                       'UID=sa;PWD=erp@123'
#                       )
# query="""Select top 1000 * from oesalesdetails"""
# data=pd.read_sql_query(query,connection)
#data.to_csv('sales_data.csv')
# # print(type(data))
# print ('Data Saved')
data=pd.read_csv('D:/PYTHON/ProjectTraining/sales_data.csv')
# print(data.head(3))

df=pd.DataFrame({'Yes':[1,1],'No':[1,2]})
# print(df)
# print(data.columns)
# print(data.shape)
# print(data.AUDTORG.unique())
# print(data['AUDTORG'])
# print(data.AUDTORG.iloc[100])
# rng=data.loc[(data.AUDTORG=='RNGSKF')]
# print(rng)
# x = ['A', 'B', 'C', 'D', 'E']
# y = [24, 40, 30, 50, 45]
#
# plt.plot(x,y,color='Red')
# plt.xlabel("Name")
# plt.ylabel("Marks")
# plt.title('Line chart')
# plt.title('Line chart')
# plt.show()

x = ['A', 'B', 'C', 'D', 'E']
y = [24, 40, 30, 50, 45]
z = [20, 45, 35, 40, 25]

fig, ax=plt.subplots()
line1=ax.plot(x,y,color='red')
line2=ax.plot(x,z,color='blue')

ax.legend(labels=('Math','English'),loc='best') # loc can be top left ,top right, bottom left etc.
plt.xlabel("Name",  color='black', fontsize=14, fontweight='bold')
plt.ylabel("Marks", color='black', fontsize=14, fontweight='bold')
plt.title('Line chart', fontweight='bold', color='#3e0a75',  fontsize=18)
# plt.plot(x,y,color='Red')
# plt.xlabel("Name")
# plt.ylabel("Marks")
# plt.title('Line chart')
# plt.title('Line chart')
# plt.show()
plt.tight_layout()
plt.savefig('linechart.png')