import os

global total

def disk_size(path):
    total = 0
    if os.path.isdir(path) == True:
        L = os.listdir(path)
        for i in range(0,len(L)):
            child = os.path.join(path,L[i])
            size = os.path.getsize(child)
            print "{0:<7} {1}".format(size, child)
            total = total + size
    print "{0:<7} {1}".format(total, path)
    return total

path = raw_input()
if os.path.exists(path) == True:
    print '\n'
    print disk_size(path)
else :
    print "directory is not exist or is wrong"
