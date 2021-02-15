# 1427
n = input()
arr = [int(i) for i in n]
for i in sorted(arr, reverse=True):
    print(i, end='')
    