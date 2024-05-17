# T = int(input())
# for _ in range(T):
#     R, S = input().split()
#     result =' '
#     for i in range(len(S)):
#         result += S[i]*int(R)
#     print(result)

T = int(input())
for _ in range(T):
    R, S = input().split()
    result = ''
    for i in S:
        result += i * int(R)
    print(result)