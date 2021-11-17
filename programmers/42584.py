def solution(prices):
    answer = []
    for i in range(len(prices)):
      for j in range(i, len(prices)):
        if prices[i] > prices[j]:
          answer.append(j-i)
          break
      if len(answer) < i+1: answer.append(len(prices)-i-1)
    return answer

print(solution([1, 2, 3, 2, 3]))