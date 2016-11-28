import random

random.seed()

in_file = open('LIS_1.txt', 'w')
n = int(raw_input("n= "))
#in_file.write(str(n)+ '\n')
for i in range(n) :
    p = random.randint(0,1000)
    in_file.write(str(p)+ ' ')
in_file.close()
