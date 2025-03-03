import os
def path_i(path):
    print('\n','-' * 60)
    if os.path.exists(path):
        print("File/folder name: ", os.path.basename(path))

        print("Directory part: ", os.path.dirname(path))
        if os.path.isdir(path):
            items = os.listdir(path)
            print("Folders and Files: ")
            for i in items:
                print(i, end=' ')
    else:
        print("The specified path does not exist or is entered incorrectly.")

path1 = "c:/Users/user/Desktop/Labaratory_Works/Labs/LAB6/Directories_and_files/1.py"
path_i(path1)
path2 = "c:/Users/user/Desktop/Labaratory_Works/Labs/LAB6/Directories_and_files"
path_i(path2)
path3 = "c:/Users/user/Desktop/Labaratory_Works/Labs/LAB6/Directories_and_files/hello"
path_i(path3)