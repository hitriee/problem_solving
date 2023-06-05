#230604
# pypy3
def print_answer():
    from sys import stdin
    from collections import deque
    T = int(input())
    q = deque()
    visited = set()

    def bfs():
        while q:
            number, command = q.popleft()
            if number == A:
                print(command)
                break
            else:
                l, r = (number % 10) * 1000 + number // 10, (number % 1000) * 10 + number // 1000
                if l == A:
                    print('L' + command)
                    break
                elif r == A:
                    print('R' + command)
                    break
                else:
                    if l not in visited:
                        q.append((l, 'L' + command))
                    if r not in visited:
                        q.append((r, 'R' + command))

            if number % 2 == 0:
                half = number // 2
                for new_num in (half, half + 5000):
                    if new_num not in visited:
                        q.append((new_num, 'D' + command))
                        visited.add(new_num)

            s = number + 1 if number < 9999 else 0
            if s not in visited:
                q.append((s, 'S' + command))
                visited.add(s)

    for _ in range(T):
        A, B = map(int, stdin.readline().split())
        q.append((B, ''))
        visited.add(B)
        bfs()

        q.clear()
        visited.clear()
print_answer()