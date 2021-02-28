# baekjoon 1676
n = int(input())

factorial = 1
for i in range(n):
    factorial *= (i+1)

fact = str(factorial)
cnt = 0
for i in range(len(fact)-1, 0, -1):
    if fact[i] == '0':
        cnt += 1
    else:
        break

print(cnt)
