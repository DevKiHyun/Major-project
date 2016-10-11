import sys
n = int(raw_input())
F = []
F.append(0)
F.append(1)
for i in range(1,n+1) :
    F.append(F[i] + F[i-1])

print F[n]
