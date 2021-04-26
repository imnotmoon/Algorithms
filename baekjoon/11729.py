# baekjoon 11729

n = int(input())
ret = 0
moved = []


def move(start, spare, end, k):
    global ret
    if k == 1:
        moved.append(f"{start} {end}")
        ret += 1
        return
    move(start, end, spare, k-1)
    move(start, spare, end, 1)
    move(spare, start, end, k-1)


move(1, 2, 3, n)
print(ret)
for i in moved:
    print(i)
