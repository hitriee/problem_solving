# 240503
def solution(order):
    # 택배 기사님이 원하는 상자 순서
    from collections import deque
    
    n, cnt = len(order), 0
    one, another = deque(range(1, n+1)), []
    
    for num in order:
        if one and another:
            if one[0] == num:
                one.popleft()
            elif another[-1] == num:
                another.pop()
            else:
                while one:
                    temp = one.popleft()
                    if temp == num:
                        break
                    another.append(temp)
                else:
                    break
        elif one:
            while one:
                temp = one.popleft()
                if temp == num:
                    break
                another.append(temp)
            else:
                break
        elif another[-1] == num:
            another.pop()
        else:
            break
        
        cnt += 1
    
    return cnt

'''
테스트 1 〉	통과 (16.79ms, 20.5MB)
테스트 2 〉	통과 (75.07ms, 56.5MB)
테스트 3 〉	통과 (105.27ms, 70.4MB)
테스트 4 〉	통과 (67.75ms, 52.5MB)
테스트 5 〉	통과 (147.41ms, 103MB)
테스트 6 〉	통과 (45.16ms, 26.8MB)
테스트 7 〉	통과 (199.63ms, 75.7MB)
테스트 8 〉	통과 (9.52ms, 13.3MB)
테스트 9 〉	통과 (126.41ms, 55.4MB)
테스트 10 〉	통과 (211.61ms, 87.7MB)
'''



#
def solution(order):
    # 택배 기사님이 원하는 상자 순서
    from collections import deque
    
    n, cnt = len(order), 0
    one, another = deque(range(1, n+1)), []
    
    for num in order:
        if another and another[-1] == num:
            another.pop()
        elif one:
            if one[0] == num:
                one.popleft()
            else:
                while one:
                    temp = one.popleft()
                    if temp == num:
                        break
                    another.append(temp)
                else:
                    break
            
        else:
            break
        
        cnt += 1
    
    return cnt

'''
테스트 1 〉	통과 (32.37ms, 20.6MB)
테스트 2 〉	통과 (92.94ms, 56.6MB)
테스트 3 〉	통과 (103.78ms, 70.6MB)
테스트 4 〉	통과 (84.44ms, 52.6MB)
테스트 5 〉	통과 (172.60ms, 103MB)
테스트 6 〉	통과 (51.02ms, 26.8MB)
테스트 7 〉	통과 (198.06ms, 75.7MB)
테스트 8 〉	통과 (10.40ms, 13.3MB)
테스트 9 〉	통과 (168.06ms, 55.4MB)
테스트 10 〉	통과 (230.39ms, 87.6MB)
'''


#
def solution(order):
    # 택배 기사님이 원하는 상자 순서
    from collections import deque
    
    n, cnt = len(order), 0
    one, another = deque(range(1, n+1)), []
    
    for num in order:
        if another and another[-1] == num:
            another.pop()
        elif not one:
            break
        elif one[0] == num:
            one.popleft()
        else:
            while one:
                temp = one.popleft()
                if temp == num:
                    break
                another.append(temp)
            else:
                break
        
        cnt += 1
    
    return cnt


'''
테스트 1 〉	통과 (24.78ms, 20.5MB)
테스트 2 〉	통과 (78.16ms, 56.6MB)
테스트 3 〉	통과 (109.39ms, 70.5MB)
테스트 4 〉	통과 (107.16ms, 52.4MB)
테스트 5 〉	통과 (199.24ms, 103MB)
테스트 6 〉	통과 (47.43ms, 26.7MB)
테스트 7 〉	통과 (199.60ms, 75.6MB)
테스트 8 〉	통과 (10.40ms, 13.4MB)
테스트 9 〉	통과 (129.87ms, 55.2MB)
테스트 10 〉	통과 (229.04ms, 87.7MB)
'''
