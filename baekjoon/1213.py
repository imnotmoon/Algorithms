# baekjoon 1213
import sys
input = sys.stdin.readline

name = input().strip()
count = dict()

for letter in name:
    if letter in count.keys():
        count[letter] += 1
    else:
        count[letter] = 1

sorted_count = sorted(count.items())
ret = ''

# 홀수개는 하나만 가능함
odd_cnt = 0
is_available = True
for i in count.keys():
    if count[i] % 2 == 1:
        odd_cnt += 1
    if odd_cnt == 2:
        is_available = False
        break

# 여기서부터는 가능한 경우
left_letter = ''
for item in sorted_count:
    key, value = item[0], item[1]
    if value % 2 == 1:
        ret += key * ((value-1) // 2)
        left_letter = key
    else:
        ret += key * (value // 2)

if is_available:
    print(ret + left_letter + ret[::-1])
else:
    print("I'm Sorry Hansoo")
