# baekjoon 1149 다시풀기

n = int(input())
house = []
for i in range(n):
    house.append(list(map(int, input().split())))

red, green, blue = [house[0][0]], [house[0][1]], [house[0][2]]
for i in range(1, n):
    red.append(min(green[i-1], blue[i-1])+house[i][0])
    green.append(min(red[i-1], blue[i-1])+house[i][1])
    blue.append(min(red[i-1], green[i-1])+house[i][2])

print(min(red[i], green[i], blue[i]))
