####### Line chart ###################
import pandas as pd
import pyodbc as db
import numpy as np
import math
from matplotlib import pyplot as plt

# connection = db.connect('DRIVER={SQL Server};'
#                         'SERVER=10.168.2.241;'
#                         'DATABASE=ARCHIVESKF;'
#                         'UID=sa;PWD=erp')
#
# query = """select top 10  AUDTORG as [Branch Name],
# cast(sum(case when TRANSDATE='20200601' then EXTINVMISC else 0 END)/100000 as decimal(10,0))  as [Day 1 Sales],
# cast(sum(case when TRANSDATE='20200629' then EXTINVMISC else 0 END)/100000 as decimal(10,0))as [Day 2 Sales]
# from OESalesDetails where TRANSDATE in ('20200601','20200629') and audtorg in ('BOGSKF','MHKSKF','RNGSKF','FRDSKF','COMSKF')
# group by AUDTORG"""
# data = pd.read_sql_query(query, connection)
# data=pd.read_sql_query(query,connection)
# data.to_csv('SalesData_Roseline.csv',index=False)
data=pd.read_csv('D:/PYTHON/ProjectTraining/SalesData_Roseline.csv')
# # print(data.head(3))
df=pd.DataFrame(data)
df.head()
x = df['Branch Name'].tolist()
y = data['Day 1 Sales'].tolist()
z = data['Day 2 Sales'].tolist()
print(y)
print(z)
fig, ax = plt.subplots()
ax.plot(x, y, color='red', marker='o')
ax.plot(x, z, color='blue', marker='o')

ax.legend(labels=('Day 1 Sales', 'Day 2 Sales'), loc='upper center',bbox_to_anchor=(0.5,-0.3),fancybox=True,shadow=True,ncol=2)

plt.xlabel("Branch Name", color='black', fontsize=14, fontweight='bold', )
plt.ylabel("Amount", color='black', fontsize=14, fontweight='bold', )
# plt.xticks(x, rotation='vertical')
# plt.ylabel("Sales", color='black', fontsize=14, fontweight='bold')
plt.yticks(np.arange(0, max(z)*1.5, (max(z)*1.5)/10))
#
#
for a, b in zip(x, y):
    plt.text(a, b, str(b) + 'K', ha='center', va='bottom')

for a, b in zip(x, z):
    plt.text(a, b, str(b) + 'K', ha='center', va='bottom')
#
# print('complete')
plt.tight_layout()
# plt.savefig('task1.png')
plt.show()