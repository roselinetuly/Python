import pandas as pd
import pyodbc as db
import matplotlib.pyplot as plt
from matplotlib.patches import Patch

# data_label = ['A','B']
# print(data)
def convert(number):
    number = int(number/1000)
    number = format(number, ',')
    number = number + 'K'
    return number
colors = ['#ecff5a','#ffa500','#a52a2a','#81d8d0','#ff8600']
legend_element = [Patch(facecolor='#ecff5a', label='A'),
                  Patch(facecolor='#ffa500', label='B')
                  # Patch(facecolor='#a52a2a', label='C'),
                  # Patch(facecolor='#81d8d0', label='D'),
                  # Patch(facecolor='#ff8600', label='E')
                  ]

data = [3000000,4000000]
# total=data[0]+data[1]
total=convert(sum(data))
total='Total \n'+total
cash_label=convert(data[0])
credit_label=convert(data[1])
data_label =[cash_label,credit_label]
print(data_label)
fig1, ax = plt.subplots()
pack_all, label, percent_value = ax.pie(data, labels=data_label, colors=colors, autopct='%.1f%%', startangle=90, pctdistance=.8)

plt.setp(percent_value, fontsize=14, color='blue', fontweight='bold')
ax.text(0,-.1,total,ha='center',fontsize=14,fontweight='bold')
plt.setp(label, fontsize=14, fontweight='bold')

center_circle=plt.Circle((0,0),0.50,fc='white')
fig1.gca().add_artist(center_circle)
plt.title('Assignment 6 - Tuly', fontsize=16, fontweight='bold', color='#3e0a75')
ax.axis('equal')
plt.legend(handles=legend_element, loc='lower left', fontsize=11)
plt.tight_layout()
# plt.savefig('Assignment6_Tuly.png')
plt.show()
