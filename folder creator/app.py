# Recursively create directories and subdirectories with given struct
# Example: >app 5 c:/test spo0kye test/first test/second
import os
import sys


if len(sys.argv) == 2:
    if sys.argv[1] == "-h":
        print('example: 4 c:/test programming home/java home/csharp home/python, it will create 4 folders "programming" with home\
            /java, home/python and home/csharp')
        sys.exit(0)
    
if len(sys.argv) <= 4 or len(sys.argv) > 20:
    print("usage: {app} parent_folder main_folder amount_of_copies  subfolders(max 15)")
    sys.exit(1)

path = sys.argv[2] + "/"
main_folder = sys.argv[3]
for i in range(int(sys.argv[1])):
    for subfolder in sys.argv[4:]:
        actualPath = path + main_folder + str(i)
        try:
            os.makedirs(actualPath + '/' + subfolder, exist_ok=True)
        except:
            print("Couldn't create folders, unable to access path")
            sys.exit(2)