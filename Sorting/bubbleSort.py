# 옆에 있는 값과 비교해서 더 작은 값을 앞으로 보냄
# 구현하기에는 제일 쉬우나 효율성이 가장 떨어짐
# 1~10 / 1~9 / 1~8 .. 가장 큰 값이 맨 뒤로 이동
# 맨 뒤의 값은 정렬이 되었다고 가정한다. 실제로 그렇기도 하고.


def main() :
    array = [1, 10, 5, 8, 7, 6, 4, 3, 2, 9]
    for i in range(len(array)):
        for j in range(0, len(array)-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
        print(array)

if __name__ == "__main__" :
    main()

# 시간복잡도는 똑같이 O(n^2)
# 실제로 선택정렬보다도 훨씬 느리다.