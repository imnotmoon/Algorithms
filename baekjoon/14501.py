# baekjoon 14510

n = int(input())
timetable = []

for i in range(n):
    timetable.append(list(map(int, input().split())))

dp = list(map(lambda x: x[1], timetable))

for i in range(n):
    to = timetable[i][0]

    # 퇴사한 다음 상담이 끝나는 스케줄의 경우
    # 상담 접수가 불가능하므로 삭제
    if i + to > n:
        dp[i] = 0
        continue

    t = dp[i]
    for j in range(i + to, n):
        if t + timetable[j][1] > dp[j]:
            dp[j] = t + timetable[j][1]
print(max(dp))
