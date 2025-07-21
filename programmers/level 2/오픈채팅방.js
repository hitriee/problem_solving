// 250721
function solution(record) {
    const answer = []
    const idToName = {}
    const splitedRecord = record.map((log) => log.split(' '))
    splitedRecord.forEach(([command, uid, nickname]) => {
        if (command !== 'Leave') {
            idToName[uid] = nickname
        }
    })

    splitedRecord.forEach(([command, uid, nickname]) => {
        if (command !== 'Change') {
            answer.push(`${idToName[uid]}님이 ${command === 'Enter' ? '들어왔' : '나갔'}습니다.`)
        }
    })

    return answer
}

/*
정확성  테스트
테스트 1 〉	통과 (0.24ms, 33.4MB)
테스트 2 〉	통과 (0.14ms, 33.4MB)
테스트 3 〉	통과 (0.35ms, 33.5MB)
테스트 4 〉	통과 (0.35ms, 33.5MB)
테스트 5 〉	통과 (1.49ms, 34.2MB)
테스트 6 〉	통과 (1.79ms, 34.2MB)
테스트 7 〉	통과 (1.50ms, 34.2MB)
테스트 8 〉	통과 (1.72ms, 34.3MB)
테스트 9 〉	통과 (1.89ms, 34.4MB)
테스트 10 〉	통과 (1.72ms, 34.4MB)
테스트 11 〉	통과 (1.07ms, 33.8MB)
테스트 12 〉	통과 (1.05ms, 33.9MB)
테스트 13 〉	통과 (1.74ms, 34.3MB)
테스트 14 〉	통과 (3.15ms, 34.5MB)
테스트 15 〉	통과 (0.14ms, 33.4MB)
테스트 16 〉	통과 (0.15ms, 33.6MB)
테스트 17 〉	통과 (0.36ms, 33.5MB)
테스트 18 〉	통과 (0.37ms, 33.5MB)
테스트 19 〉	통과 (1.93ms, 34.4MB)
테스트 20 〉	통과 (1.76ms, 34.2MB)
테스트 21 〉	통과 (2.80ms, 34.1MB)
테스트 22 〉	통과 (2.02ms, 34.2MB)
테스트 23 〉	통과 (1.68ms, 34.4MB)
테스트 24 〉	통과 (2.17ms, 34.3MB)
테스트 25 〉	통과 (138.41ms, 86.5MB)
테스트 26 〉	통과 (188.97ms, 104MB)
테스트 27 〉	통과 (190.48ms, 108MB)
테스트 28 〉	통과 (224.94ms, 111MB)
테스트 29 〉	통과 (203.71ms, 110MB)
테스트 30 〉	통과 (246.03ms, 104MB)
테스트 31 〉	통과 (240.40ms, 115MB)
테스트 32 〉	통과 (186.65ms, 102MB)
*/


function solution(record) {
    const answer = []
    const idToName = {}

    record.forEach((log) => {
        const [command, uid, nickname] = log.split(' ')
        if (command === 'Leave') {
            answer.push([uid, '님이 나갔습니다.'])
        } else {
            idToName[uid] = nickname
            if (command === 'Enter') {
                answer.push([uid, '님이 들어왔습니다.'])
            }
        }
    })



    return answer.map(([uid, detail]) => `${idToName[uid]}${detail}`)
}


/*
정확성  테스트
테스트 1 〉	통과 (0.13ms, 33.5MB)
테스트 2 〉	통과 (0.14ms, 33.5MB)
테스트 3 〉	통과 (0.30ms, 33.5MB)
테스트 4 〉	통과 (0.31ms, 33.7MB)
테스트 5 〉	통과 (1.24ms, 34.1MB)
테스트 6 〉	통과 (1.55ms, 34.2MB)
테스트 7 〉	통과 (1.30ms, 34.1MB)
테스트 8 〉	통과 (1.52ms, 34.2MB)
테스트 9 〉	통과 (1.74ms, 34.2MB)
테스트 10 〉	통과 (1.53ms, 33.9MB)
테스트 11 〉	통과 (1.01ms, 33.9MB)
테스트 12 〉	통과 (1.06ms, 34.1MB)
테스트 13 〉	통과 (1.61ms, 34.2MB)
테스트 14 〉	통과 (1.74ms, 34.5MB)
테스트 15 〉	통과 (0.25ms, 33.4MB)
테스트 16 〉	통과 (0.13ms, 33.4MB)
테스트 17 〉	통과 (0.38ms, 33.6MB)
테스트 18 〉	통과 (0.36ms, 33.6MB)
테스트 19 〉	통과 (1.67ms, 34.3MB)
테스트 20 〉	통과 (1.41ms, 34MB)
테스트 21 〉	통과 (1.41ms, 34MB)
테스트 22 〉	통과 (2.13ms, 34.1MB)
테스트 23 〉	통과 (1.55ms, 34.2MB)
테스트 24 〉	통과 (1.87ms, 34.3MB)
테스트 25 〉	통과 (116.66ms, 85.4MB)
테스트 26 〉	통과 (153.93ms, 99.7MB)
테스트 27 〉	통과 (155.77ms, 105MB)
테스트 28 〉	통과 (150.96ms, 104MB)
테스트 29 〉	통과 (156.79ms, 108MB)
테스트 30 〉	통과 (127.90ms, 85.7MB)
테스트 31 〉	통과 (135.76ms, 105MB)
테스트 32 〉	통과 (109.65ms, 97.8MB)
*/

function solution(record) {
    const answer = []
    const idToName = {}

    record.forEach((log) => {
        const [command, uid, nickname] = log.split(' ')
        if (command === 'Leave') {
            answer.push([uid, '나갔'])
        } else {
            idToName[uid] = nickname
            if (command === 'Enter') {
                answer.push([uid, '들어왔'])
            }
        }
    })



    return answer.map(([uid, detail]) => `${idToName[uid]}님이 ${detail}습니다.`)
}
/*
정확성  테스트
테스트 1 〉	통과 (0.14ms, 33MB)
테스트 2 〉	통과 (0.17ms, 33.4MB)
테스트 3 〉	통과 (0.32ms, 33MB)
테스트 4 〉	통과 (0.32ms, 32.9MB)
테스트 5 〉	통과 (1.42ms, 33.5MB)
테스트 6 〉	통과 (1.63ms, 33.7MB)
테스트 7 〉	통과 (1.39ms, 33.9MB)
테스트 8 〉	통과 (1.68ms, 34.1MB)
테스트 9 〉	통과 (1.86ms, 34.3MB)
테스트 10 〉	통과 (2.73ms, 34.1MB)
테스트 11 〉	통과 (1.10ms, 33.9MB)
테스트 12 〉	통과 (1.08ms, 33.9MB)
테스트 13 〉	통과 (1.63ms, 34.1MB)
테스트 14 〉	통과 (1.87ms, 34.4MB)
테스트 15 〉	통과 (0.15ms, 33.4MB)
테스트 16 〉	통과 (0.14ms, 33.4MB)
테스트 17 〉	통과 (0.35ms, 33.6MB)
테스트 18 〉	통과 (0.38ms, 33.4MB)
테스트 19 〉	통과 (1.69ms, 34.2MB)
테스트 20 〉	통과 (1.43ms, 34MB)
테스트 21 〉	통과 (1.46ms, 34MB)
테스트 22 〉	통과 (1.45ms, 34MB)
테스트 23 〉	통과 (1.66ms, 34.2MB)
테스트 24 〉	통과 (1.62ms, 34.3MB)
테스트 25 〉	통과 (165.29ms, 85.2MB)
테스트 26 〉	통과 (190.88ms, 104MB)
테스트 27 〉	통과 (180.47ms, 109MB)
테스트 28 〉	통과 (185.93ms, 111MB)
테스트 29 〉	통과 (178.35ms, 111MB)
테스트 30 〉	통과 (136.47ms, 94.8MB)
테스트 31 〉	통과 (187.38ms, 103MB)
테스트 32 〉	통과 (159.89ms, 102MB)
*/