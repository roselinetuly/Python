import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image
#------------Pic 1
left, width = 0.0, .19
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
    color='#ffd700'
)
ax.add_patch(p)
# plt.show()

kpi_label = 'MHK'
retuen_p = '125K'
ax.text(.5 * (left + right), .55 * (bottom + top), kpi_label,
        ha='center', va='center',
        fontsize=24, color='black',
        transform=ax.transAxes)

ax.text(.5 * (left + right), .3 * (bottom + top), retuen_p,
        ha='center', va='center',
        fontsize=24, color='green',
        transform=ax.transAxes)
# ----------- Box 2--------------------------------------------

#-----------Pic2
left, width = .20, .19
bottom, height = .0, 1
right = left + width
top = 1

# fig = plt.figure(figsize=(12, 2))
# ax = fig.add_axes([0, 0, 1, 1])  #Left, Bottom, Width, Height
# # plt.show()

# # -------------------------------------
p = patches.Rectangle(
    (left, bottom), width, height,
    color='#4b0082'
)
ax.add_patch(p)
# plt.show()

kpi_label2 = 'FRD'
MTD_P = '80K'
ax.text(.5 * (left + right), .55 * (bottom + top), kpi_label2,
        ha='center', va='center',
        fontsize=24, color='black',
        transform=ax.transAxes)

ax.text(.5 * (left + right), .3 * (bottom + top), MTD_P,
        ha='center', va='center',
        fontsize=24, color='green',
        transform=ax.transAxes)

#--------- Pic3
left, width = .40, .19
bottom, height = .0, 1
right = left + width
top = 1

# fig = plt.figure(figsize=(12, 2))
# ax = fig.add_axes([0, 0, 1, 1])  #Left, Bottom, Width, Height
# # plt.show()

# # -------------------------------------
p = patches.Rectangle(
    (left, bottom), width, height,
    color='#ffa500'
)
ax.add_patch(p)
# plt.show()

kpi_label3 = 'RNG'
MTD_P1 = '240K'
ax.text(.5 * (left + right), .55 * (bottom + top), kpi_label3,
        ha='center', va='center',
        fontsize=24, color='black',
        transform=ax.transAxes)

ax.text(.5 * (left + right), .3 * (bottom + top), MTD_P1,
        ha='center', va='center',
        fontsize=24, color='green',
        transform=ax.transAxes)
#----------------Pic4
left, width = .60, .19
bottom, height = .0, 1
right = left + width
top = 1

# fig = plt.figure(figsize=(12, 2))
# ax = fig.add_axes([0, 0, 1, 1])  #Left, Bottom, Width, Height
# # plt.show()

# # -------------------------------------
p = patches.Rectangle(
    (left, bottom), width, height,
    color='#514d5b'
)
ax.add_patch(p)
# plt.show()

kpi_label3 = 'MOT'
MTD_P1 = '240K'
ax.text(.5 * (left + right), .55 * (bottom + top), kpi_label3,
        ha='center', va='center',
        fontsize=24, color='black',
        transform=ax.transAxes)

ax.text(.5 * (left + right), .3 * (bottom + top), MTD_P1,
        ha='center', va='center',
        fontsize=24, color='green',
        transform=ax.transAxes)


#--------------- Pic5
left, width = .80, .20
bottom, height = .0, 1
right = left + width
top = 1

# fig = plt.figure(figsize=(12, 2))
# ax = fig.add_axes([0, 0, 1, 1])  #Left, Bottom, Width, Height
# # plt.show()

# # -------------------------------------
p = patches.Rectangle(
    (left, bottom), width, height,
    color='#d11e5d'
)
ax.add_patch(p)
# plt.show()

kpi_label3 = 'MIR'
MTD_P1 = '45K'
ax.text(.5 * (left + right), .55 * (bottom + top), kpi_label3,
        ha='center', va='center',
        fontsize=24, color='black',
        transform=ax.transAxes)

ax.text(.5 * (left + right), .3 * (bottom + top), MTD_P1,
        ha='center', va='center',
        fontsize=24, color='green',
        transform=ax.transAxes)

# plt.show()
plt.tight_layout()
plt.savefig('Box_Assignment.png')

img1 = Image.open("D:/PYTHON/ProjectTraining/Box_Assignment.png")
img2 = Image.open("D:/PYTHON/ProjectTraining/Assignment5_Tuly.png")
# img2.show()

width, height = img1.size
imageSize = Image.new('RGB', (1200, 700))
imageSize.paste(img1, (0, 0))
imageSize.paste(img2, (0, height))
# imageSize.paste(img3, (0, height))
# imageSize.paste(img4, (width, height))
# imageSize.show()
imageSize.save("Assignment9_Roseline.png")

# img=Image.open("D:/PYTHON/ProjectTraining/four_Image.png")