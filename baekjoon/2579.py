def main() :
    n = int(input())
    stairs = []
    for i in range(n) :
        stairs.append(int(input()))
    if n == 1 :
        print(stairs[0])
        return

    plusOne = [0 for _ in range(n)]
    plusOne[0] = stairs[0]
    plusOne[1] = stairs[1] + stairs[0]
    plusTwo = [0 for _ in range(n)]
    plusTwo[0] = -1
    plusTwo[1] = stairs[1]

    for i in range(n) :
        if i == 0 or i == 1 :
            continue
        stair = stairs[i]
        plusOne[i] = plusTwo[i-1] + stair
        plusTwo[i] = max(plusOne[i-2], plusTwo[i-2]) + stair

    print(max(plusOne[n-1], plusTwo[n-1]))


if __name__ == "__main__":
    main()