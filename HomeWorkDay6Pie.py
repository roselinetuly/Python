import pandas as pd
import pyodbc as db
import matplotlib.pyplot as plt
from matplotlib.patches import Patch

data_label = ['A','B','C', 'D', 'E']
# print(data)

colors = ['#ecff5a','#ffa500','#a52a2a','#81d8d0','#ff8600']
legend_element = [Patch(facecolor='#ecff5a', label='A'),
                  Patch(facecolor='#ffa500', label='B'),
                  Patch(facecolor='#a52a2a', label='C'),
                  Patch(facecolor='#81d8d0', label='D'),
                  Patch(facecolor='#ff8600', label='E')
                  ]

data = [300,400,700,200,150]
# print(data_label)
fig1, ax = plt.subplots()
pack_all, label, percent_value = ax.pie(data, labels=data_label, colors=colors, autopct='%.1f%%', startangle=90, pctdistance=.8)

plt.setp(percent_value, fontsize=14, color='blue', fontweight='bold')
plt.setp(label, fontsize=14, fontweight='bold')
plt.title('Assignment 6 - Tuly', fontsize=16, fontweight='bold', color='#3e0a75')
ax.axis('equal')
plt.legend(handles=legend_element, loc='lower left', fontsize=11)
plt.tight_layout()
plt.savefig('Assignment6_Tuly.png')
# plt.show()
