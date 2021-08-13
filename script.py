import os
from sys import argv
script, first, second, third, fourth = argv
    

dirName = second
for i in range(1,(int(third)+1)) : 
    dirName = dirName + str(i)
    try:
        os.mkdir(dirName, mode=int(fourth))
        print("Directory " , dirName ,  " Created ")
    except FileExistsError:
        print("Directory " , dirName ,  " already exists")  
    dirName= 'usr'    


