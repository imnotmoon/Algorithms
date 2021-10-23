# baekjoon 1541
exp = input()
bracket = False
i = 0
while i < len(exp):
  if i > 0 and exp[i-1] in ['-', '+', '('] and exp[i] == '0':
    while exp[i] == '0':
      exp = exp[:i] + exp[i+1:]
  if i == 0 and exp[i] == '0' :
    while exp[i] == '0':
      exp = exp[i+1:]
  if exp[i] == '-' and not bracket:
    bracket = True
    exp = exp[:i+1] + '(' + exp[i+1:]
  elif exp[i] == '-' and bracket:
    bracket = False
    exp = exp[:i] + ')' + exp[i:]
  i += 1
if bracket : exp += ')'

print(eval(exp))