// 250723
function solution(prices) {
    const N = prices.length
    const answer = Array(N).fill(0)
    const stack = [[0, prices[0]]]

    for (let i = 1; i < N-1; i += 1) {
        const val = prices[i]
        while (stack.length !== 0 && val < stack.at(-1)[1]) {
            const j = stack.pop()[0]
            answer[j] = i-j
        }
        stack.push([i, val])
    }

    stack.forEach(([j, _]) => {
        answer[j] = N-1-j
    })

    return answer
}



/*
정확성  테스트
테스트 1 〉	통과 (0.08ms, 33.4MB)
테스트 2 〉	통과 (0.22ms, 33.4MB)
테스트 3 〉	통과 (0.46ms, 33.7MB)
테스트 4 〉	통과 (0.50ms, 33.6MB)
테스트 5 〉	통과 (0.53ms, 33.8MB)
테스트 6 〉	통과 (0.20ms, 33.5MB)
테스트 7 〉	통과 (0.39ms, 33.6MB)
테스트 8 〉	통과 (0.41ms, 33.6MB)
테스트 9 〉	통과 (0.23ms, 33.5MB)
테스트 10 〉	통과 (0.54ms, 33.7MB)
효율성  테스트
테스트 1 〉	통과 (39.34ms, 45.9MB)
테스트 2 〉	통과 (36.88ms, 43.1MB)
테스트 3 〉	통과 (40.21ms, 46.2MB)
테스트 4 〉	통과 (15.25ms, 44.2MB)
테스트 5 〉	통과 (10.83ms, 43.7MB)
*/




//
function solution(prices) {
    const N = prices.length
    const answer = Array(N).fill(0)
    const stack = []

    prices.forEach((price, i) => {
        while (stack.length !== 0 && price < stack.at(-1)[1]) {
            const j = stack.pop()[0]
            answer[j] = i-j
        }
        stack.push([i, price])
    })

    stack.forEach(([j, _]) => {
        answer[j] = N-1-j
    })

    return answer
}


/*
정확성  테스트
테스트 1 〉	통과 (0.10ms, 33.5MB)
테스트 2 〉	통과 (0.37ms, 33.4MB)
테스트 3 〉	통과 (0.76ms, 33.6MB)
테스트 4 〉	통과 (0.88ms, 33.6MB)
테스트 5 〉	통과 (0.53ms, 33.6MB)
테스트 6 〉	통과 (0.21ms, 33.6MB)
테스트 7 〉	통과 (0.46ms, 33.5MB)
테스트 8 〉	통과 (0.67ms, 33.7MB)
테스트 9 〉	통과 (0.24ms, 33.5MB)
테스트 10 〉	통과 (0.61ms, 33.6MB)
효율성  테스트
테스트 1 〉	통과 (16.18ms, 46.2MB)
테스트 2 〉	통과 (12.67ms, 43.3MB)
테스트 3 〉	통과 (39.82ms, 45.8MB)
테스트 4 〉	통과 (36.13ms, 43.7MB)
테스트 5 〉	통과 (12.56ms, 43.7MB)
*/


//
function solution(prices) {
    const N = prices.length
    const answer = Array(N).fill(0)
    const stack = []

    prices.forEach((price, i) => {
        while (stack.length !== 0) {
            const [j, val] = stack.at(-1)
            if (price < val) {
                answer[j] = i-j
            } else {
                break
            }
            stack.pop()
        }
        stack.push([i, price])
    })

    stack.forEach(([j, _]) => {
        answer[j] = N-1-j
    })

    return answer
}

/*
정확성  테스트
테스트 1 〉	통과 (0.10ms, 33.4MB)
테스트 2 〉	통과 (0.28ms, 33.4MB)
테스트 3 〉	통과 (0.91ms, 33.7MB)
테스트 4 〉	통과 (0.75ms, 33.7MB)
테스트 5 〉	통과 (0.91ms, 33.8MB)
테스트 6 〉	통과 (0.25ms, 33.4MB)
테스트 7 〉	통과 (0.98ms, 33.6MB)
테스트 8 〉	통과 (0.78ms, 33.7MB)
테스트 9 〉	통과 (0.33ms, 33.5MB)
테스트 10 〉	통과 (0.96ms, 34MB)
효율성  테스트
테스트 1 〉	통과 (48.50ms, 45MB)
테스트 2 〉	통과 (37.77ms, 43.1MB)
테스트 3 〉	통과 (19.42ms, 46.8MB)
테스트 4 〉	통과 (38.51ms, 43.4MB)
테스트 5 〉	통과 (13.46ms, 43.8MB)
*/



//
function solution(prices) {
    const N = prices.length
    const answer = Array(N).fill(0)
    const stack = [0]

    for (let i = 1; i < N-1; i += 1) {
        const val = prices[i]
        while (stack.length !== 0 && val < prices[stack.at(-1)]) {
            const j = stack.pop()
            answer[j] = i-j
        }
        stack.push(i)
    }

    stack.forEach((j) => {
        answer[j] = N-1-j
    })

    return answer
}

/*
정확성  테스트
테스트 1 〉	통과 (0.09ms, 33.3MB)
테스트 2 〉	통과 (0.20ms, 33.4MB)
테스트 3 〉	통과 (0.34ms, 33.5MB)
테스트 4 〉	통과 (0.39ms, 33.5MB)
테스트 5 〉	통과 (0.41ms, 33.6MB)
테스트 6 〉	통과 (0.17ms, 33.5MB)
테스트 7 〉	통과 (0.32ms, 33.5MB)
테스트 8 〉	통과 (0.34ms, 33.6MB)
테스트 9 〉	통과 (0.18ms, 33.4MB)
테스트 10 〉	통과 (0.41ms, 33.5MB)
효율성  테스트
테스트 1 〉	통과 (39.37ms, 43.2MB)
테스트 2 〉	통과 (10.39ms, 42MB)
테스트 3 〉	통과 (14.76ms, 43.9MB)
테스트 4 〉	통과 (13.08ms, 42MB)
테스트 5 〉	통과 (9.21ms, 42.3MB)
*/





//
function solution(prices) {
    const N = prices.length
    const answer = Array(N).fill(0)
    const stack = []

    prices.forEach((price, i) => {
        while (stack.length !== 0 && price < prices[stack.at(-1)]) {
            const j = stack.pop()
            answer[j] = i-j
        }
        stack.push(i)
    })

    stack.forEach((j) => {
        answer[j] = N-1-j
    })

    return answer
}

/*
정확성  테스트
테스트 1 〉	통과 (0.08ms, 33.5MB)
테스트 2 〉	통과 (0.22ms, 33.5MB)
테스트 3 〉	통과 (0.39ms, 33.6MB)
테스트 4 〉	통과 (0.65ms, 33.5MB)
테스트 5 〉	통과 (0.47ms, 33.5MB)
테스트 6 〉	통과 (0.20ms, 33.5MB)
테스트 7 〉	통과 (0.49ms, 33.4MB)
테스트 8 〉	통과 (0.38ms, 33.5MB)
테스트 9 〉	통과 (0.18ms, 33.4MB)
테스트 10 〉	통과 (0.45ms, 33.6MB)
효율성  테스트
테스트 1 〉	통과 (13.21ms, 43.6MB)
테스트 2 〉	통과 (11.82ms, 42.4MB)
테스트 3 〉	통과 (14.58ms, 44.2MB)
테스트 4 〉	통과 (11.82ms, 42.1MB)
테스트 5 〉	통과 (30.98ms, 41.9MB)
*/

