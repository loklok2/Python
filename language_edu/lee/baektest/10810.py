n, m = map(int, input().split())
bk = [0] * n
for _ in range(m):
    i, j, k = map(int, input().split())
    for idx in range(i-1,j):
        bk[idx] = k
for bks in bk:
    print(bks, end=' ')