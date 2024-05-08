# 240508
def solution(keymap, targets):
    min_tap_total = []
    min_tap = {}
    for rule in keymap:
        n = len(rule)
        for i in range(n):
            alp = rule[i]
            min_tap[alp] = min(min_tap.get(alp, 100), i+1)
    
    for target in targets:
        cnt = 0
        for alp in target:
            if min_tap.get(alp):
                cnt += min_tap[alp]
            else:
                cnt = -1
                break
                
        min_tap_total.append(cnt)
    return min_tap_total
