# 선택정렬 : 가장 작은것을 선택해서 제일 앞으로 보냄
# 하나 선택해서 맨 앞으로 보내고 
# 두번째부터 끝까지 중에서 가장 작은것을 골라 맨 앞의 원소와 교체

def main() :
    array = [1, 10, 5, 8, 7, 6, 4, 3, 2, 9]
    index = 0
    for i in range(len(array)):
        min = 9999      # 항상 최소값을 선택해야 해서 초기화는 아무거나 큰 수
        for j in range(i, len(array)):
            if min > array[j]:
                min = array[j]
                index = j
        # swap
        array[i], array[index] = array[index], array[i]
        print(array)


if __name__ == "__main__":
    main()

# 시간복잡도 O(n^2)
# 10 + 9 + 8 + ... + 1
