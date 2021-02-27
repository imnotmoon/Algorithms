# baekjoon 11723
import sys
input = sys.stdin.readline

m = int(input())
s = set()
for i in range(m):
    cmd = list(map(str, input().split()))
    cmd.append(0)
    num = int(cmd[1])
    if cmd[0] == 'add':
        s.add(num)
    elif cmd[0] == 'remove':
        if num in s:
            s.remove(num)
    elif cmd[0] == 'check':
        print(1 if num in s else 0)
    elif cmd[0] == 'toggle':
        if num in s:
            s.remove(num)
        else:
            s.add(num)
    elif cmd[0] == 'all':
        s = set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11,
                 12, 13, 14, 15, 16, 17, 18, 19, 20])
    elif cmd[0] == 'empty':
        s = set()
