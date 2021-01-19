# # baekjoon 10815

_ = input()
my_cards = set(map(int, input().split()))
_ = input()
total_cards = list(map(int, input().split()))

for i in total_cards:
    if i in my_cards:
        print(1, end=" ")
    else :
        print(0, end=" ")