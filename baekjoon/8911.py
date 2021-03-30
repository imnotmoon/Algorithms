# baekjoon 8911
import sys
input = sys.stdin.readline

t = int(input())
dy, dx = [1, 0, -1, 0], [0, -1, 0, 1]


def turtle(command):
    head = 0
    current = [0, 0]
    ymax, ymin, xmax, xmin = 0, 0, 0, 0
    for i in range(len(command)):
        ymax, ymin = max(ymax, current[0]), min(ymin, current[0])
        xmax, xmin = max(xmax, current[1]), min(xmin, current[1])

        if command[i] == 'F':
            current[0] += dy[head]
            current[1] += dx[head]
        elif command[i] == 'B':
            current[0] -= dy[head]
            current[1] -= dx[head]
        elif command[i] == 'L':
            head = (head+1) % 4
        elif command[i] == 'R':
            head = (head+3) % 4

    if (ymax-ymin == 0 or xmax-xmin == 0):
        print(0)
    else:
        print((ymax-ymin) * (xmax-xmin))


for i in range(t):
    turtle(input())
