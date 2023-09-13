import os
import shutil

folder_path = "D:\Sarab youtube\\automated videos\\automated videos"
new_name = "image"
extension = ".jpg" 
extension1 = ".png" # Change the extension to match your image files

counter = 1

for filename in os.listdir(folder_path):
    if filename.endswith(extension):
        new_filename = f"{new_name}_{counter}{extension}"
        old_file_path = os.path.join(folder_path, filename)
        new_file_path = os.path.join(folder_path, new_filename)
        shutil.move(old_file_path, new_file_path)
        counter += 1

for filename in os.listdir(folder_path):
    if filename.endswith(extension1):
        new_filename = f"{new_name}_{counter}{extension1}"
        old_file_path = os.path.join(folder_path, filename)
        new_file_path = os.path.join(folder_path, new_filename)
        shutil.move(old_file_path, new_file_path)
        counter += 1