N = int(input())
grade = list(map(int,input().split()))

r = max(grade)
sum = 0
for i in range(N):
    a = grade[i] / max(grade) * 100
    sum += a

print(sum / N)