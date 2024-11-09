x = int(input())
y = int(input())
z = int(input())
n = int(input())

res = []

for i in range(x+1):
    for j in range(y+1):
        for u in range(z+1):
            res.append([i, j, u])

print([i for i in res if sum(i) != n])
