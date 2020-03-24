import sys
import random

len_argv = len(sys.argv)
list_argv = list(sys.argv)
if (len_argv != 2):
    print("Wrong size of arguments. Exit program")
    exit()

file_name = list_argv[1]

with open(file_name, 'rb') as f:
    f.seek(0, 2)
    filesize = f.tell()

    random_set = sorted(random.sample(range(filesize), 1))

    f.seek(random_set[0])
    print(f.readline().rstrip()) 
