n, m = map(int, input().split())
bk = [i for i in range(1, n+1)]
for i in range(m):
    i,j = map(int, input().split())
    k = bk[i-1:j]
    k.reverse()
    bk[i-1:j] = k
for i in range(n):
    print(bk[i], end=' ')