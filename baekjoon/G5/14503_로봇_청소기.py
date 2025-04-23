# 250423
# 32412 KB / 40 ms
def main():

    N, M = map(int, input().split())
    r, c, d = map(int, input().split())

    arr = [input().split() for _ in range(N)]
    dr, dc = (-1, 0, 1, 0), (0, 1, 0, -1)
    cnt = 1

    while True:
        # 청소
        arr[r][c] = ''
        # 청소되지 않은 빈 칸 찾기
        for _ in range(4):
            d = (d - 1) % 4
            nr, nc = r+dr[d], c+dc[d]
            if arr[nr][nc] == '0':
                # 청소되지 않았을 경우 한 칸 전진
                r, c = nr, nc
                cnt += 1
                break
        else:
            # 청소되지 않은 빈 칸이 없는 경우, 후진
            nr, nc = r-dr[d], c-dc[d]
            val = arr[nr][nc]
            if val == '1':
                return cnt

            r, c = nr, nc
            if val == '0':
                cnt += 1


print(main())