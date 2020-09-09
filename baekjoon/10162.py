# 10162

def main() :
    T = int(input())
    click = [0,0,0]
    btn = [300, 60, 10]

    if T%10 != 0 : 
        print(-1)
        return
    for time in btn :
        if T >= time : 
            click[btn.index(time)] += int(T/time)
            T -= int(T/time) * time
    print(click[0], click[1], click[2])

if __name__ == "__main__":
    main()