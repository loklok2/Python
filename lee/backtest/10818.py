n, m = map(int, input().split())
bk = list(range(1, n+1))
def re_bk(bk, i, j):
    while i < j:
        bk[i-1], bk[j-1] = bk[j-1], bk[i-1]
        i += 1
        j -= 1
for _ in range(m):
    i, j = map(int, input().split())
    re_bk(bk, i, j)
print(*bk)
