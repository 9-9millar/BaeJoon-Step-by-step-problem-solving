import sys
data = [int(sys.stdin.readline()) for i in range(9)]
a = max(data)

print(a,data.index(a)+1,sep='\n')