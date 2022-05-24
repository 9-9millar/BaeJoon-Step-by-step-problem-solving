T = int(input())

list = []
for _ in range(T):
    A, B = map(int,input().split())
    list.append(A+B)

for i in range(T):
    print(list[i])