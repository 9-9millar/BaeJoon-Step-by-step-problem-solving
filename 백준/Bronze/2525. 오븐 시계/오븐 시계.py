A, B = map(int,input().split())
C = int(input())

T = A * 60 + B + C
A = T // 60
if A >= 24:
    A = A - 24
B = T % 60
print(A,B)