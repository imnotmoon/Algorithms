# 백준 1138 201020

def countBlank(to) :
    blank = 0   # 빈칸 갯수
    for i in range(n) :
        if to == 0 :
            if result[i] == 0 : 
                return i
        else :
            if result[i] == 0 :
                blank += 1
                if blank == to+1 :
                    return i
        


n = int(input())
height = list(map(int, input().split()))
result = [0]*n
# 자기 앞에 있는 빈칸의 수가 height가 되도록
for i in range(n) :
    pos = countBlank(height[i])
    result[pos] = i+1

res = ""
for i in range(n) :
    res = res + str(result[i]) + " "

print(res.rstrip())


