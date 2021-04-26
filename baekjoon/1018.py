import sys
input = sys.stdin.readline

chessWhite = ['WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW',
              'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW']
chessBlack = ['BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB',
              'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB']


def compare(i, j):
    currentBoard = [row[j:j+8] for row in board[i:i+8]]

    startBlack, startWhite = 0, 0
    for row in range(8):
        for col in range(8):
            if currentBoard[row][col] != chessWhite[row][col]:
                startWhite += 1
            if currentBoard[row][col] != chessBlack[row][col]:
                startBlack += 1
    return min(startBlack, startWhite)


n, m = map(int, input().split())
board = [input().strip() for _ in range(n)]

ret = 64
for i in range(n-8+1):
    for j in range(m-8+1):
        ret = min(ret, compare(i, j))

print(ret)
