# 240502
def solution(enroll, referral, seller, amount):
    # 판매원 이름, 각 판매원을 참여시킨 다른 판매원, 판매원 이름, 판매 수량
    from math import ceil, floor

    n, m = len(enroll), len(seller)
    enr_to_i, enr_to_ref = {}, {}
    for i in range(n):
        person = enroll[i]
        enr_to_i[person] = i
        enr_to_ref[person] = referral[i]

    # 각 판매원에게 배분된 이익금의 총합 (enroll 순서대로)
    total_profit = [0] * n

    for i in range(m):
        person, profit = seller[i], amount[i] * 100
        while True:
            total_profit[enr_to_i[person]] += ceil(profit * 0.9)
            person = enr_to_ref[person]
            profit = floor(profit / 10)
            if profit == 0 or person == '-':
                break

    return total_profit

'''

'''

#
def solution(enroll, referral, seller, amount):
    # 판매원 이름, 각 판매원을 참여시킨 다른 판매원, 판매원 이름, 판매 수량
    from math import ceil, floor

    n, m = len(enroll), len(seller)
    enr_to_i, enr_to_ref = {}, {}
    for i in range(n):
        person = enroll[i]
        enr_to_i[person] = i
        enr_to_ref[person] = referral[i]

    # 각 판매원에게 배분된 이익금의 총합 (enroll 순서대로)
    total_profit = [0] * n

    for i in range(m):
        person, profit = seller[i], amount[i] * 100
        while True:
            total_profit[enr_to_i[person]] += ceil(profit * 0.9)
            person, profit = enr_to_ref[person], floor(profit / 10)
            if profit == 0 or person == '-':
                break

    return total_profit

'''
테스트 1 〉	통과 (0.03ms, 9.93MB)
테스트 2 〉	통과 (0.11ms, 10.3MB)
테스트 3 〉	통과 (0.05ms, 10.2MB)
테스트 4 〉	통과 (0.16ms, 10.2MB)
테스트 5 〉	통과 (1.37ms, 10.3MB)
테스트 6 〉	통과 (2.27ms, 12.7MB)
테스트 7 〉	통과 (2.58ms, 12.5MB)
테스트 8 〉	통과 (4.37ms, 12.4MB)
테스트 9 〉	통과 (19.15ms, 13.8MB)
테스트 10 〉	통과 (192.33ms, 21MB)
테스트 11 〉	통과 (157.38ms, 20.4MB)
테스트 12 〉	통과 (244.16ms, 20.6MB)
테스트 13 〉	통과 (154.02ms, 20.6MB)
'''