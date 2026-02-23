# 260223
# 35508 KB / 648 ms
def main():
    from sys import stdin
    from heapq import heappush, heappop, heapify

    new_input = stdin.readline
    div_num = int(1e9)+7

    T = int(new_input())
    for _ in range(T):
        n = int(new_input())
        energy_arr = list(map(int, new_input().split()))
        total = 1
        heapify(energy_arr)

        while True:
            if n == 1:
                break
            one = heappop(energy_arr)
            another = heappop(energy_arr)

            multiple = one * another
            heappush(energy_arr, multiple)
            total = (total * multiple) % div_num
            n -= 1

        print(total)

main()




# 35508 KB / 692 ms
def main():
    from sys import stdin
    from heapq import heappush, heappop, heapify

    new_input = stdin.readline
    div_num = int(1e9)+7

    T = int(new_input())
    for _ in range(T):
        n = int(new_input())
        energy_arr = list(map(int, new_input().split()))
        total = 1
        heapify(energy_arr)

        while n > 1:
            one = heappop(energy_arr)
            another = heappop(energy_arr)

            multiple = one * another
            heappush(energy_arr, multiple)
            total = (total * multiple) % div_num
            n -= 1

        print(total)

main()








# 35508 KB / 672 ms
def main():
    from sys import stdin
    from heapq import heappush, heappop, heapify

    new_input = stdin.readline
    div_num = int(1e9)+7

    T = int(new_input())
    for _ in range(T):
        n = int(new_input())
        energy_arr = list(map(int, new_input().split()))
        total = 1
        heapify(energy_arr)

        for _ in range(n-1):
            one = heappop(energy_arr)
            another = heappop(energy_arr)

            multiple = one * another
            heappush(energy_arr, multiple)
            total = (total * multiple) % div_num

        print(total)

main()