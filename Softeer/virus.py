# 제한시간 : C/C++(1초), Java/Python(2초) | 메모리 제한 : 256MB
# 바이러스가 숙주의 몸속에서 1초당 P배씩 증가한다. 처음에 바이러스 K마리가 있었다면 N초 후에는 총 몇 마리의 바이러스로 불어날까? N초 동안 죽는 바이러스는 없다고 가정한다.
# 입력형식
# 첫 번째 줄에 처음 바이러스의 수 K, 증가율 P, 총 시간 N(초)이 주어진다.

# 입력은 다음 조건을 만족한다.

#    1 ≤ K ≤ 108 인 정수
#    1 ≤ P ≤ 108 인 정수
#    1 ≤ N ≤ 106 인 정수

import sys
input = sys.stdin.readline

k, p, n = map(int, input().split())
for i in range(n):
    k = (k*p) % 1000000007

print(k)
