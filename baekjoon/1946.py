T = int(input())
testCase = []

def countPassed(sortedApplicants) :
    ret = 1
    lessThan = sortedApplicants[0][1]
    for person in sortedApplicants[1:] :
        if person[1] < lessThan : 
            lessThan = person[1]
            ret += 1
    return ret

for i in range(T) :
    N = int(input())
    apply = []
    for i in range(N) :
        apply.append(list(map(int, input().split())))
    testCase.append(apply)

for i in testCase:
    sortedApplicants = sorted(i, key=lambda x: x[0])
    passed = countPassed(sortedApplicants)
    print(passed)

