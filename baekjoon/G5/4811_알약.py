# 241021
# 31120 KB / 872 ms
def main():
    from sys import stdin

    while True:
        N = int(stdin.readline())
        if N == 0:
            return
        cnt = [[0] * (N+1) for _ in range(N+1)]
        new_cnt = [[0] * (N+1) for _ in range(N+1)]
        cnt[N-1][1] = 1
        
        for _ in range(2*N-1):
            for i in range(N+1):
                for j in range(N+1):
                    if cnt[i][j]:
                        if i:
                            new_cnt[i-1][j+1] += cnt[i][j]
                        if j:
                            new_cnt[i][j-1] += cnt[i][j]
    
            for i in range(N+1):
                for j in range(N+1):
                    cnt[i][j], new_cnt[i][j] = new_cnt[i][j], 0


        print(cnt[0][0])

main()



# 31120 KB / 740 ms
def main():
    from sys import stdin

    while True:
        N = int(stdin.readline())
        if N == 0:
            return
        cnt = [[0] * (N+1) for _ in range(N+1)]
        cnt[N-1][1] = 1
        for _ in range(2*N-1):
            for i in range(N+1):
                for j in range(N+1):
                    if cnt[i][j]:
                        if i:
                            cnt[i-1][j+1] += cnt[i][j]
                        if j:
                            cnt[i][j-1] += cnt[i][j]

        print(cnt[0][0])

main()


# 31120 KB / 696 ms
def main():
    from sys import stdin

    while True:
        N = int(stdin.readline())
        if N == 0:
            return
        cnt = [[0] * (N+1) for _ in range(N+1)]
        cnt[N-1][1] = 1
        for _ in range(2*N-1):
            for i in range(N+1):
                for j in range(N+1):
                    val = cnt[i][j] 
                    if val:
                        if i:
                            cnt[i-1][j+1] += val
                        if j:
                            cnt[i][j-1] += val

        print(cnt[0][0])

main()



# 31120 KB / 752 ms
def main():
    while True:
        N = int(input())
        if N == 0:
            return
        cnt = [[0] * (N+1) for _ in range(N+1)]
        cnt[N-1][1] = 1
        for _ in range(2*N-1):
            for i in range(N+1):
                for j in range(N+1):
                    val = cnt[i][j] 
                    if val:
                        if i:
                            cnt[i-1][j+1] += val
                        if j:
                            cnt[i][j-1] += val

        print(cnt[0][0])


main()




# 34044 KB / 104 ms
def main():
    from sys import stdin
    from collections import deque

    while True:
        N = int(stdin.readline())
        if N == 0:
            return
        cnt = [[0] * (N+1) for _ in range(N+1)]
        cnt[N-1][1] = 1
        q = deque()
        q.append((N-1, 1))
        for _ in range(2*N-1):
            next_temp = set()
            while q:
                i, j = q.popleft()
                val = cnt[i][j]
                if val:
                    if i:
                        cnt[i-1][j+1] += val
                        next_temp.add((i-1, j+1))
                    if j:
                        cnt[i][j-1] += val
                        next_temp.add((i, j-1))
            q = deque(next_temp)

        print(cnt[0][0])

main()



# 34044 KB / 100 ms
def main():
    from sys import stdin
    from collections import deque

    while True:
        N = int(stdin.readline())
        if N == 0:
            return
        cnt = [[0] * (N+1) for _ in range(N+1)]
        cnt[N-1][1] = 1
        q = deque()
        q.append((N-1, 1))
        
        for _ in range(2*N-1):
            next_temp = set()
            while q:
                i, j = q.popleft()
                val = cnt[i][j]
                if i:
                    cnt[i-1][j+1] += val
                    next_temp.add((i-1, j+1))
                if j:
                    cnt[i][j-1] += val
                    next_temp.add((i, j-1))
            
            q = deque(next_temp)

        print(cnt[0][0])

main()
