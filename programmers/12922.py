def solution(n):
    return '수박'*(n//2) if n % 2 == 0 else '수박'*(n//2)+'수'


print(solution(3))
print(solution(4))
