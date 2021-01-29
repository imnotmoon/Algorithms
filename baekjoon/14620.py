import sys
input = sys.stdin.readline

# 집합연산을 이용함
# 그 외에는 brute force로 풀어도 문제 없음

def calc_fee(lst):
    dx, dy = [0, -1, 0, 1, 0], [0, 0, -1, 0, 1]
    petals = []
    result = 0

    for flower in lst:
        x = flower // N
        y = flower % N

        # 테두리가 아닌 경우
        if x==0 or x==N-1 or y==0 or y==N-1:
            return 10000

        for i in range(5):
            petals.append((x+dx[i], y+dy[i]))
            result += garden[x+dx[i]][y+dy[i]]     # 땅값 합

    # 집합으로 변환해서 길이 체크 : 제대로 다 들어갔으면 15겠지
    if len(set(petals)) == 15:
        return result
    return 10000

N = int(input())
garden = [list(map(int, input().split())) for _ in range(N)]

fee = 10000
for i in range(N*N):
    for j in range(N*N):
        for k in range(N*N):
            lst = [i, j, k]
            fee = min(fee, calc_fee(lst))
print(fee)