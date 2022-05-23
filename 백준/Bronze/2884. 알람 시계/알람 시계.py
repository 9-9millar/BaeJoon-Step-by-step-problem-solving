# 45분 일찍 일어나기
H, M = map(int,input().split())

a = H * 60 + M #모두 분 단위로 바꾸기

if a > 45: #(ii)
    a = a - 45
    H = a // 60
    M = a % 60
    print(H,M)

else: # a <= 45, H = 0, M <= 45
    a = a - 45
    if a == 0: # 0 45
        H = 0
        M = 0
        print(H,M)
    else:
        H = 23
        M = 60 + a
        print(H,M)