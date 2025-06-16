// 250616
function calcDif(time1, hour2, minute2) {
    const [hour1, minute1] = [Math.floor(timelog/100), timelog%100]
    return (hour1 - hour2) * 60 + (minute1 - minute2)
}

function solution(schedules, timelogs, startday) {
    // 출근 희망 시각, 실제 출근 시각, 이벤트 시작 요일
    const n = schedules.length
    let headcount = 0
    for (let i = 0; i < n; i += 1) {
        const [hour, minute] = [Math.floor(schedules[i]/100), schedules[i]%100]
        let isSimilar = true
        let day = startday
        for (timelog of timelogs[i]) {
            if (day >= 6) {
                day = day === 6 ? 7 : 1
                continue
            }
            if (calcDif(timelog, hour, minute) > 10) {
                isSimilar = false
                break
            }
            day += 1
        }

        if (isSimilar) {
            headcount += 1
        }

    }


    return headcount
}

/*
정확성  테스트
테스트 1 〉	통과 (0.11ms, 33.5MB)
테스트 2 〉	통과 (0.18ms, 33.5MB)
테스트 3 〉	통과 (0.11ms, 33.4MB)
테스트 4 〉	통과 (0.11ms, 33.5MB)
테스트 5 〉	통과 (0.20ms, 33.4MB)
테스트 6 〉	통과 (0.10ms, 33.5MB)
테스트 7 〉	통과 (2.95ms, 36.9MB)
테스트 8 〉	통과 (3.50ms, 36.9MB)
테스트 9 〉	통과 (3.72ms, 36.9MB)
테스트 10 〉	통과 (4.88ms, 36.9MB)
테스트 11 〉	통과 (3.45ms, 36.9MB)
테스트 12 〉	통과 (3.25ms, 36.9MB)
테스트 13 〉	통과 (3.13ms, 36.9MB)
테스트 14 〉	통과 (3.00ms, 36.9MB)
테스트 15 〉	통과 (5.00ms, 36.9MB)
테스트 16 〉	통과 (4.68ms, 37MB)
테스트 17 〉	통과 (3.07ms, 36.9MB)
테스트 18 〉	통과 (3.99ms, 36.9MB)
테스트 19 〉	통과 (3.56ms, 37MB)
테스트 20 〉	통과 (2.99ms, 37MB)
테스트 21 〉	통과 (2.94ms, 37MB)
테스트 22 〉	통과 (3.59ms, 36.9MB)
테스트 23 〉	통과 (3.15ms, 37MB)
테스트 24 〉	통과 (3.06ms, 37MB)
테스트 25 〉	통과 (0.36ms, 33.4MB)
테스트 26 〉	통과 (0.41ms, 33.5MB)
테스트 27 〉	통과 (0.44ms, 33.4MB)
테스트 28 〉	통과 (2.23ms, 34.4MB)
테스트 29 〉	통과 (1.98ms, 34.3MB)
테스트 30 〉	통과 (1.05ms, 33.9MB)
테스트 31 〉	통과 (1.45ms, 34.4MB)
테스트 32 〉	통과 (1.42ms, 34.3MB)
테스트 33 〉	통과 (3.69ms, 36.9MB)
테스트 34 〉	통과 (4.98ms, 36.9MB)
테스트 35 〉	통과 (3.10ms, 36.9MB)
테스트 36 〉	통과 (3.20ms, 36.9MB)
테스트 37 〉	통과 (2.10ms, 36.6MB)
테스트 38 〉	통과 (2.36ms, 34.6MB)
테스트 39 〉	통과 (5.18ms, 36.9MB)
테스트 40 〉	통과 (3.12ms, 36.9MB)
테스트 41 〉	통과 (2.99ms, 36.9MB)
테스트 42 〉	통과 (3.10ms, 36.8MB)
*/



//
function calcDif(time1, hour2, minute2) {
    const [hour1, minute1] = [Math.floor(timelog/100), timelog%100]
    return hour1 >= hour2 ? (hour1 - hour2) * 60 + (minute1 - minute2) : -1
}

function solution(schedules, timelogs, startday) {
    // 출근 희망 시각, 실제 출근 시각, 이벤트 시작 요일
    const n = schedules.length
    let headcount = 0
    for (let i = 0; i < n; i += 1) {
        const [hour, minute] = [Math.floor(schedules[i]/100), schedules[i]%100]
        let isSimilar = true
        let day = startday
        for (timelog of timelogs[i]) {
            if (day >= 6) {
                day = day === 6 ? 7 : 1
                continue
            }
            if (calcDif(timelog, hour, minute) > 10) {
                isSimilar = false
                break
            }
            day += 1
        }

        if (isSimilar) {
            headcount += 1
        }

    }


    return headcount
}

/*
정확성  테스트
테스트 1 〉	통과 (0.17ms, 33.3MB)
테스트 2 〉	통과 (0.18ms, 33MB)
테스트 3 〉	통과 (0.11ms, 33.4MB)
테스트 4 〉	통과 (0.11ms, 33.1MB)
테스트 5 〉	통과 (0.11ms, 33.4MB)
테스트 6 〉	통과 (0.10ms, 33.3MB)
테스트 7 〉	통과 (26.48ms, 37.6MB)
테스트 8 〉	통과 (26.06ms, 37.7MB)
테스트 9 〉	통과 (23.82ms, 37.5MB)
테스트 10 〉	통과 (21.42ms, 37.5MB)
테스트 11 〉	통과 (2.96ms, 36.9MB)
테스트 12 〉	통과 (3.68ms, 36.9MB)
테스트 13 〉	통과 (3.00ms, 37MB)
테스트 14 〉	통과 (25.12ms, 37.6MB)
테스트 15 〉	통과 (2.95ms, 36.9MB)
테스트 16 〉	통과 (2.92ms, 36.9MB)
테스트 17 〉	통과 (19.44ms, 37.6MB)
테스트 18 〉	통과 (3.09ms, 36.8MB)
테스트 19 〉	통과 (3.16ms, 36.9MB)
테스트 20 〉	통과 (2.96ms, 36.8MB)
테스트 21 〉	통과 (4.40ms, 36.8MB)
테스트 22 〉	통과 (2.95ms, 37MB)
테스트 23 〉	통과 (2.99ms, 36.5MB)
테스트 24 〉	통과 (3.02ms, 37MB)
테스트 25 〉	통과 (0.25ms, 33.4MB)
테스트 26 〉	통과 (0.28ms, 33.5MB)
테스트 27 〉	통과 (0.27ms, 33.5MB)
테스트 28 〉	통과 (1.44ms, 34.4MB)
테스트 29 〉	통과 (1.41ms, 34.3MB)
테스트 30 〉	통과 (1.03ms, 33.9MB)
테스트 31 〉	통과 (2.30ms, 34.3MB)
테스트 32 〉	통과 (2.35ms, 34.3MB)
테스트 33 〉	통과 (3.06ms, 36.9MB)
테스트 34 〉	통과 (3.06ms, 36.9MB)
테스트 35 〉	통과 (3.06ms, 36.9MB)
테스트 36 〉	통과 (3.11ms, 36.9MB)
테스트 37 〉	통과 (1.49ms, 34.4MB)
테스트 38 〉	통과 (1.46ms, 34.3MB)
테스트 39 〉	통과 (3.01ms, 36.8MB)
테스트 40 〉	통과 (3.06ms, 37MB)
테스트 41 〉	통과 (3.21ms, 36.8MB)
테스트 42 〉	통과 (3.03ms, 36.9MB)
*/




//
function solution(schedules, timelogs, startday) {
    // 출근 희망 시각, 실제 출근 시각, 이벤트 시작 요일
    const n = schedules.length
    let headcount = 0
    for (let i = 0; i < n; i += 1) {
        const [hour1, minute1] = [Math.floor(schedules[i]/100), schedules[i]%100]
        let isSimilar = true
        let day = startday
        for (timelog of timelogs[i]) {
            if (day >= 6) {
                day = day === 6 ? 7 : 1
                continue
            }

            const [hour2, minute2] = [Math.floor(timelog/100), timelog%100]

            if ((hour2 - hour1) * 60 + (minute2 - minute1) > 10) {
                isSimilar = false
                break
            }
            day += 1
        }

        if (isSimilar) {
            headcount += 1
        }

    }


    return headcount
}


/*
정확성  테스트
테스트 1 〉	통과 (0.09ms, 33.4MB)
테스트 2 〉	통과 (0.10ms, 33.4MB)
테스트 3 〉	통과 (0.09ms, 33.4MB)
테스트 4 〉	통과 (0.10ms, 33.4MB)
테스트 5 〉	통과 (0.09ms, 33.5MB)
테스트 6 〉	통과 (0.09ms, 33.4MB)
테스트 7 〉	통과 (2.31ms, 34.7MB)
테스트 8 〉	통과 (2.21ms, 34.7MB)
테스트 9 〉	통과 (2.18ms, 34.8MB)
테스트 10 〉	통과 (2.36ms, 34.7MB)
테스트 11 〉	통과 (2.32ms, 34.7MB)
테스트 12 〉	통과 (2.22ms, 34.9MB)
테스트 13 〉	통과 (2.27ms, 34.8MB)
테스트 14 〉	통과 (2.22ms, 34.8MB)
테스트 15 〉	통과 (2.24ms, 34.8MB)
테스트 16 〉	통과 (2.28ms, 34.8MB)
테스트 17 〉	통과 (2.21ms, 34.8MB)
테스트 18 〉	통과 (2.27ms, 34.8MB)
테스트 19 〉	통과 (2.44ms, 34.8MB)
테스트 20 〉	통과 (2.32ms, 34.8MB)
테스트 21 〉	통과 (2.34ms, 34.7MB)
테스트 22 〉	통과 (2.24ms, 34.8MB)
테스트 23 〉	통과 (2.23ms, 34.9MB)
테스트 24 〉	통과 (3.04ms, 34.8MB)
테스트 25 〉	통과 (0.42ms, 33.5MB)
테스트 26 〉	통과 (0.27ms, 33.5MB)
테스트 27 〉	통과 (0.27ms, 33.5MB)
테스트 28 〉	통과 (1.30ms, 34.4MB)
테스트 29 〉	통과 (1.26ms, 34.5MB)
테스트 30 〉	통과 (0.92ms, 34MB)
테스트 31 〉	통과 (1.34ms, 34.3MB)
테스트 32 〉	통과 (2.13ms, 34.4MB)
테스트 33 〉	통과 (2.26ms, 34.8MB)
테스트 34 〉	통과 (2.36ms, 34.8MB)
테스트 35 〉	통과 (2.28ms, 34.8MB)
테스트 36 〉	통과 (2.39ms, 34.8MB)
테스트 37 〉	통과 (1.42ms, 34.5MB)
테스트 38 〉	통과 (1.28ms, 34.3MB)
테스트 39 〉	통과 (2.37ms, 34.8MB)
테스트 40 〉	통과 (4.01ms, 34.8MB)
테스트 41 〉	통과 (2.32ms, 34.8MB)
테스트 42 〉	통과 (3.60ms, 34.8MB)
*/