
import os
from PIL import Image 
  



def traverse_directory(directory):
    for root, dirs, files in os.walk(directory):
        print(f"Current directory: {root}")
        print("Subdirectories:")
        for directory_name in dirs:
            print(os.path.join(root, directory_name))
        print("Files:")
        for file_name in files:
            print(os.path.join(root, file_name))
            
root = 'D:/TEMP/uuu/.data/home/JJmow/Labs/ML/finalProject/data'
# root = 'trainlog'

label = root + '/image_class_labels.txt'
img = root + '/image.txt'
trainTest = root + '/train_test_split.txt'

link = 'D:/TEMP/uuu/.data/home/JJmow/Labs/ML/finalProject/ref/MMAL-Net/datasets/CUB_200_2011/bounding_boxes.txt'


root = 'D:/TEMP/uuu/.data/home/JJmow/Labs/ML/finalProject/data/train'
# traverse_directory(root)


with open(link, 'w') as f1:
    
    counter = 0
    split = 15
    for root, dirs, files in os.walk(root):
        print(f"Current directory: {root}")
        print("Subdirectories:")
        for directory_name in dirs:
            print(os.path.join(root, directory_name))
        for file_name in files:
            counter += 1

            filepath = root + '/' + file_name
            
            img = Image.open(filepath)
            
            w = img.width
            h = img.height
            
            f1.write(f'{counter} 0.0 .0.0 {w}.0 {h}.0\n')
            
print(counter)