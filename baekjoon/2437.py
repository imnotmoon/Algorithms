# baekjoon 2437 : 저울
# 추들로 측정할 수 없는 양의 정수 무게 중 최솟값

n = int(input())
weights = sorted(list(map(int, input().split())))

target = 1
for i in weights:
    if target < i:
        break
    target += i

print(target)