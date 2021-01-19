# baekjoon 1431
from functools import cmp_to_key

def compare(a, b):
    # 1. 길이로 비교
    if len(a) < len(b) :
        return -1
    elif len(a) > len(b) :
        return 1
    else :
        # 2. 자리수 합으로 비교
        total_a, total_b = 0, 0
        for i in range(len(a)) :
            try:
                total_a += int(a[i])
            except:
                pass
            try:
                total_b += int(b[i])
            except:
                pass
        if total_a < total_b:
            return -1
        elif total_a > total_b:
            return 1
        else :
            # 3. 사전 순으로 비교. 숫자가 알파벳보다 사전순으로 작다.
            for i in range(len(a)):
                if ord(a[i]) < ord(b[i]):
                    return -1
                elif ord(a[i]) > ord(b[i]):
                    return 1

n = int(input())
guitars = []
for i in range(n):
    guitars.append(input())
    
result = sorted(guitars, key=cmp_to_key(compare))
for i in result:
    print(i)