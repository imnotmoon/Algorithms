N=input()
if N[0]=='0':
    print(0)
else:
    encode=[1,1]
    for i in range(1, len(N)):
        ans = 0
        if int(N[i])>0:
            ans = ans + encode[i]
        if 10*int(N[i-1])+int(N[i])>=10 and 10*int(N[i-1])+int(N[i])<=26:
            ans = ans + encode[i-1]
        encode.append(ans)
    print(encode[len(N)]%1000000)