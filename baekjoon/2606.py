# 2020.08.30 03:49 정답


def main() :
    n = int(input())
    pair = int(input())
    network = [list() for _ in range(n+1)]
    for i in range(pair) :
        tmp = list(map(int, input().split()))
        network[tmp[0]].append(tmp[1])
        network[tmp[1]].append(tmp[0])

    # print(network[1:])
    
    # bfs
    queue = list()
    infected = [False for _ in range(n+1)]
    queue.append(1)
    infected[1] = True

    while(len(queue) > 0) :
        current = queue[0]
        queue.pop(0)
        for com in network[current]:
            if infected[com]:
                continue
            else :
                infected[com] = True
                queue.append(com)

    count = 0
    for com in infected:
        if com:
            count += 1
    # print(infected[1:])
    print(count-1)

if __name__ == "__main__":
    main()