import os
import re
def rename_files():
    #(1) get file names from a folder
    file_list = os.listdir(r"D:\Educational\Python\prank")
    #print(file_list)
    saved_path = os.getcwd()
    print("Current Working Directory is"+saved_path)
    os.chdir(r"D:\Educational\Python\prank")

    #(2) for each file, rename filename
    for file_name in file_list:
        print("Old Name - " + file_name)
        print("New Name - " + re.sub("[0-9](?!\d*$)", "", file_name))
        os.rename(file_name, re.sub("[0-9](?!\d*$)", "", file_name))
    os.chdir(saved_path)

rename_files()
