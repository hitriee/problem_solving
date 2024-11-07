# 241106
def main():
    word = input()
    word_cnt = 0
    limit = len(word)
    vowels = {'A', 'E', 'I', 'O', 'U'}

    # 단어 인덱스, 연속된 모음 개수, 연속된 자음 개수, 경우의 수, L 포함 여부
    def make_new_word(level, cnt1, cnt2, total_cnt, need_l):
        nonlocal word_cnt
        # 연속된 개수 판별
        if cnt1 == 3 or cnt2 == 3:
            return

        if level == limit:
            if need_l:
                word_cnt += total_cnt
            return

        alp = word[level]
        if alp != '_':
            if alp in vowels:
                make_new_word(level+1, cnt1+1, 0, total_cnt, need_l)
            else:
                make_new_word(level+1, 0, cnt2+1, total_cnt, need_l)
        else:
            make_new_word(level+1, cnt1+1, 0, total_cnt*5, need_l)
            make_new_word(level+1, 0, cnt2+1, total_cnt*20, need_l)
            make_new_word(level+1, 0, cnt2+1, total_cnt, True)


    make_new_word(0, 0, 0, 1, 'L' in word)

    return word_cnt

print(main())