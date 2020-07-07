import matplotlib.pyplot as plt
import matplotlib.patches as patches

left, width = 0.0, .48
bottom, height = 0, 1
right = left + width
top = 1

fig = plt.figure(figsize=(12, 2))
ax = fig.add_axes([0, 0, 1, 1])  # Left, Bottom, Width, Height
# plt.show()

for item in [fig, ax]:
    item.patch.set_visible(False)
    fig.patch.set_visible(False)
    ax.axis('Off')

# # -------------------------------------
p = patches.Rectangle(
    (left, bottom), width, height,
    color='#e2f6a2'
)
ax.add_patch(p)
# plt.show()

kpi_label = 'Return'
retuen_p = '1.2%'
ax.text(.5 * (left + right), .55 * (bottom + top), kpi_label,
        ha='center', va='center',
        fontsize=24, color='black',
        transform=ax.transAxes)

ax.text(.5 * (left + right), .3 * (bottom + top), retuen_p,
        ha='center', va='center',
        fontsize=24, color='green',
        transform=ax.transAxes)
# ----------- Box 2--------------------------------------------
left, width = .50, .50
bottom, height = .0, 1
right = left + width
top = 1

# fig = plt.figure(figsize=(12, 2))
# ax = fig.add_axes([0, 0, 1, 1])  #Left, Bottom, Width, Height
# # plt.show()

# # -------------------------------------
p = patches.Rectangle(
    (left, bottom), width, height,
    color='#d7e8d7'
)
ax.add_patch(p)
# plt.show()

kpi_label2 = 'MTD'
MTD_P = '82%'
ax.text(.5 * (left + right), .55 * (bottom + top), kpi_label2,
        ha='center', va='center',
        fontsize=24, color='black',
        transform=ax.transAxes)

ax.text(.5 * (left + right), .3 * (bottom + top), MTD_P,
        ha='center', va='center',
        fontsize=24, color='green',
        transform=ax.transAxes)
plt.show()
# plt.savefig('Box.png')
