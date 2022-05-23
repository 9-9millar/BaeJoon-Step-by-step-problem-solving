# 3개 주사위의 나온 눈이 주어짐
a,b,c = map(int,input().split())
if a == b == c:
    price = 10000 + a * 1000
elif a == b != c:
    price = 1000 + a * 100
elif a != b == c:
    price = 1000 + b * 100
elif a == c != b:
    price = 1000 + c * 100
elif a != b !=c:
    price = max(a,b,c) * 100
    
print(price)