# fibonacci for python
# 0 1 1 2 3 5 8 13 21 34 ...

fib = [0,1,1]

n = 0

while(n>=0 & n<91) :
    n = int(input('input number : '))
    
    if(n>1) :
        for i in range(n) :
            fib[i%3] = fib[(i+1)%3] + fib[(i+2)%3]
    else :
        break
    break

print('fib ', n, 'is ', fib[n%3])
