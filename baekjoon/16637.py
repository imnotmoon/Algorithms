# baekjoon 16637
from copy import deepcopy
n = int(input())
exp = [ int(i) if i not in ['+', '-', '*'] else i for i in input().strip() ]

def calc(pre, post, op):
  return eval(f'{pre} {op} {post}')

def calc_queue(q):
  result = q[0]
  for i in range(0, len(q)-2, 2):
    result = calc(result, q[i+2], q[i+1])
  return result

def bracket(i, q):
  if i == n-1:  # 마지막 숫자
    q.append(exp[i])
    return calc_queue(q)
  if i == n-3:
    if_use_bracket = q + [calc(exp[i], exp[i+2], exp[i+1])]
    if_skip_bracket = q + [exp[i], exp[i+1]]
    return max(bracket(i+2, if_use_bracket), bracket(i+2, if_skip_bracket))

  # 괄호를 넣는 경우
  t = calc(exp[i], exp[i+2], exp[i+1])
  if_use_bracket = q + [t, exp[i+3]]
  # 괄호를 안넣는 경우
  if_skip_bracket = q + [exp[i], exp[i+1]]
  return max(bracket(i+4, if_use_bracket), bracket(i+2, if_skip_bracket))

print(bracket(0, []))