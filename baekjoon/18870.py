# baekjoon 18870

n = int(input())
numbers = list(map(int, input().split()))
set_numbers = sorted(set(numbers), reverse=True)

idx = dict()
length = len(set_numbers)
for i in range(length):
    idx[set_numbers[i]] = length-i-1

for i in range(n):
    print(idx[numbers[i]], end=' ')

print()
