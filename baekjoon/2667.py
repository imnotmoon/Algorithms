# 2020.08.30 04:32

def main() :
    n = int(input())
    house = []
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    for i in range(n):
        house.append(list(map(str, input())))
    
    # scenario 0. 같은 단지끼리 묶기 위해 numbering 변수 선언
    numbering = 0
    # scenario 1. for 루프 두개로 전체 그래프를 탐색
    queue = []
    apartments = []
    for i in range(n):
        for j in range(n):
            # scenario 2. 다음 칸에 대해서도 똑같은 작업 수행
            if house[i][j] == "1" :
                queue.append((i,j))
                house[i][j] = "0"     # visited
                # scenario 1.1. scenario 1에서 시작한 칸에 대한 모든 탐색이 끝나면 numbering++
                numbering += 1

                # scenario 1.2. 각 칸마다 상하좌우 탐색 - BFS
                count = 1
                while(len(queue) > 0) :
                    # print(queue)
                    ii, jj = queue[0]
                    queue.pop(0)
                    for k in range(4):
                        x = dx[k]
                        y = dy[k]
                        if ii+x < n and ii+x >= 0 and jj+y < n and jj+y>= 0 :
                            if house[ii+x][jj+y] == "1" :
                                queue.append((ii+x, jj+y))
                                count += 1
                                house[ii+x][jj+y] = "0"
                apartments.append(count)

    print(numbering)
    apartments = sorted(apartments)
    for num in apartments :
        print(num)

if __name__ == "__main__":
    main()