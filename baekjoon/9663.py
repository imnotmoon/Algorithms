# baekjoon 9963

n = int(input())
cnt = 0

is_used1 = [0 for _ in range(n)]
is_used2 = [0 for _ in range(2*n - 1)]
is_used3 = [0 for _ in range(2*n - 1)]


def func(m):  # m행
    global cnt
    if m == n:
        cnt += 1
        return
    # m+1행에 대한 조사
    for i in range(n):
        if is_used1[i] == 1 or is_used2[i+m] == 1 or is_used3[m-i+n-1] == 1:
            continue
        is_used1[i], is_used2[i+m], is_used3[m+n-i-1] = 1, 1, 1
        func(m+1)
        is_used1[i], is_used2[i+m], is_used3[m+n-i-1] = 0, 0, 0


func(0)
print(cnt)
