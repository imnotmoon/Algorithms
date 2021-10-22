# baekjoon 1918
exp = input()
from collections import deque
deq = deque()
res = ''

for i in range(len(exp)):
  if exp[i] not in ['+', '-', '*', '/', '(', ')']: res += exp[i]
  else :
    if exp[i] == '(' : deq.append(exp[i])
    elif exp[i] in ['*', '/']:
      while deq and deq[-1] in ['*', '/']: res += deq.pop()
      deq.append(exp[i])
    elif exp[i] in ['+', '-']:
      while deq and deq[-1] != '(': res += deq.pop()
      deq.append(exp[i])
    elif exp[i] == ')':
      while deq and deq[-1] != '(': res += deq.pop()
      deq.pop()

print(res)

while deq:
  res += deq.pop()
  
print(res)