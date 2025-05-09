// 250509
function solution(a) {
    // a : 풍선에 쓰인 숫자 (-10억 ~ 10억) 목록 - 겹치는 수 없음
    const N = a.length // 100만 이하

    if (N <= 2) {
        return N
    }
    // 1개만 남을 때까지 터뜨림
    const minNumArr1 = new Array(N) // 끝 -> 처음
    const minNumArr2 = new Array(N) // 처음 -> 끝
    let minNum = a[N-1]
    minNumArr1[N-1] = minNum

    for (let i = N-2; i >= 0; i -= 1) {
        if (minNum > a[i]) {
            minNum = a[i]
        }
        minNumArr1[i] = minNum
    }

    minNum = a[0]
    minNumArr2[0] = minNum
    for (let i = 1; i < N; i += 1) {
        if (minNum > a[i]) {
            minNum = a[i]
        }
        minNumArr2[i] = minNum
    }

    let cnt = 2 // 최후까지 남기는 것이 가능한 풍선 개수 - 맨 처음, 맨 끝
    for (let i = 1; i < N-1; i += 1) {
        const [num, before, after] = [a[i], minNumArr2[i-1], minNumArr1[i+1]]
        if (num <= before || num <= after) {
            cnt += 1
        }
    }

    return cnt
}

/*
정확성  테스트
테스트 1 〉	통과 (0.08ms, 33.4MB)
테스트 2 〉	통과 (0.08ms, 33.5MB)
테스트 3 〉	통과 (0.61ms, 33.7MB)
테스트 4 〉	통과 (10.84ms, 42.3MB)
테스트 5 〉	통과 (18.53ms, 60.6MB)
테스트 6 〉	통과 (24.87ms, 74.9MB)
테스트 7 〉	통과 (30.71ms, 89.5MB)
테스트 8 〉	통과 (32.18ms, 89.6MB)
테스트 9 〉	통과 (33.16ms, 89.5MB)
테스트 10 〉	통과 (30.54ms, 89.5MB)
테스트 11 〉	통과 (35.49ms, 89.4MB)
테스트 12 〉	통과 (34.93ms, 89.3MB)
테스트 13 〉	통과 (38.83ms, 89.3MB)
테스트 14 〉	통과 (30.82ms, 89.5MB)
테스트 15 〉	통과 (50.09ms, 89.4MB)
*/