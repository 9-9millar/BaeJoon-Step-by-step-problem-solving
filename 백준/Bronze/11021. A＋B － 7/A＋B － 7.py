N = int(input())
l = []
for _ in range(N):
    A,B = map(int,input().split())
    l.append(A+B)
    
for i in range(N):
    print('Case #%d:'%(i+1),l[i])