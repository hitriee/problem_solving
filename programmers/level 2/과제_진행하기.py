# 241206
def calc_dif(time_str1, time_str2):
    hour1, minute1 = map(int, time_str1.split(':'))
    hour2, minute2 = map(int, time_str2.split(':'))
    return (hour2 - hour1) * 60 + minute2 - minute1

def solution(plans):
    plans.sort(key=lambda plan: plan[1])
    finished = []
    stopped = []
    
    for i in range(len(plans)-1):
        # 다음 시각 - 현재 시각 - 현재 과제 소요시간
        dif = calc_dif(plans[i][1], plans[i+1][1]) - int(plans[i][2])

        # 현재 과제 끝남
        if dif >= 0:
        
            finished.append(plans[i][0])
            if dif > 0:
                while stopped:
                    name, left = stopped.pop()
                    if left > dif:
                        stopped.append((name, left - dif))
                        break;
                    elif left == dif:
                        finished.append(name)
                        break;
                    else:
                        finished.append(name)
                        dif -= left
        else:
            stopped.append((plans[i][0], -dif))
    
    finished.append(plans[-1][0])
    
    for name, _ in stopped[::-1]:
        finished.append(name)
    
    return finished
