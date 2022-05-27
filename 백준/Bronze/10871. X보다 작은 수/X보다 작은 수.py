N, X = map(int,input().split())
A = list(map(int,input().split()))
l = []
for i in range(N):
    if A[i] < X:
        l.append(A[i])

for i in range(len(l)):
    print(l[i])