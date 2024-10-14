from PIL import Image
from matplotlib.pyplot import imshow
import pandas
import matplotlib.pylab as plt
import os
import glob
import skillsnetwork

directory="/Users/fpj/Development/python/ml-with-python/capstone/resources/data"
negative='Negative'
positive='Positive'

negative_file_path=os.path.join(directory,negative)
positive_file_path=os.path.join(directory, positive)

print("Negative file path: ", negative_file_path)
print("Positive file path: ", positive_file_path)

print("First three negative files: ", os.listdir(negative_file_path)[0:3])
print("First three positive files: ", os.listdir(positive_file_path)[0:3])
#
negative_files = [os.path.join(negative_file_path, file) for file in os.listdir(negative_file_path)][0:3]
positive_files = [os.path.join(positive_file_path, file) for file in os.listdir(positive_file_path)][0:3]
#
print("First three negative images: ", negative_files)
print("First three positive images: ", positive_files)

# First image in negative
img_neg_01 = Image.open(negative_files[0])
plt.imshow(img_neg_01)
plt.title('First Image with no cracks')
plt.show()

# Second image in negative
img_neg_02 = Image.open(negative_files[1])
plt.imshow(img_neg_02)
plt.title('Second Image with no cracks')
plt.show()

# Plot the first 3 images in positive
print("First three positive files: ", os.listdir(positive_file_path)[0:3])

# First image in posative
img_pos_01 = Image.open(positive_files[0])
plt.imshow(img_pos_01)
plt.title('First Image with cracks')
plt.show()

# Second image in positive
img_pos_02 = Image.open(positive_files[1])
plt.imshow(img_pos_02)
plt.title('Second Image with cracks')
plt.show()

# Third image in positive
img_pos_03 = Image.open(positive_files[2])
plt.imshow(img_pos_03)
plt.title('Third Image with cracks')
plt.show()

# In lab: 12849_1.jpg, 08089.jpg, 08052.jpg
