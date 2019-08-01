x11=int(input())
l=list(map(int,input().split()))
y11=l[0]
for p in range(1,len(l)):
    y11=y11|l[p]
print(y11)
