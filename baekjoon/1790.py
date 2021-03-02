# baekjoon 1790. 사실 다시푸는거임

n, k = map(int, input().split())

numbers_with_i = 9
i = 1
total_number = 0
while(k > numbers_with_i*i):
    total_number += numbers_with_i
    k -= numbers_with_i * i
    numbers_with_i *= 10
    i += 1

# print(i, k)

total_number += (k-1) // i+1
# print(total_number)
if total_number > n:
    print(-1)
else:
    idx = (k-1) % i
    print(str(total_number)[idx])
