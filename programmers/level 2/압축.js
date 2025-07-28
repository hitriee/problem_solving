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