"""
Exercise 2
Create a program called tree.py

Given a file path (absolute or relative), the program should write to a file all of the contents of the directory and the child directories bellow it. The output file should look something like this:

./file1.py
./file2.py
./dir1/file1_in_dir1.txt
./dir1/file2_in_dir1.txt
./dir3/file1_in_dir3.txt

import os
import pathlib

file_path = input('Enter file path:')
path_type = input('Enter abs or rel:')

try:
    if os.path.isfile(file_path):
        os.chdir(file_path)
        os.listdir(file_path)


    if path_type == 'abs':
        path = pathlib.PurePath(file_path)
        directory = os.path.abspath(path)
        #for i in directory:
         #   print(i)
    parent_dir = os.path.dirname(path)
    print(parent_dir)




except (NotADirectoryError, FileNotFoundError):
    print('Not a file or there is no such file')
"""

import os
import pathlib

def dir_files_info():
    file_path = input('Enter file path:')
    dir_name_1 = os.path.dirname(file_path)
    dir_name = os.chdir(dir_name_1)
    data = []

    if os.path.isfile(file_path):

        for root, dirs, files in os.walk(".", topdown=True):
            for name in files:
                filename = os.path.join(root,name)
                data.append(filename)
                #print(os.path.join(root,name))
            for name in dirs:
                filename = os.path.join(root, name)
                data.append(filename)
                #print(os.path.join(root,name))

    else:
        print('This is not a file path')
    return data

new_file = open('output1.txt', 'w')

for filename in dir_files_info():
    new_file.write(filename)
    new_file.write("\n");

new_file.close()
