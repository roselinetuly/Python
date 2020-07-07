from PIL import Image


img1 = Image.open("D:/PYTHON/ProjectTraining/Figure1.jpeg")
img2 = Image.open("D:/PYTHON/ProjectTraining/Figure2.png")
img3 = Image.open("D:/PYTHON/ProjectTraining/Figure3.jpeg")
img4 = Image.open("D:/PYTHON/ProjectTraining/Figure4.jpeg")

width, height = img1.size
imageSize = Image.new('RGB', (1280, 960))
imageSize.paste(img1, (0, 0))
imageSize.paste(img2, (width, 0))
imageSize.paste(img3, (0, height))
imageSize.paste(img4, (width, height))
imageSize.save("four_Image.png")
img=Image.open("D:/PYTHON/ProjectTraining/four_Image.png")
img.show()
# print("Two_Image.png")
# img1.show()
# # img2.show()
# # img3.show()
# # img4.show()
