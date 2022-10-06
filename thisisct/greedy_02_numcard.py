# N, M 행 열
N, M = map(int, input().split())

card_lst = list()
for _ in range(N):
    temp = list(map(int, input().split()))
    card_lst.append(min(temp))

print(max(card_lst))

