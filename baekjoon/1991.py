# baekjoon 1991
import sys
input = sys.stdin.readline
n, t = int(input()), dict()
result = ''
for i in range(n):
  root, left, right = map(str, input().split())
  t[root] = (left, right)

def preorder(root):
  global result
  result += root
  left, right = t[root]
  if left != '.' : preorder(left)
  if right != '.' : preorder(right)


def inorder(root):
  global result
  left, right = t[root]
  if left != '.': inorder(left)
  result += root
  if right != '.': inorder(right)

def postorder(root):
  global result
  left, right = t[root]
  if left != '.': postorder(left)
  if right != '.' : postorder(right)
  result += root

preorder('A')
print(result)
result = ''
inorder('A')
print(result)
result = ''
postorder('A')
print(result)