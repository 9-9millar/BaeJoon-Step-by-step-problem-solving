N = int(input())
l = []
Al = []
Bl = []

for _ in range(N):
    A,B = map(int,input().split())
    l.append(A+B)
    Al.append(A)
    Bl.append(B)
for i in range(N):
    print('Case #%d:'%(i+1),Al[i],'+',Bl[i],'=',l[i])