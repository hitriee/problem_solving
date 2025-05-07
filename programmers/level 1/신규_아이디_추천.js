// 250507
function solution(initial_id) {
    let new_id1 = []
    const upperToLower = new Map()
    // 소문자, 숫자, -, _, .
    const possible = new Set(['-', '_', '.'])
    const lowerStartCode = 'a'.charCodeAt()
    const upperStartCode = 'A'.charCodeAt()

    for (let i = 0; i < 10; i += 1) {
        possible.add(i+'')
    }

    for (let i = 0; i < 26; i += 1) {
        const key = String.fromCharCode(upperStartCode+i)
        const value = String.fromCharCode(lowerStartCode+i)
        upperToLower.set(key, value)
        possible.add(value)
    }

    // 1 : 대문자 -> 소문자
    for (const element of initial_id) {
        const newElement = upperToLower.get(element)
        const charCode = String.fromCharCode(element)
        if (newElement) {
            // 1 : 대문자 -> 소문자
            new_id1.push(newElement)
        } else if (possible.has(element)) {
            // 2 : 사용 가능한 문자만 남겨두기
            new_id1.push(element)
        }

    }

    let cnt = 1 // 4 : . 처음 -> 제거
    let new_id2 = []
    new_id1.forEach((element) => {
        // 3 : . 연속 -> 하나만 남겨두기
        if (element !== '.') {
            cnt = 0
            new_id2.push(element)
        } else {
            if (cnt === 0) {
                new_id2.push(element)
            }
            cnt += 1
        }
    })

    let length = new_id2.length

    if (new_id2[length - 1] === '.') {
        // 4 : . 끝 -> 제거
        new_id2.pop()
        length -= 1
    }

    if (length === 0) {
        // 5 : 빈 문자열 -> a 대입
        new_id2.push('a')
        length += 1
    }
    // 6 : 16자 이상이면 첫 15개 문자만 -> 끝 . 제거
    while (length >= 16) {
        new_id2.pop()
            length -= 1
    }
    if (new_id2[length-1] === '.') {
        new_id2.pop()
        length -= 1
    }

    // 7 : 2자 이하면 마지막 문자를 길이가 3이 될 때까지 붙이기
    while (length < 3) {
        new_id2.push(new_id2[length-1])
        length += 1
    }


    return new_id2.join('')
}

/*
정확성  테스트
테스트 1 〉	통과 (0.22ms, 33.5MB)
테스트 2 〉	통과 (0.15ms, 33.4MB)
테스트 3 〉	통과 (0.18ms, 33.4MB)
테스트 4 〉	통과 (0.16ms, 33.6MB)
테스트 5 〉	통과 (0.28ms, 33.6MB)
테스트 6 〉	통과 (0.17ms, 33.5MB)
테스트 7 〉	통과 (0.28ms, 33.4MB)
테스트 8 〉	통과 (0.26ms, 33.4MB)
테스트 9 〉	통과 (0.15ms, 33.4MB)
테스트 10 〉	통과 (0.24ms, 33.5MB)
테스트 11 〉	통과 (0.27ms, 33.5MB)
테스트 12 〉	통과 (0.33ms, 33.4MB)
테스트 13 〉	통과 (0.29ms, 33.4MB)
테스트 14 〉	통과 (0.27ms, 33.4MB)
테스트 15 〉	통과 (0.41ms, 33.4MB)
테스트 16 〉	통과 (0.51ms, 33.5MB)
테스트 17 〉	통과 (0.63ms, 33.4MB)
테스트 18 〉	통과 (0.44ms, 33.5MB)
테스트 19 〉	통과 (1.02ms, 33.6MB)
테스트 20 〉	통과 (0.81ms, 33.4MB)
테스트 21 〉	통과 (0.51ms, 33.6MB)
테스트 22 〉	통과 (0.46ms, 33.5MB)
테스트 23 〉	통과 (0.61ms, 33.5MB)
테스트 24 〉	통과 (0.99ms, 33.6MB)
테스트 25 〉	통과 (0.54ms, 33.6MB)
테스트 26 〉	통과 (0.58ms, 33.6MB)
*/






//
function solution(initial_id) {
    // 아이디의 길이는 3 ~ 15
    // 소문자, 숫자, -, _, .
    // .는 처음과 끝에 사용 X, 연속 사용 X
    let new_id1 = []
    const upperToLower = new Map()
    const possible = new Set(['-', '_', '.'])

    for (let i = 0; i < 10; i += 1) {
        possible.add(i+'')
    }

    for (let i = 0; i < 26; i += 1) {
        const key = String.fromCharCode('A'.charCodeAt()+i)
        const value = String.fromCharCode('a'.charCodeAt()+i)
        upperToLower.set(key, value)
        possible.add(value)
    }

    // 1 : 대문자 -> 소문자
    for (const element of initial_id) {
        const newElement = upperToLower.get(element)
        const charCode = String.fromCharCode(element)
        if (newElement) {
            // 1 : 대문자 -> 소문자
            new_id1.push(newElement)
        } else if (possible.has(element)) {
            // 2 : 사용 가능한 문자만 남겨두기
            new_id1.push(element)
        }

    }

    let cnt = 1 // 4 : . 처음 -> 제거
    let new_id2 = []
    new_id1.forEach((element) => {
        // 3 : . 연속 -> 하나만 남겨두기
        if (element !== '.') {
            cnt = 0
            new_id2.push(element)
        } else {
            if (cnt === 0) {
                new_id2.push(element)
            }
            cnt += 1
        }
    })

    let length = new_id2.length

    if (new_id2[length - 1] === '.') {
        // 4 : . 끝 -> 제거
        new_id2.pop()
        length -= 1
    }

    if (length === 0) {
        // 5 : 빈 문자열 -> a 대입
        new_id2.push('a')
        length += 1
    }
    // 6 : 16자 이상이면 첫 15개 문자만 -> 끝 . 제거
    while (length >= 16) {
        new_id2.pop()
            length -= 1
    }
    if (new_id2[length-1] === '.') {
        new_id2.pop()
        length -= 1
    }

    // 7 : 2자 이하면 마지막 문자를 길이가 3이 될 때까지 붙이기
    while (length < 3) {
        new_id2.push(new_id2[length-1])
        length += 1
    }


    return new_id2.join('')
}


/*
정확성  테스트
테스트 1 〉	통과 (0.24ms, 33.4MB)
테스트 2 〉	통과 (0.24ms, 33.5MB)
테스트 3 〉	통과 (0.27ms, 33.4MB)
테스트 4 〉	통과 (0.21ms, 33.5MB)
테스트 5 〉	통과 (0.16ms, 33.6MB)
테스트 6 〉	통과 (0.16ms, 33.4MB)
테스트 7 〉	통과 (0.16ms, 33.4MB)
테스트 8 〉	통과 (0.16ms, 33.5MB)
테스트 9 〉	통과 (0.15ms, 33.4MB)
테스트 10 〉	통과 (0.23ms, 33.5MB)
테스트 11 〉	통과 (0.25ms, 33.5MB)
테스트 12 〉	통과 (0.32ms, 33.5MB)
테스트 13 〉	통과 (0.48ms, 33.4MB)
테스트 14 〉	통과 (0.30ms, 33.4MB)
테스트 15 〉	통과 (0.29ms, 33.4MB)
테스트 16 〉	통과 (0.33ms, 33.5MB)
테스트 17 〉	통과 (0.42ms, 33.5MB)
테스트 18 〉	통과 (0.46ms, 33.5MB)
테스트 19 〉	통과 (0.72ms, 33.6MB)
테스트 20 〉	통과 (0.49ms, 33.5MB)
테스트 21 〉	통과 (0.57ms, 33.5MB)
테스트 22 〉	통과 (0.48ms, 33.5MB)
테스트 23 〉	통과 (0.57ms, 33.6MB)
테스트 24 〉	통과 (0.58ms, 33.6MB)
테스트 25 〉	통과 (0.63ms, 33.6MB)
테스트 26 〉	통과 (0.55ms, 33.5MB)
*/





//
function solution(initial_id) {
    // 아이디의 길이는 3 ~ 15
    // 소문자, 숫자, -, _, .
    // .는 처음과 끝에 사용 X, 연속 사용 X
    let new_id1 = []
    const upperToLower = new Map()
    const possible = new Set(['-', '_', '.'])

    for (let i = 0; i < 10; i += 1) {
        possible.add(i+'')
    }

    for (let i = 0; i < 26; i += 1) {
        const key = String.fromCharCode('A'.charCodeAt()+i)
        const value = String.fromCharCode('a'.charCodeAt()+i)
        upperToLower.set(key, value)
        possible.add(value)
    }

    // 1 : 대문자 -> 소문자
    for (const element of initial_id) {
        const newElement = upperToLower.get(element)
        const charCode = String.fromCharCode(element)
        if (newElement) {
            // 1 : 대문자 -> 소문자
            new_id1.push(newElement)
        } else if (possible.has(element)) {
            // 2 : 사용 가능한 문자만 남겨두기
            new_id1.push(element)
        }

    }

    let cnt = 1 // 4 : . 처음 -> 제거
    let new_id2 = []
    new_id1.forEach((element) => {
        // 3 : . 연속 -> 하나만 남겨두기
        if (element !== '.') {
            cnt = 0
            new_id2.push(element)
        } else {
            if (cnt === 0) {
                new_id2.push(element)
            }
            cnt += 1
        }
    })

    let length = new_id2.length

    if (new_id2[length - 1] === '.') {
        // 4 : . 끝 -> 제거
        new_id2.pop()
        length -= 1
    }

    if (length === 0) {
        // 5 : 빈 문자열 -> a 대입
        // 7 : 2자 이하면 마지막 문자를 길이가 3이 될 때까지 붙이기
        new_id2.push('aaa')
    } else if (length >= 16) {
        // 6 : 16자 이상이면 첫 15개 문자만 -> 끝 . 제거
        do {
            new_id2.pop()
            length -= 1
        } while (length >= 16)

        if (new_id2[length-1] === '.') {
            new_id2.pop()
            length -= 1
        }

    } else if (length <= 2) {
        // 7 : 2자 이하면 마지막 문자를 길이가 3이 될 때까지 붙이기
        do {
            new_id2.push(new_id2[length-1])
            length += 1
        } while (length < 3)
    }


    return new_id2.join('')
}

/*
정확성  테스트
테스트 1 〉	통과 (0.16ms, 33.4MB)
테스트 2 〉	통과 (0.17ms, 33.4MB)
테스트 3 〉	통과 (0.16ms, 33.4MB)
테스트 4 〉	통과 (0.18ms, 33.4MB)
테스트 5 〉	통과 (0.16ms, 33.5MB)
테스트 6 〉	통과 (0.16ms, 33.4MB)
테스트 7 〉	통과 (0.17ms, 33.4MB)
테스트 8 〉	통과 (0.16ms, 33.4MB)
테스트 9 〉	통과 (0.16ms, 33.4MB)
테스트 10 〉	통과 (0.28ms, 33.4MB)
테스트 11 〉	통과 (0.16ms, 33.5MB)
테스트 12 〉	통과 (0.45ms, 33.5MB)
테스트 13 〉	통과 (0.32ms, 33.5MB)
테스트 14 〉	통과 (0.29ms, 33.4MB)
테스트 15 〉	통과 (0.29ms, 33.5MB)
테스트 16 〉	통과 (0.32ms, 33.6MB)
테스트 17 〉	통과 (0.40ms, 33.6MB)
테스트 18 〉	통과 (0.44ms, 33.5MB)
테스트 19 〉	통과 (0.62ms, 33.6MB)
테스트 20 〉	통과 (0.52ms, 33.4MB)
테스트 21 〉	통과 (0.52ms, 33.5MB)
테스트 22 〉	통과 (0.48ms, 33.5MB)
테스트 23 〉	통과 (0.58ms, 33.5MB)
테스트 24 〉	통과 (1.09ms, 33.6MB)
테스트 25 〉	통과 (0.55ms, 33.7MB)
테스트 26 〉	통과 (0.57ms, 33.6MB)
*/