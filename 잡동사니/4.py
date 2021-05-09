def solution(n, start, end, roads, traps):    
    from collections import deque
    import sys
    import copy
    queue = deque()
    queue.append((start, 0, roads))
    result = sys.maxsize
    while queue:
        # time.sleep(1)
        currentNode, currentTime, currentRoads = queue.popleft()

        # 도착한 경우
        if currentNode == end:
            if result < currentTime:
                break
            result = currentTime
            break
        
        if currentNode in traps:
            # 현재 노드가 트랩인 경우 => 연결된 경로 거꾸로 수정
            print(currentRoads)
            for i in range(len(roads)):
                if currentRoads[i][0] == currentNode or currentRoads[i][1] == currentNode:
                    currentRoads[i][0], currentRoads[i][1] = currentRoads[i][1], currentRoads[i][0]
            print(currentRoads)
            print()
        # 가능한 모든 경로로 탐색
        for i in range(len(currentRoads)):
            if currentRoads[i][0] == currentNode:
                queue.append((currentRoads[i][1], currentTime+currentRoads[i][2], currentRoads))

    print(result)
    return result

# solution(3, 1, 3, [[1, 2, 2], [3, 2, 3]], [2])
solution(4, 1, 4, [[1, 2, 1], [3, 2, 1], [2, 4, 1]], [2, 3])