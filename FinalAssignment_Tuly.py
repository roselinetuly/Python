import matplotlib.patches as patches
import numpy as np
import pandas as pd
import pyodbc as db
from matplotlib.patches import Patch
import matplotlib.pyplot as plt


# ----------convert the number into thousand and give comma -------
def fmtthousand(number):
    number = number / 1000
    number = int(number)
    number = format(number, ',')
    number = number + 'K'
    return number


connection = db.connect('DRIVER={SQL Server};'
                        'SERVER=137.116.139.217;'
                        'DATABASE=ARCHIVESKF;'
                        'UID=sa;PWD=erp@123')

# df_query1 = pd.read_sql_query(""" select
#                 SUM(CASE WHEN TERMS='CASH' THEN OUT_NET END) AS CashOut,
#                 SUM(CASE WHEN TERMS not like '%CASH%' THEN OUT_NET END) AS CreditOut
#
#                 from  [ARCOUT].dbo.[CUST_OUT]
#                 where  [INVDATE] <= convert(varchar(8),GETDATE()-1,112)
#                                         """, connection)
#
# cash = int(df_query1['CashOut'])
# credit = int(df_query1['CreditOut'])
#
# data = [cash, credit]
# total = sum(data)
# total = 'Total \n' + fmtthousand(total)
# # print(data)
#
# colors = ['#63ff14', '#ff9c09']
# legend_element = [Patch(facecolor='#63ff14', label='Cash'),
#                   Patch(facecolor='#ff9c09', label='Credit')]
# fmtcash = fmtthousand(cash)
# fmtcredit = fmtthousand(credit)
# DataLabel = [fmtcash, fmtcredit]
#
# # ----Figure 1 - Figure--------------
# fig1, ax = plt.subplots()
# packall, labels, autopct = ax.pie(data, colors=colors, labels=DataLabel, autopct='%.1f%%', startangle=90,
#                                   pctdistance=.7)
# plt.setp(autopct, fontsize=14, color='white', fontweight='bold')
# plt.setp(labels, fontsize=14, fontweight='bold')
# ax.text(0, -.1, total, ha='center', fontsize=14, fontweight='bold', backgroundcolor='#FFFFFF')
# centre_circle = plt.Circle((0, 0), 0.50, fc='white')
#
# fig = plt.gcf()
#
# fig.gca().add_artist(centre_circle)
# plt.title('1. Total Outstanding (Cash,Credit)', fontsize=16, fontweight='bold', color='#3e0a75')
# ax.axis('equal')
# plt.legend(handles=legend_element, loc='lower left', fontsize=11)
# plt.tight_layout()
# plt.savefig('1Figure_TermwiseOutstanding.png')
# # print('1Figure_TermwiseOutstanding.png')
# # plt.close()
# # plt.show()
#
# # ----Figure 2 - Figure--------------
# df_query2 = pd.read_sql_query(""" select case when DayDiff>0 then 'Matured' else 'Non Matured' end as CreditType
# ,sum(OUT_NET) as Amount from (
# select INVNUMBER,INVDATE,CUSTOMER,TERMS,CustomerInformation.CREDIT_LIMIT_DAYS,
#                         (datediff([dd] , CONVERT (DATETIME , LTRIM(cust_out.INVDATE) , 102) , GETDATE())+1)-CREDIT_LIMIT_DAYS as DayDiff,
#                         OUT_NET from [ARCOUT].dbo.[CUST_OUT]
#                         join ARCHIVESKF.dbo.CustomerInformation
#                         on [CUST_OUT].CUSTOMER = CustomerInformation.IDCUST
#                         where  TERMS<>'Cash'
# ) as Credit
# group by case when DayDiff>0 then 'Matured' else 'Non Matured' end""", connection)
#
# mature = int(df_query2.Amount.iloc[0])
# nonmature = int(df_query2.Amount.iloc[1])
#
# data1 = [mature, nonmature]
# # total = sum(data)
# # total = 'Total \n' + fmtthousand(total)
# # print(data1)
#
# colors = ['#fd3612', '#f9d342']
# legend_element = [Patch(facecolor='#fd3612', label='Mature'),
#                   Patch(facecolor='#f9d342', label='Non-Mature')]
# fmtcash = fmtthousand(mature)
# fmtcredit = fmtthousand(nonmature)
# DataLabel = [fmtcash, fmtcredit]
# # print(DataLabel)
# fig1, ax = plt.subplots()
# packall, labels, autopct = ax.pie(data1, colors=colors, labels=DataLabel, autopct='%.1f%%', startangle=90,
#                                   pctdistance=.7)
# plt.setp(autopct, fontsize=14, color='white', fontweight='bold')
# plt.setp(labels, fontsize=14, fontweight='bold')
# # ax.text(0, -.1, total, ha='center', fontsize=14, fontweight='bold', backgroundcolor='#b2cab6')
# # centre_circle = plt.Circle((0, 0), 0.50, fc='white')
# #
# # fig = plt.gcf()
# #
# # fig.gca().add_artist(centre_circle)
# plt.title('2. Credit Outstanding (Matured,Non-matured)', fontsize=16, fontweight='bold', color='#3e0a75')
# ax.axis('equal')
# plt.legend(handles=legend_element, loc='lower left', fontsize=11)
# plt.tight_layout()
# plt.savefig('2Figure_CreditOutstanding.png')
# # print('1Figure_TermwiseOutstanding.png')
# # plt.close()
# # plt.show()
#
# # Figure - 3 Matured aging days
colors = ['#d51400', '#63ff14', '#1906e1', '#b056ef']
df_query3 = pd.read_sql_query("""
select case when DayDiff between 1 and 3 then '1-3 Days'
 when DayDiff between 4 and 10 then '4-10 Days'
 when DayDiff between 11 and 15 then '11-15 Days'
 when DayDiff >15 then '16+ Days' end as [Aging Days]
 ,sum(OUT_NET)/1000 as Amount

from (
select INVNUMBER,INVDATE,CUSTOMER,TERMS,CustomerInformation.CREDIT_LIMIT_DAYS,
                        (datediff([dd] , CONVERT (DATETIME , LTRIM(cust_out.INVDATE) , 102) , GETDATE())+1)-CREDIT_LIMIT_DAYS as DayDiff,
                        OUT_NET from [ARCOUT].dbo.[CUST_OUT]
                        join ARCHIVESKF.dbo.CustomerInformation
                        on [CUST_OUT].CUSTOMER = CustomerInformation.IDCUST
                        where  TERMS<>'Cash'  and (datediff([dd] , CONVERT (DATETIME , LTRIM(cust_out.INVDATE) , 102) , GETDATE())+1)-CREDIT_LIMIT_DAYS >0
) as Credit
Group by case when DayDiff between 1 and 3 then '1-3 Days'
 when DayDiff between 4 and 10 then '4-10 Days'
 when DayDiff between 11 and 15 then '11-15 Days'
 when DayDiff >15 then '16+ Days' end """, connection)
width = 0.75
AgingDays = df_query3['Aging Days']
y_pos = np.arange(len(AgingDays))
performance = df_query3['Amount']
tovalue = sum(performance)
maxVal = max(performance)
fig, ax = plt.subplots()
bars = plt.bar(y_pos, performance, width, align='center', alpha=1)

# bars[0].set_color('#d51400')
# bars[1].set_color('#63ff14')
# bars[2].set_color('#1906e1')
# bars[3].set_color('#b056ef')

bar_index = np.arange(len(performance))
fig, ax = plt.subplots(figsize=(6.4, 4.8))
bar_width = 0.6
opacity = 0.9

bar1 = plt.bar(bar_index, performance, bar_width,
               alpha=opacity, color=colors)


def autolabel(bar1):
    for bar in bar1:
        height = int(bar.get_height())
        ax.text(bar.get_x() + .23, height,
                fmtthousand(height),
                va='bottom',
                fontsize=15, fontweight='bold')


autolabel(bar1)
plt.xticks(y_pos, AgingDays, fontsize=12)
plt.yticks(np.arange(0, maxVal + (.6 * maxVal), maxVal / 5), fontsize=12)
plt.xlabel('Aging Days', color='black', fontsize=14, fontweight='bold')
# plt.yticks(np.arange(0, round(ran) + (.6 * round(ran))), fontsize='12')
plt.ylabel('Amount', color='black', fontsize=14, fontweight='bold')
plt.title('3.Matured aging days', color='#3e0a75', fontweight='bold', fontsize=16)
plt.tight_layout()
# plt.show()
plt.savefig('3Figure_Maturedagingdays.png')
# plt.close()
# print('6. Closed to mature Credit Generated')

# # Figure - 4 Top 10 Market wise Outstanding
colors = ['#eead0e', '#008b8b', '#ff7256', '#a374ab']
df_query4 = pd.read_sql_query("""
select top 10 rtrim(ci.MARKETNAME) as [MARKET NAME], sum(OUT_NET)/1000 as AMOUNT from [ARCOUT].dbo.[CUST_OUT]
                        join ARCHIVESKF.dbo.CustomerInformation ci
                        on [CUST_OUT].CUSTOMER = ci.IDCUST
						and [CUST_OUT].AUDTORG=ci.AUDTORG
                        where  TERMS<>'Cash'
group by rtrim(ci.MARKETNAME)
order by sum(OUT_NET) desc """, connection)
width = 0.75
Marketname = df_query4['MARKET NAME']
y_pos = np.arange(len(Marketname))
performance = df_query4['AMOUNT']
tovalue = sum(performance)
maxVal = max(performance)
fig, ax = plt.subplots()
bars = plt.bar(y_pos, performance, width, align='center', alpha=1)

# bars[0].set_color('#d51400')
# bars[1].set_color('#63ff14')
# bars[2].set_color('#1906e1')
# bars[3].set_color('#b056ef')

bar_index = np.arange(len(performance))
fig, ax = plt.subplots(figsize=(6.4, 4.8))
bar_width = 0.6
opacity = 0.9

bar2 = plt.bar(bar_index, performance, bar_width,
               alpha=opacity, color=colors)


def autolabel(bar2):
    for bar in bar2:
        height = int(bar.get_height())
        ax.text(bar.get_x() + .1, height,
                fmtthousand(height),
                va='bottom',
                fontsize=10, fontweight='bold')

autolabel(bar2)
plt.xticks(y_pos, Marketname, fontsize=12)
plt.yticks(np.arange(0, maxVal + (.6 * maxVal), maxVal / 5), fontsize=12)
plt.xlabel('Market Name', color='black', fontsize=14, fontweight='bold')
plt.xticks(y_pos, rotation='vertical')
# plt.yticks(np.arange(0, round(ran) + (.6 * round(ran))), fontsize='12')
plt.ylabel('Amount', color='black', fontsize=10, fontweight='bold')
plt.title('4. Top 10 Market', color='#3e0a75', fontweight='bold', fontsize=16)
plt.tight_layout()
# plt.show()
plt.savefig('4Figure_Top10Market.png')

# Figure - 5 Top 10 Customer Outstanding
df_query5 = pd.read_sql_query("""
select top 10 CUSTOMER,rtrim(cs.NAMECUST_ShortName) as [Customer Name], round(sum(OUT_NET)/1000,0) as AMOUNT from [ARCOUT].dbo.[CUST_OUT]
                        join ARCHIVESKF.dbo.CustomerInformation ci
                        on [CUST_OUT].CUSTOMER = ci.IDCUST
						and [CUST_OUT].AUDTORG=ci.AUDTORG
						join Customer_ShortName cs
						on ci.IDCUST=cs.IDCUST
						and ci.AUDTORG=cs.AUDTORG
                        where  TERMS<>'Cash' 
group by CUSTOMER,rtrim(cs.NAMECUST_ShortName) 
order by sum(OUT_NET) desc 
 """, connection)
x = df_query5['Customer Name'].tolist()
y = df_query5['AMOUNT'].tolist()
fig, ax = plt.subplots(figsize=(12, 6.4))
ax.plot(x, y, color='#A35C4C',label='Outstanding', marker='o',markerfacecolor="#4BEB0A", linewidth=2.9)
# ax.plot(x, z, color='blue', marker='o')
ax.legend(loc='best')
plt.xlabel("Customer Name", color='black', fontsize=14, fontweight='bold' )
plt.ylabel("Amount", color='black', fontsize=14, fontweight='bold', )
plt.xticks(x, rotation=45)
# plt.ylabel("Sales", color='black', fontsize=14, fontweight='bold')
plt.yticks(np.arange(0, 5000, 1000))
#
#
for a, b in zip(x, y):
    plt.text(a, b+155, str(b) + 'K', ha='center', va='bottom',rotation=70)
# plt.xticks(x, rotation='vertical')
plt.title('5. Top 10 Customer', color='#3e0a75', fontweight='bold', fontsize=16)
plt.tight_layout()
# plt.show()
plt.savefig('5Figure_TopCustomer.png')


