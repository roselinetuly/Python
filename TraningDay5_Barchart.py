import numpy as np
import matplotlib.pyplot as plt
#
#
# sales_person = ['Apple', 'Orange', 'Watermelon', 'Mango', 'Lichi', 'Grapes']
# sales = [10000, 8000, 9000, 4000, 5000, 20000]
# #
# total_bar = np.arange(len(sales_person))
# #
# color = ['red', 'green', 'yellow', 'blue', 'orange', 'black']
# plt.barh(total_bar, sales, align='center', alpha=.90, color=color) # alpha for bright
# plt.xticks(total_bar, sales_person)
# plt.ylabel('Amount')
# plt.title('Sales Performance')
# #
# plt.show()
# #
# # # ------------------------------------------------------------
#
# # sales_person = ['Kuddus', 'Rubel', 'Rony', 'Rocky', 'Abir', 'Noyon']
# # performance = [10000, 8000, 9000, 4000, 5000, 20000]
# #

# # total_bar = np.arange(len(sales_person))
# # color = ['red', 'green', 'yellow', 'blue', 'orange', 'pink']
# #
# # plt.barh(total_bar, performance, align='center', alpha=0.9, color=color)
# # plt.yticks(total_bar, sales_person)
# # plt.ylabel('Amount')
# # plt.title('Sales Performance')
# #
# # plt.show()
# # -------------------------------------------------------------------------------
def number_decorator(number):
    number = round(number, 1)
    number = format(number, ',')
    number = number + 'K'
    return number

def thousand_K_number_decorator(number):
    number = int(number / 1000)
    number = format(number, ',')
    number = number + 'K'
    return number


day1_sale = [9000, 5500, 4000, 6500]
day2_sale = [8500, 6200, 5400, 2000]
sales_person = ['Kuddus', 'Rubel', 'Rony', 'Rocky']
bar_index = np.arange(len(day2_sale))

# create plot
fig, ax = plt.subplots()

bar_width = 0.3
opacity = 0.9

bar1 = plt.bar(bar_index, day1_sale, bar_width,
               alpha=opacity, color='b', label='Frank')

bar2 = plt.bar(bar_index + bar_width, day2_sale, bar_width,
               alpha=opacity, color='r', label='Guido')


def autolabel(bar1):
    for bar in bar1:
        height = int(bar.get_height())
        ax.text(bar.get_x() + .1, 0.8 * height,
                number_decorator(height),
                va='bottom', rotation=90,
                fontsize=12, fontweight='bold')


def autolabel(bar2):
    for bar in bar2:
        height = int(bar.get_height())
        ax.text(bar.get_x() + .1, 0.8 * height,
                number_decorator(height),
                va='bottom', rotation=90,
                fontsize=12, fontweight='bold')


autolabel(bar1)
autolabel(bar2)

plt.ylabel('Amount')
plt.xlabel('Name')
plt.title('Assignment 5')
plt.xticks(bar_index + bar_width / 2, sales_person)
plt.legend(['day1', 'day2'])

plt.tight_layout()
plt.show()