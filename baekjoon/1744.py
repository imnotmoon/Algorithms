# baekjoon 1744
import time

n = int(input())
arr = []
res = []
for i in range(n):
    arr.append(int(input()))

if len(arr) == 1:
    print(arr[0])
    exit()

arr.sort(key=lambda x: abs(x), reverse=True)
# print(arr)

while(len(arr)):
    current_max = arr[0]        # 혼자
    max_idx = 0
    for i in range(1, len(arr)):
        # print(arr[0], arr[i])
        mult = arr[0] * arr[i]
        if mult > current_max:
            max_idx = i
            break
    if max_idx != 0:  # 두 수가 묶인 경우
        # print("묶임 : ", arr[0], arr[max_idx])
        res.append(arr[0] * arr[max_idx])
        arr.pop(max_idx)
        arr.pop(0)
    else:
        # print("혼자 : ", arr[0])
        res.append(arr[0])
        arr.pop(0)

# print(res)
print(sum(res))
