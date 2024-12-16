# 241216
# 32412 KB / 36 ms
def main():
    N = int(input())
    final_cards = list(map(int, input().split()))
    num = 4
    for limit in range(2, N):
        if num >= N:
            break
        num *= 2

    def mix_cards(cards, K, num):
        cards = cards[N-num:] + cards[:N-num]
        for k in range(K, -1, -1):
            half = num // 2
            cards = cards[half:num] + cards[:half] + cards[num:]
            num = half
        return cards

    num1 = 2
    for i in range(1, limit):
        result1 = mix_cards(list(range(1, N+1)), i, num1)
        num2 = 2
        for j in range(1, limit):
            result2 = mix_cards(result1, j, num2)
            if result2 == final_cards:
                return f'{i} {j}'
            num2 *= 2
        num1 *= 2

print(main())