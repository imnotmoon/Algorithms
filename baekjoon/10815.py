# # baekjoon 10815

# N = int(input())
# my_cards = list(map(int, input().split()))
# M = int(input())
# total_cards = list(map(int, input().split()))

# sorted_my_cards = sorted(my_cards)
# sorted_total_cards = sorted([[total_cards[i], i] for i in range(len(total_cards))])

# i, j = 0, 0
# check = []
# while(i < N and j < M) :
#     if sorted_my_cards[i] == sorted_total_cards[j][0]:
#         sorted_total_cards[j][0] = 1
#         i += 1
#         j += 1
#     elif sorted_my_cards[i] < sorted_total_cards[j][0] and i < N :
#         i += 1
#     elif sorted_my_cards[i] > sorted_total_cards[j][0] and j < M :
#         sorted_total_cards[j][0] = 0
#         j += 1

# chk = sorted(sorted_total_cards, key=lambda item: item[1])
# # print(chk)

# result = ""
# for idx in range(len(total_cards)) :
#     if chk[idx][0] == 1:
#         result += "1"
#     elif chk[idx][0] == 0:
#         result += "0"
    
#     if idx < len(total_cards)-1 :
#         result += " "

# print(result)

# # (값, 정렬전 인덱스) -> 정렬 -> 위에꺼처럼
# # -> 정렬전 인덱스로 정렬 -> for 루프 돌면서 스트링 조합

_ = input()
my_cards = set(map(int, input().split()))
_ = input()
total_cards = list(map(int, input().split()))

for i in total_cards:
    if i in my_cards:
        print(1, end=" ")
    else :
        print(0, end=" ")