# 2020.08.30 03:49 정답


def main() :
    n = int(input())
    pair = int(input())
    network = [list() for _ in range(n+1)]
    for i in range(pair) :
        tmp = list(map(int, input().split()))
        # 반대쪽 경우도 경로에 추가
        network[tmp[0]].append(tmp[1])
        network[tmp[1]].append(tmp[0])
    
    # bfs
    queue = list()
    # 처음엔 아무것도 감염되지 않음
    infected = [False for _ in range(n+1)]
    queue.append(1)     # 1번 컴퓨터 감염
    infected[1] = True

    while queue :
        current = queue[0]  # 큐의 맨 앞의 컴퓨터가 감염된거
        queue.pop(0)
        for com in network[current]:
            if infected[com]:   # 감염된 경우를 또 방문
                continue
            else :
                infected[com] = True
                queue.append(com)

    # 감염된 컴퓨터 수
    count = 0
    for com in infected:
        if com:
            count += 1
    # print(infected[1:])
    print(count-1)

if __name__ == "__main__":
    main()