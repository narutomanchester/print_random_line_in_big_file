import sys
import random

len_argv = len(sys.argv)
list_argv = list(sys.argv)
if (len_argv != 2):
    print("Wrong size of arguments. Exit program")
    exit()

file_name = list_argv[1]

def read_by_chunk(file, size=65536):
    while True:
        data = file.read(size)
        if not data: break
        
        yield data
        
count = 0
data  = ""

with open(file_name, "r") as f:
    
    for lines in read_by_chunk(f):
        count += int(lines.count("\n"))
        data += lines
    
import random
list_random = random.sample(range(count), 1)

for _id, line in enumerate(data.splitlines()):
    if _id == list_random[0]:
        print(line)

