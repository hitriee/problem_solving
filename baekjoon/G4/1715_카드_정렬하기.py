#230613
from sys import stdin
from heapq import heappush, heappop, heapify

def to_int(): return int(stdin.readline())

N = to_int()
cards = [to_int() for _ in range(N)]
heapify(cards)
total_cnt = 0
for _ in range(len(cards) - 1):
    card1 = heappop(cards)
    card2 = heappop(cards)
    cnt = card1+card2
    total_cnt += cnt
    heappush(cards, cnt)
print(total_cnt)


#
def sort_cards():
    from sys import stdin
    from heapq import heappush, heappop, heapify

    def to_int(): return int(stdin.readline())

    N = to_int()
    cards = [to_int() for _ in range(N)]
    heapify(cards)
    total_cnt = 0
    for _ in range(len(cards) - 1):
        card1 = heappop(cards)
        card2 = heappop(cards)
        cnt = card1+card2
        total_cnt += cnt
        heappush(cards, cnt)

    return total_cnt

print(sort_cards())

#
def sort_cards():
    from sys import stdin
    from heapq import heappush, heappop, heapify

    def to_int(): return int(stdin.readline())

    N = to_int()
    cards = [to_int() for _ in range(N)]
    heapify(cards)
    total_cnt = 0
    for _ in range(len(cards) - 1):
        card_list = [heappop(cards) for _ in range(2)]
        cnt = sum(card_list)
        total_cnt += cnt
        heappush(cards, cnt)

    return total_cnt

print(sort_cards())

