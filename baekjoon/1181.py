dic = set()
n = int(input())

for i in range(n):
    dic.add(input())

dic = sorted(dic, key=lambda x : (len(x), x))
for word in dic:
    print(word)

