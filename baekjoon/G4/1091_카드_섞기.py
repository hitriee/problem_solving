#230829
def cards_to_target():
    N = int(input())
    target = list(map(int, input().split()))
    method = list(map(int, input().split()))
    cards = [0, 1, 2] * (N//3)
    if cards == target:
        return 0

    initial_cards = cards[:]
    cnt = 0

    def shuffle(cards):
        new_cards = [0] * N
        for i in range(N):
            new_cards[i] = cards[method[i]]
        return new_cards

    while True:
        cards = shuffle(cards)
        cnt += 1
        if cards == initial_cards:
            return -1
        if cards == target:
            return cnt

print(cards_to_target())


#
def cards_to_target():
    N = int(input())
    target = list(map(int, input().split()))
    method = list(map(int, input().split()))
    cards = [0, 1, 2] * (N//3)
    if cards == target:
        return 0

    initial_cards = cards[:]
    cnt = 0

    def shuffle():
        nonlocal cards
        new_cards = [0] * N
        for i in range(N):
            new_cards[i] = cards[method[i]]
        cards = new_cards

    while True:
        shuffle()
        cnt += 1
        if cards == initial_cards:
            return -1
        if cards == target:
            return cnt

print(cards_to_target())