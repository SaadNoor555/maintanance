from see_changes import *
from linecount import *
import os

def check_changes(folder1, folder2, changefile):
    f1_files = os.listdir(folder1)
    f2_files = os.listdir(folder2)

    for file in f1_files:
        if file not in f2_files or file=='.git' or file=='a.out':
            continue
        print(file)
        f1_path = os.path.join(folder1, file)
        f2_path = os.path.join(folder2, file)
        if os.path.isdir(f1_path):
            check_changes(f1_path, f2_path, changefile)
            continue
        write_changes(f1_path, f2_path, changefile)


if __name__ == "__main__":
    f2 = 'Information_Security_1'
    f1 = 'Information_Security'
    check_changes(f1, f2, 'changes.diff')