# baekjoon 18222

def find(num):
    if num == 0 : return 0
    elif num == 1 : return 1
    elif num % 2 == 1 : return 1 - find(num // 2)
    else : return find(num//2)

print(find(int(input())-1))