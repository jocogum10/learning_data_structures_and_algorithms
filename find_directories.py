import os

def find_directories(dir):
    dir_obj = os.scandir(dir)
    for file in dir_obj:
        if file.is_file():          # base case
            print("---->File: {0}".format(file.name))
        elif file.is_dir():
            print("Dir: {0}".format(file.path))
            find_directories(file.path)
            
        
find_directories('..')