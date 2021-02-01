x, y = tuple(map(int, input().split()))
z = int(y*100/x)

left, right = 0, 1000000001
mid = int((left+right)/2)
ret = -1
prev_mid = right

while(left < right):
    if prev_mid == mid :
        break
    new_z = int((y+mid)*100/(x+mid))
    before_new_z = int((y+mid-1)*100/(x+mid-1))
    if before_new_z == z and new_z > z:
        ret = mid
        break
    prev_mid = mid
    if new_z > z:
        right = mid
        mid = int((left+right)/2)
    elif new_z == z:
        left = mid
        mid = int((left+right)/2)
    
print(ret)