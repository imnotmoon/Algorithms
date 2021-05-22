import sys
letters = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

word = sys.stdin.readline().strip()
for l in letters:
    word = word.replace(l, '0')
    
print(len(word))
