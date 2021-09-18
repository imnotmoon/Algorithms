# baekjoon 1062
# a n t i c

import sys
from itertools import combinations
input = sys.stdin.readline

n, k = map(int, input().split())
antic = set(['a', 'n', 't', 'i', 'c'])
words = [set(input().strip()).difference(antic) for _ in range(n)]

wordDict = {
    'b': 20, 'd': 19, 'e': 18, 'f': 17, 'g': 16, 'h': 15, 'j': 14,
    'k': 13, 'l': 12, 'm': 11, 'o': 10, 'p': 9, 'q': 8, 'r': 7, 's': 6,
    'u': 5, 'v': 4, 'w': 3, 'x': 2, 'y':1, 'z': 0 
}

if k < 5: 
    print(0)
    exit()
if k == 26:
    print(n)
    exit()

def convert_binary(word):
    ret = 0b0
    for c in word:
        ret = ret | (1 << wordDict[c])
    return ret

binary_words = [ convert_binary(''.join(word)) for word in words]
ans = 0

po2 = [2 ** i for i in range(21)]
for comb in combinations(po2, k-5):
    current = sum(comb)
    count = 0
    for word in binary_words:
        if word & current == word:
            count += 1
    ans = max(ans, count)

print(ans)