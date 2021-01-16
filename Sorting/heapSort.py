# HeapSort
# 병합정렬, 퀵정렬만큼 빠른 정렬 알고리즘
# 실제로 고급 프로그래밍 기법으로 갈수록 Heap의 개념이 자주 등장
# 힙 트리 구조를 이용하는 정렬 방법

# 이진트리
# 자식이 최대 2인 트리 자료구조
# 데이터가 서로 연결되어있다는 것

# 완전이진트리
# 데이터가 왼쪽 / 오른쪽으로 차근차근 들어감

# 힙
# 최소값이나 최대값을 빠르게 찾아내기 위해 완전이진트리를 기반으로 하는 트리
# 최대힙 : 부모 > 자식. 
# 여러 형태가 나올 수 있다

# 특정 노드 때문에 최대힙이 붕괴되는 일이 생김
# 그 노드의 자식중에서 자기보다 더 큰값과 바꿈. => Heapify Algorithm
# 아래쪽으로 내려가며 최대힙을 유지하는지 반복하면서 검사
# Heapify를 수행하는 시간은 트리의 높이와 같기 때문에 logN
# 모든 정점에 대해서 Heapify를 수행하면 NlogN
# 실제로는 시간복잡도가 NlogN의 절반이다. => 1/2 NlogN. (리프노드는 볼 필요가 없어서)
# 이때 1/2 N 보다 logN이 작으므로 시간복잡도는 O(N)

# 힙을 배열로 표현해서 구현
# 힙의 루트 노드 값은 해당 트리에서 최대값임을 이용
# 맨 위와 맨 마지막 값을 바꾸고 Heapify
# 맨 위와 맨 마지막-1 값을 바꾸고 Heapify
# ...
# 정렬 끝

# Heapify : logN. 이걸 N번 반복

heap = [7, 6, 5, 8, 3, 5, 1, 6]
number = len(heap)

def main() :
    # scenario1. 전체 트리 구조를 힙 구조로 바꿈
    for i in range(number):
        c = i
        root = int((c-1)/2)
        if heap[root] < heap[c] :
            heap[root], heap[c] = heap[c], heap[root]
        c = root
        while(c != 0) :
            root = int((c-1)/2)
            if heap[root] < heap[c] :
                heap[root], heap[c] = heap[c], heap[root]
            c = root
        
    # scenario2. 맨 끝에서부터 크기를 하나씩 줄여가며 힙 정렬
    for i in range(number):
        # scenario2-1. 맨 위와 맨 마지막 값을 교체
        last = number-i-1
        heap[0], heap[last] = heap[last], heap[0]

        # scenario2-2. Heapify
        
        root = 0
        c = 1       # 현재 보고있는 노드
        # 두 자식 중에 더 큰 값을 찾기
        if heap[c] < heap[c+1] and c < last:
            c += 1
        # 루트보다 자식이 더 크다면 교환
        if heap[root] < heap[c]:
            heap[root], heap[c] = heap[c], heap[root]
        
        while(c < i) :
            c = 2*root + 1
            if c < last-1 and heap[c] < heap[c+1] :
                c += 1
            # 루트보다 자식이 더 크다면 교환
            if heap[root] > heap[c]:
                heap[root], heap[c] = heap[c], heap[root]
            root = c

    print(heap)

if __name__ == "__main__":
    main()
