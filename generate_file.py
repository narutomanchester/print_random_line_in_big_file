import sys
import random 
import string

len_argv = len(sys.argv)
list_argv = list(sys.argv)
if (len_argv != 3):
    print("Wrong size of arguments. Exit program")
    exit()

data_size = int(float(list_argv[1]) * 1024 * 1024 * 1024) # data size in bytes = list_argv[1] GB

file_name = list_argv[2]

with open(file_name, 'w') as f:

    total_size = 0
    print(data_size)
    while total_size < data_size:
        size_of_each_line = random.randrange(10, 10*10, 8)
        line = ""

        for i in range(size_of_each_line):
            line += random.choice(string.ascii_letters)
        
        total_size += size_of_each_line

        f.write(line)
        f.write('\n')

print("generate file done")


