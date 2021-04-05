def solution(answers):
    tester = [[], [1, 2, 3, 4, 5], [2, 1, 2, 3, 2,
                                    4, 2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    total = [0, 0, 0, 0]

    for i in range(len(answers)):
        for j in range(1, 4):
            if answers[i] == tester[j][i % len(tester[j])]:
                total[j] += 1

    max_score = max(total)
    answer = []
    for i in range(1, len(total)):
        if total == total[i]:
            answer.append(i)
    return answer


solution([1, 2, 3, 4, 5])
solution([1, 3, 2, 4, 2])
