# baekjoon 21315
import math
import sys
input = sys.stdin.readline

N = int(input())
cards = list(range(1, N+1))
cards_to = list(map(int, input().split()))

def shuffle(cards, k):
  new_cards = cards[len(cards) - 2**k:] + cards[:len(cards) - 2**k]
  t = k
  for i in range(2, k+2):
    new_cards[:2**t] = new_cards[2**(k-i+1):2**t] + new_cards[:2**(k-i+1)]
    t = t - i + 1
  return new_cards

for i in range(1, math.floor(math.log2(N))+1):
  for j in range(1, math.floor(math.log2(N))+1):
    new_cards = shuffle(cards, i)
    new_cards = shuffle(new_cards, j)
    print(new_cards)
    if new_cards == cards_to: 
      print(i, j)
      exit(0)