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
            person, profit = enr_to_ref[person], floor(profit/10)
            if profit == 0 or person == '-':
                break
    
    return total_profit


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
            person, profit = enr_to_ref[person], floor(profit/10)
            if profit == 0 or person == '-':
                break
    
    return total_profit
