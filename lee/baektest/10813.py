n, m = map(int, input().split())
bk = [i for i in range(1, n+1)]
def change_bk(bk, i, j):
    bk[i-1], bk[j-1] = bk[j-1], bk[i-1]
for _ in range(m):
    i,j = map(int, input().split())
    change_bk(bk, i, j)
print(*bk) 