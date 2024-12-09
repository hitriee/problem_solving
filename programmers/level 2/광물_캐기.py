# 241209
def solution(picks, minerals):
    N = sum(picks)
    M = min(len(minerals), 5 * N)

    min_val = 25 * M
    name_to_idx = {
        'diamond' : 0,
        'iron' : 1,
        'stone' : 2,
    }
    
    table = [
        [1, 1, 1],
        [5, 1, 1],
        [25, 5, 1],
    ]
    
    def find_val(i, j):
        return table[i][name_to_idx[minerals[j]]]
    
    def dfs(level, pick, val):
        nonlocal min_val
        
        if val >= min_val:
            return
        
        if level == M:
            min_val = val
            return
        
        if level % 5 == 0:
            for i in range(3):
                if picks[i]:
                    picks[i] -= 1
                    dfs(level+1, i, val + find_val(i, level))
                    picks[i] += 1
                    
        else:
            dfs(level+1, pick, val + find_val(pick, level))
    
    dfs(0, 0, 0)
    
        
    return min_val
