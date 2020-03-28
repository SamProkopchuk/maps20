n,m = map(int, input().split())
going_out = [0 for i in range(n)]
going_to = [0 for i in range(n)]

for i in range(m):
    x,y = map(int, input().split())
    going_out[x]+=1
    going_to[y]+=1

count = 0
for i in range(n):
    if going_out[i] == 0:
        count += n-going_to[i] -1
        for j in range(n):
            if i!=j and going_out[j]==0:
                going_out[j]+=1
    elif going_to[i] == 0:
        count += n - going_out[i] - 1
        for j in range(n):
            if i!=j and going_to[j]==0:
                going_to[j]+=1
print(count)