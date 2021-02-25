# baekjoon 16953

a, b = map(int, input().split())

queue = list()
queue.append((a, 0))

ret = -1
while queue:
    current = queue.pop(0)
    if current[0] > b:
        continue
    if current[0] == b:
        ret = current[1]+1
        break
    if current[1]*2 < b:
        queue.append((current[0]*2, current[1]+1))
    if current[1]*10+1 < b:
        queue.append((current[0]*10+1, current[1]+1))

print(ret)
