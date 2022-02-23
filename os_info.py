# http://helloraspberrypi.blogspot.com/2015/03/python-get-file-system-disk-space-usage.html
# link to tutorial

import os 

# print(os.popen('df -h /').read())
                                 
def getDf():
    df = os.popen("df -h /")
    i = 0
    while True:
        i = i + 1
        line = df.readline()
        if i==2:
            return(line.split()[0:6])

def getAvailableSpace():
    # Disk information
    disk_root = getDf()
    # Available space
    available_space = disk_root[3]
    return(available_space)


