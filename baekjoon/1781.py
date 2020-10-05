n = int(input())
quest = []  # [데드라인, 컵라면]
for i in range(n) :
    t = list(map(int, input().split()))
    quest.append(t)

newQuest = sorted(quest, key=lambda x: [-x[0], -x[1]])
lastDay = newQuest[0][0]

totalCupRamen = 0

# 마지막 날부터 시작
for i in range(lastDay, 0, -1) :
    bestSelectionIdx = 0
    dayExist = 1    # i 이상의 데드라인을 주는 문제가 남아있지 않은 경우
    # (남아있는) 큰 데드라인의 문제부터 하나씩 탐색
    for j in range(len(newQuest)-1) :
        if newQuest[j][0] < i :
            break
        if newQuest[bestSelectionIdx][1] <= newQuest[j][1] :
            dayExist = 0
            bestSelectionIdx = j
    if dayExist == 0 :
        # i보다 큰 데드라인을 가진 문제들 중 컵라면을 제일 많이 주는 문제
        totalCupRamen += newQuest[bestSelectionIdx][1]
        newQuest.remove(newQuest[bestSelectionIdx])

print(totalCupRamen)

# 시간초과