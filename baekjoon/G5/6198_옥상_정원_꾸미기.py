# 250205
def main():
    from sys import stdin

    def int_input():
        return int(stdin.readline())

    total = 0
    N = int_input()
    heights = [int_input() for _ in range(N)]
    stack = [N-1]
    for i in range(N-2, -1, -1):
        peek = stack[-1]
        while heights[peek] < heights[i]:
            stack.pop()
            if stack:
                peek = stack[-1]
            else:
                total += N-1-i
                break
        else:
            total += peek - i - 1

        stack.append(i)

    return total

print(main())