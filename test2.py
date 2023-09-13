import shutil
import os

source_folder = 'D:\Sarab youtube\\automated videos\\automated videos\\automated videos'
destination_folder = 'D:\Sarab youtube\\automated videos\\automated videos'

for filename in os.listdir(source_folder):
    if filename.endswith('.jpg') or filename.endswith(".png"):
        source_path = os.path.join(source_folder, filename)
        destination_path = os.path.join(destination_folder, filename)
        shutil.move(source_path, destination_path)