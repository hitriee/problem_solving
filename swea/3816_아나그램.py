# 260402
# 60800 KB / 176 ms
def main():
    T = int(input())
    for tc in range(1, T+1):
        s1, s2 = input().split()
        n, m = len(s1), len(s2)
        is_anagram = False
        s1_alp, s2_alp = {}, {}
        removed_alp = ''
        cnt = 0
        for alp in s1:
            s1_alp[alp] = s1_alp.get(alp, 0) + 1

        for i in range(n-1):
            alp = s2[i]
            s2_alp[alp] = s2_alp.get(alp, 0) + 1


        for i in range(n-1, m):
            new_alp = s2[i]
            s2_alp[new_alp] = s2_alp.get(new_alp, 0) + 1

            if is_anagram:
                if new_alp == removed_alp:
                    cnt += 1
                else:
                    is_anagram = False
            else:
                for alp in s1_alp:
                    if s1_alp[alp] != s2_alp.get(alp, 0):
                        break
                else:
                    cnt += 1
                    is_anagram = True

            removed_alp = s2[i-n+1]
            s2_alp[removed_alp] -= 1

        print(f'#{tc} {cnt}')

main()




# 61184 KB / 129 ms
def main():
    T = int(input())
    a_num = ord('a')

    def alp_to_idx(alp):
        return ord(alp) - a_num

    for tc in range(1, T+1):
        s1, s2 = input().split()
        n, m = len(s1), len(s2)
        is_anagram = False
        s1_alp, s2_alp = [0] * 26, [0] * 26
        idx_arr = list(set(alp_to_idx(alp) for alp in s1))

        removed_idx = -1
        cnt = 0
        for alp in s1:
            idx = alp_to_idx(alp)
            s1_alp[idx] += 1

        for i in range(n-1):
            idx = alp_to_idx(s2[i])
            s2_alp[idx] += 1


        for i in range(n-1, m):
            new_idx = alp_to_idx(s2[i])
            s2_alp[new_idx] += 1

            if is_anagram:
                if new_idx == removed_idx:
                    cnt += 1
                else:
                    is_anagram = False
            else:
                for idx in idx_arr:
                    if s1_alp[idx] != s2_alp[idx]:
                        break
                else:
                    cnt += 1
                    is_anagram = True

            removed_idx = alp_to_idx(s2[i-n+1])
            s2_alp[removed_idx] -= 1

        print(f'#{tc} {cnt}')

main()