# baekjoon 1062 다시풀기

from itertools import combinations
antic = ['a', 'n', 't', 'i', 'c']
to_learn = [False] * 26
total = 0

n, k = map(int, input().split())
words = [ set(input().strip()).difference(antic) for _ in range(n) ]

def backtracking(idx, length):
    global total
    if length == k-5:
        cnt = 0
        for word in words:
            flag = True
            for w in word:
                if not to_learn[ord(w) - ord('a')]:
                    flag = False
                    break
            if flag : cnt += 1
        total = max(total, cnt)
        return
    else :
        for i in range(idx, 26):
            if not to_learn[i]:
                to_learn[i] = True
                backtracking(i, length+1)
                to_learn[i] = False
        return

if k < 5 or k == 26:
    print(0 if k < 5 else n)
    exit()
else :
    for c in antic:
        to_learn[ord(c) - ord('a')] = True
    backtracking(0, 0)
    print(total)