import os
import shutil
path='C:/Users/19514/Desktop/C-99'
print("before moving the file")
print(os.listdir(path))
source='C:/Users/19514/Desktop/C-99'
destination="C:/Users/19514/Desktop/Python"
d1=shutil.move(source,destination)
print("after moving the file")
print(os.listdir(destination))