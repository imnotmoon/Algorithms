answer = []

def solution(orders, course):
    global answer
    for i in range(len(course)):
        getOrders(orders, course[i])
    answer = sorted(list(set(answer)))
    print(answer)
    return answer

def getOrders(orders, size):
    global answer
    from itertools import combinations
    orderedCombination = []
    for i in range(len(orders)):
        tmp = list(combinations(orders[i], size))
        for j in tmp: orderedCombination.append(''.join(sorted(list(j))))
    cnt, idx = 0, 0
    for i in range(len(orderedCombination)):
        if orderedCombination.count(orderedCombination[i]) > cnt : 
            cnt = orderedCombination.count(orderedCombination[i])
            idx = i

    for i in orderedCombination:
        if orderedCombination.count(i) == cnt and cnt > 1:
            answer.append(i)




solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4])
# solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2, 3, 5])
# solution(["XYZ", "XWY", "WXA"], [2, 3, 4])