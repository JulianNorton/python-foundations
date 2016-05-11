import os



def rename_files():
    # 1. get file names from a folder
    file_list = os.listdir("/Users/j/github/python-foundations/")
    print(os.listdir("/Users/j/github/python-foundations/"))
    print("/Users/j/github/python-foundations/")
    saved_path = os.getcwd()
    os.chdir("/Users/j/github/python-foundations/")
    # 2. For each file, rename filename.
    for file_name in file_list:
        print(file_name)
        file_name = os.rename(file_name, file_name.strip("0123456789"))
        print(file_name)


rename_files()

