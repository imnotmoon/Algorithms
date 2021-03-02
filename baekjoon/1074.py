# baekjoon 2074

n, r, c = map(int, input().split())
cnt = 0

dy, dx = [0, 0, 1, 1], [0, 1, 0, 1]


def count(y, x, size):
    global cnt
    if size == 2:
        for i in range(4):
            if (r, c) == (y+dy[i], x+dx[i]):
                print(cnt)
            cnt += 1
        return

    delta = size**2 // 4
    if (y <= r < y+size//2) and (x <= c < x+size//2):
        cnt += 0
        count(y, x, size//2)
    if (y <= r < y+size//2) and (x+size//2 <= c < x+size):
        cnt += delta
        count(y, x+size//2, size//2)
    if (y+size//2 <= r < y+size) and (x <= c < x+size//2):
        cnt += delta*2
        count(y+size//2, x, size//2)
    if (y+size//2 <= r < y+size) and (x+size//2 <= c < x+size):
        cnt += delta*3
        count(y+size//2, x+size//2, size//2)


count(0, 0, 2**n)
