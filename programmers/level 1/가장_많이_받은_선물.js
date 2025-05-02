// 250502
function solution(friends, gifts) {
    // 친구 이름 / 선물 기록
    // 다음 달에 선물을 가장 많이 받는 사람의 선물 수

    function convert(person1, person2) {
        return [nameToIdx.get(person1), nameToIdx.get(person2)]
    }

    const nameToIdx = new Map()
    const N = friends.length
    friends.forEach((friend, i) => {
        nameToIdx.set(friend, i)
    })

    const thisMonth = Array.from({length:N}, () => new Array(N+1).fill(0))

    gifts.forEach((gift, i) => {
        const [a, b] = convert(...gift.split(' '))
        thisMonth[a][b] += 1
        thisMonth[b][a] -= 1
    })

    for (let i = 0; i < N; i += 1) {
        thisMonth[i][N] = thisMonth[i].reduce((acc, current) => acc+current)
    }

    const nextMonth = new Array(N+1).fill(0)

    for (let i = 0; i < N-1; i += 1) {
        for (let j = i+1; j < N; j += 1) {
            const giftCnt = thisMonth[i][j]
            // 많은 선물 준 사람이 하나 더 받음
            if (giftCnt > 0) {
                nextMonth[i] += 1
            } else if (giftCnt < 0) {
                nextMonth[j] += 1
            } else {
                // 선물 지수 큰 사람이 하나 받음
                const [giftIdx1, giftIdx2] = [thisMonth[i][N], thisMonth[j][N]]
                if (giftIdx1 > giftIdx2) {
                    nextMonth[i] += 1
                } else if (giftIdx1 < giftIdx2) {
                    nextMonth[j] += 1
                }
            }

        }
    }

    return Math.max(...nextMonth)

}

/*
테스트 1 〉	통과 (0.48ms, 33.5MB)
테스트 2 〉	통과 (0.39ms, 33.4MB)
테스트 3 〉	통과 (0.90ms, 33.5MB)
테스트 4 〉	통과 (0.48ms, 33.4MB)
테스트 5 〉	통과 (1.71ms, 34MB)
테스트 6 〉	통과 (0.64ms, 33.5MB)
테스트 7 〉	통과 (1.68ms, 33.8MB)
테스트 8 〉	통과 (1.87ms, 33.8MB)
테스트 9 〉	통과 (25.43ms, 38MB)
테스트 10 〉	통과 (6.03ms, 36.9MB)
테스트 11 〉	통과 (5.56ms, 36.9MB)
테스트 12 〉	통과 (5.56ms, 36.9MB)
테스트 13 〉	통과 (9.37ms, 38.5MB)
테스트 14 〉	통과 (8.74ms, 38.3MB)
테스트 15 〉	통과 (10.41ms, 37.5MB)
테스트 16 〉	통과 (30.37ms, 37.8MB)
테스트 17 〉	통과 (0.57ms, 33.4MB)
테스트 18 〉	통과 (9.19ms, 37.9MB)
테스트 19 〉	통과 (8.59ms, 37.4MB)
테스트 20 〉	통과 (3.75ms, 37.4MB)
*/