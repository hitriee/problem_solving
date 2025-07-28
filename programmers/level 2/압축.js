// 250728
function solution(msg) {
    const dict = {}
    const aCode = 'A'.charCodeAt()

    for (let i = 0; i < 26; i += 1) {
        dict[String.fromCharCode(aCode+i)] = i+1
    }

    let [i, j, N] = [27, 0, msg.length]
    let word = msg.charAt(j)
    const answer = []
    let isLast = false

    while (j < N) {
        while (dict.hasOwnProperty(word)) {
            j += 1
            if (j >= N) {
                isLast = true
                answer.push(dict[word])
                break
            }
            word += msg.charAt(j)
        }

        if (!isLast) {
            answer.push(dict[word.slice(0, -1)])
            dict[word] = i
            word = msg.charAt(j)
            i += 1
        }
    }



    return answer
}

/*
정확성  테스트
테스트 1 〉	통과 (0.12ms, 33.4MB)
테스트 2 〉	통과 (0.23ms, 33.4MB)
테스트 3 〉	통과 (0.17ms, 33.5MB)
테스트 4 〉	통과 (0.45ms, 33.5MB)
테스트 5 〉	통과 (0.36ms, 33.5MB)
테스트 6 〉	통과 (0.50ms, 33.6MB)
테스트 7 〉	통과 (0.45ms, 33.6MB)
테스트 8 〉	통과 (0.47ms, 33.6MB)
테스트 9 〉	통과 (0.12ms, 33.6MB)
테스트 10 〉	통과 (0.48ms, 33.5MB)
테스트 11 〉	통과 (0.46ms, 33.5MB)
테스트 12 〉	통과 (0.52ms, 33.6MB)
테스트 13 〉	통과 (0.66ms, 33.7MB)
테스트 14 〉	통과 (0.95ms, 33.8MB)
테스트 15 〉	통과 (0.66ms, 33.6MB)
테스트 16 〉	통과 (0.59ms, 33.7MB)
테스트 17 〉	통과 (0.47ms, 33.5MB)
테스트 18 〉	통과 (0.33ms, 33.6MB)
테스트 19 〉	통과 (0.37ms, 33.6MB)
테스트 20 〉	통과 (0.48ms, 33.5MB)
*/