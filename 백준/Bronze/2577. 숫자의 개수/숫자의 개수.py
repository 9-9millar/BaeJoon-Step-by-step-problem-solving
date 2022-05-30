import sys
list = [int(sys.stdin.readline()) for i in range(3)]

a = list[0]
b = list[1]
c = list[2]

D = a * b * c
D = str(D)

for i in range(10):
    print(D.count('%d'%(i)))