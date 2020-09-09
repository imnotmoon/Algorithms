# 20.09.07 22:15

# 행 리스트를 따로 만들려했는데 그러면 오히려 시간이 더걸린다
# 그냥 인덱스로 비교하는게 더 나음
# append가 0으로 초기화하고 값 바꾸는거보다 오래걸린다

n = int(input())
students = [list(map(int, input().split())) for _ in range(n)]

count = [0]*n
for i in range(len(students)) :
    # 같은반이었던적이 있었던 친구는 True, 아니면 False
    friend = [False for _ in range(n)]
    for j in range(len(students[i])) :
        # 행 고정시키기 위해서 student 사용
        for student in range(n) :
            if student == i :
                continue
            if students[student][j] == students[i][j] :
                friend[student] = True
    count[i] = sum(friend)
    # print(i+1, "th student : ", friend)

print(count.index(max(count))+1)


