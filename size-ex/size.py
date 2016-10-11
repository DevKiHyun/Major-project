import os

def disk_size(path):
    total = os.path.getsize(path)
    if os.path.isfile(path) == True :
        total = os.path.getsize(path)
        print "{0:<7} {1}".format(total, path)
    elif os.path.isdir(path) == True :
        for child in os.listdir(path) :
            child = os.path.join(path, child)
            total = total + disk_size(child)
        print "{0:<7} {1}".format(total, path)
    return total

path = raw_input()
if os.path.exists(path) == True:
    print ""
    print disk_size(path)
else :
    print "Path is not exist or is wrong"
