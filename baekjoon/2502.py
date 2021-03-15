# baekjoon 2502

d, k = map(int, input().split())
da, db = [0 for _ in range(d+1)], [0 for _ in range(d+1)]
da[1], db[2] = 1, 1
for i in range(3, d+1):
    da[i] = da[i-1]+da[i-2]
    db[i] = db[i-1]+db[i-2]

i, j = 1, 1
while(True):
    j = (k-(da[d]*i)) // db[d]
    # print(i, j)
    if (k - (da[d]*i)) % db[d] == 0 and i <= j:
        print(i)
        print(j)
        break
    i += 1
