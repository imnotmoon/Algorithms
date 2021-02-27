def main():
    p, n, h = map(int, input().split())
    reservation = dict()
    for i in range(p):
        reservation[i+1] = []

    for i in range(n):
        tmp = tuple(map(int, input().split()))
        if tmp[1] <= h:
            reservation[tmp[0]].append(tmp[1])

    for i in range(p):
        res = reservation[i+1]
        hour_for_each = h
        sorted_res = sorted(res)
        for j in sorted_res:
            if hour_for_each >= j:
                hour_for_each -= j
        print(i+1, (h - hour_for_each)*1000)


if __name__ == "__main__":
    main()
