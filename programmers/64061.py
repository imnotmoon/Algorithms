# 2019 카카오 개발자 겨울 인턴십 - 크레인 인형뽑기

def solution(board, moves):
    cart = [0]
    answer = 0

    for i in range(len(moves)):
        ret = addCart(board, moves[i], cart)
        answer += ret
        # print(ret, cart)

    return answer


def addCart(board, handle, cart):
    for i in range(0, len(board[0])):
        if board[i][handle-1] > 0:
            if cart[-1] == board[i][handle-1]:
                cart.pop(-1)
                board[i][handle-1] = 0
                return 2
            else:
                cart.append(board[i][handle-1])
                board[i][handle-1] = 0
                return 0
    return 0


solution([[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [
         4, 2, 4, 4, 2], [3, 5, 1, 3, 1]], [1, 5, 3, 5, 1, 2, 1, 4])
