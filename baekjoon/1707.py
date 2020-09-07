#  20.09.07. 시간초과
edges = []
links = []

def bfs(node, i) :
    global edges, links
    edge = links[i]
    ## edge = [[1, 2], [2, 3], [3, 4], [4, 2]]
    queue = []
    queue.append(1)
    # scenario 1. fill blue/red at each level of the graph
    color = [-1] * (node+1)
    color[1] = 1    # 1 : red / 0 : blue / -1 : 미적용
    while queue :
        front = queue.pop(-1)
        for e in edge :
            if e[0] == front : 
                ## 같은 그룹 내에서 연결된 경우
                if color[front] == color[e[1]] : 
                    # print("!!!!!", front, e[1], "!!!!!")
                    return "No"
                if color[front] == 1 and color[e[1]] == -1:
                    color[e[1]] = 0
                elif color[front] == 0 and color[e[1]] == -1 :
                    color[e[1]] = 1
                else : continue       ## 이미 방문했던건 방문 다시 안함
                queue.append(e[1])
            elif e[1] == front:
                ## 같은 그룹 내에서 연결된 경우
                if color[front] == color[e[0]] :
                    # print("!!!!!", front, e[0], "!!!!!")
                    return "No"
                if color[front] == 1 and color[e[0]] == -1 :
                    color[e[0]] = 0
                elif color[front] == 0 and color[e[0]] == -1 :
                    color[e[0]] = 1
                else : continue       ## 이미 방문했던건 방문 다시 안함
                queue.append(e[0])
    # scenario 2. find edges which links 2 nodes that in same group
    return "Yes"


k = int(input())
nodes = []

for i in range(k) :
    node, edge = map(int, input().split())
    nodes.append(node)
    edges.append(edge)
    array = []
    for j in range(edge) :
        array.append(list(map(int, input().split())))
    links.append(array)

for i in range(k) :
    print(bfs(nodes[i], i))
