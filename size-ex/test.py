import os
def disk_size(path) :
    total = os.path.getsize(path)
    if os.path.isdir(path) == True :
        dir = os.listdir(path)
        for x in range(len(dir)):
            child = os.path.join(path, dir[x])
            total = total + disk_size(child)
    elif os.path.isfile(path) == True:
        print "{0:<7} {1}".format(total, path)
        return total
    print "{0:<7} {1}".format(total, path)
    return total

path = '/home/namkihyun/test'
if os.path.exists(path) == True:
    print ""
    print disk_size(path)
else :
    print "Path is not exist or is wrong"
