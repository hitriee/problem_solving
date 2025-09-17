# 250917
# 32412 KB / 48ms
def main():
    N = int(input())
    target = list(map(int, input().split()))
    if sum(target) == 0:
        return 0

    min_cnt = 0
    cnt = {}
    for num in target:
        cnt[num] = cnt.get(num, 0) + 1

    keys = sorted(cnt)

    while True:
        new_keys = set()
        for key in keys:
            if key:
                value = cnt[key]
                if key % 2:
                    min_cnt += value
                cnt[key] = 0
                new_key = key//2
                cnt[new_key] = cnt.get(new_key, 0) + value
                new_keys.add(new_key)
        keys = sorted(new_keys)
        if keys == [0]:
            return min_cnt
        min_cnt += 1

print(main())


# 32412 KB / 32 ms
def main():
    _ = int(input())
    target = list(map(int, input().split()))
    if sum(target) == 0:
        return 0

    min_cnt = 0
    cnt = [0] * 1001
    keys = []
    for num in target:
        if cnt[num] == 0:
            keys.append(num)
        cnt[num] += 1

    keys.sort()

    while True:
        new_keys = set()
        for key in keys:
            if key:
                value = cnt[key]
                if key % 2:
                    min_cnt += value
                cnt[key] = 0
                new_key = key//2
                cnt[new_key] += value
                new_keys.add(new_key)
        keys = sorted(new_keys)
        if keys == [0]:
            return min_cnt
        min_cnt += 1

print(main())