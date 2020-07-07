import pandas as pd
import pyodbc as db
import numpy as np
import math
from matplotlib import pyplot as plt

# connection = db.connect('DRIVER={SQL Server};'
#                         'SERVER=137.116.139.217;'
#                         'DATABASE=ARCHIVESKF;'
#                         'UID=sa;PWD=erp@123')
#
# query = """DECLARE @Thisday CHAR(8) = CONVERT(varchar(8), dateAdd(day,-1,getdate()), 112)
#             DECLARE @lastday CHAR(8) = CONVERT(varchar(8), dateAdd(DAY,-2,getdate()), 112)
#             DECLARE @thismonth CHAR(6) = CONVERT(varchar(6), dateAdd(MONTH,0,getdate()-30), 112)
#             select top 10 RSMTR as RSMTR,
#             SUM(case when TRANSDATE = @Thisday then EXTINVMISC END)  as YesterdaySales,
#             SUM(case when TRANSDATE = @lastday then EXTINVMISC END) as BeforeTwodaysSales,
#             SUM(case when transtype=2 and left(transdate,6) = @thismonth then EXTINVMISC*(-1) END) as ReturnVal
#             from OESalesDetails
#             group by RSMTR
#             order by  YesterdaySales desc,   BeforeTwodaysSales desc, ReturnVal DESC"""
# data = pd.read_sql_query(query, connection)
# data=pd.read_sql_query(query,connection)
# data.to_csv('Chart_Roseline.csv',index=False)
# print('Saved data')
data = pd.read_csv('D:/PYTHON/ProjectTraining/Chart_Roseline.csv')
# print(data.head(10))
df = pd.DataFrame(data)
# df.head()
RSMTR = df['RSMTR'].tolist()
YesterdaySales = data['YesterdaySales'].tolist()
ReturnVal = data['ReturnVal'].tolist()
color = ['red', 'green', 'yellow', 'blue', 'orange', 'pink']


def number_decorator(number):
    number = round(number / 1000)
    number = format(number, ',')
    number = number + 'K'
    return number


bar_index = np.arange(len(YesterdaySales))
fig, ax = plt.subplots(figsize=(12.6,6))
bar_width = 0.6
opacity = 0.9

bar1 = plt.bar(bar_index, YesterdaySales, bar_width,
               alpha=opacity, color=color)
def autolabel(bar1):
    for bar in bar1:
        height = int(bar.get_height())
        ax.text(bar.get_x() + .1, height,
                number_decorator(height),
                va='bottom',
                fontsize=8, fontweight='bold')

autolabel(bar1)


ax.plot(RSMTR, ReturnVal, color='red', marker='o')
ax.legend(labels=('Yesterday Sales', '30 Days Return'), loc='upper center', bbox_to_anchor=(0.5, -0.3), fancybox=True,
          shadow=True, ncol=2)



plt.ylabel('Sales Amount and Return')
plt.xlabel('RSMTR Name')
plt.title('Sales Evaluation')
plt.xticks(bar_index + bar_width, RSMTR)

for a, b in zip(RSMTR, ReturnVal):
    plt.text(a, b, number_decorator(b), ha='center', va='bottom')
plt.xticks(bar_index + bar_width / 2, RSMTR)
plt.title('Assignment 5 - Tuly')
# plt.legend(['Yesterday Sales', '30 Days Return'])
plt.tight_layout()
plt.show()
# print(x)
# print(y)
# print(z)
# fig, ax = plt.subplots()
# ax.plot(x, y, color='red', marker='o')
# ax.plot(x, z, color='blue', marker='o')
# ax.legend(labels=('Day 1 Sales', 'Day 2 Sales'), loc='upper right')
# plt.xlabel("Branch Name", color='black', fontsize=14, fontweight='bold', )
# plt.ylabel("Amount", color='black', fontsize=14, fontweight='bold', )
# # plt.xticks(x, rotation='vertical')
# # plt.ylabel("Sales", color='black', fontsize=14, fontweight='bold')
# plt.yticks(np.arange(0, 40, 5))
# #
# #
# for a, b in zip(x, y):
#     plt.text(a, b, str(b) + 'K', ha='center', va='bottom')
#
# for a, b in zip(x, z):
#     plt.text(a, b, str(b) + 'K', ha='center', va='bottom')
# #
# # print('complete')
# plt.tight_layout()
# plt.savefig('Assignment5_Tuly.png')
# plt.show()
