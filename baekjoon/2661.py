# baekjoon 2661

N = int(input())

def backtracking(s):
  l = len(s)
  for i in range(1, l//2+1): # 길이
    if s[l-(2*i):l-i] == s[l-i:]: return
  if l == N:
    print(s)
    exit(0)
  for i in range(1, 4):
    if s and s[-1] == str(i): continue
    backtracking(s+str(i))

backtracking('')
