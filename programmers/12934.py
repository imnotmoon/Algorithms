def solution(n):
    answer = -1
    start, end = 0, 30000000
    while(end - start > 1):
        mid = (start+end) // 2
        if mid**2 > n:
            end = mid
        elif mid ** 2 < n:
            start = mid
        else:
            answer = (mid+1)**2
            break
    return answer


# solution(121)
solution(50000000000000)
