# N, M, K

N, M, K = map(int, input().split())
num_lst = list(map(int, input().split()))

num_lst.sort()
temp = K
result = 0

while M:
    if temp:
        result += num_lst[-1]
    else:
        result += num_lst[-2]
        temp = K

    temp -= 1
    M -= 1

print(result)