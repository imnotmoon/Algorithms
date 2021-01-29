a, b = input(), input()
for i in range(len(b)):
    j = len(b)-i-1
    print(int(a)*int(b[j]))
print(int(a)*int(b))

