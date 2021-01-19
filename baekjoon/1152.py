token = input().strip().split(' ')
if len(token) == 1 and token[0] == '':
    print(0)
else:
    print(len(token))
