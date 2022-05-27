A= None; B = None
l = []
while (A and B) !=0:
    A, B = map(int,input().split())
    if A == 0 and B == 0:
        break
    l.append(A+B)

for i in range(len(l)):
    print(l[i])