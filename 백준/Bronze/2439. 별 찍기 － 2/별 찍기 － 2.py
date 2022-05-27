N = int(input())
l = []
for i in range(1,N+1):
    str1 = ' '*(N-i) + '*'*i
    l.append(str1)

for i in range(N):
    print(l[i])