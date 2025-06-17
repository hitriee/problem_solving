// 250617
function solution(wallpaper) {

    // 파일을 한번에 삭제하기 위한 최소 이동 거리
    const [n, m] = [wallpaper.length, wallpaper[0].length]
    let [minX, minY, maxX, maxY] = [n+1, m+1, -1, -1]
    for (let i = 0; i < n; i += 1) {
        for (let j = 0; j < m; j += 1) {
            if (wallpaper[i][j] === '#') {
                if (i < minX) {
                    minX = i
                }
                if (i > maxX) {
                    maxX = i
                }

                if (j < minY) {
                    minY = j
                }
                if (j > maxY) {
                    maxY = j
                }
            }
        }
    }

    maxX = maxX < minX ? minX+1 : maxX+1
    maxY = maxY < minY ? minY+1 : maxY+1

    return [minX, minY, maxX, maxY]
}

/*
정확성  테스트
테스트 1 〉	통과 (0.08ms, 33.5MB)
테스트 2 〉	통과 (0.10ms, 33.5MB)
테스트 3 〉	통과 (0.09ms, 33.4MB)
테스트 4 〉	통과 (0.08ms, 33.4MB)
테스트 5 〉	통과 (0.08ms, 33.2MB)
테스트 6 〉	통과 (0.08ms, 33.6MB)
테스트 7 〉	통과 (0.22ms, 33.4MB)
테스트 8 〉	통과 (0.24ms, 33.5MB)
테스트 9 〉	통과 (0.28ms, 33.5MB)
테스트 10 〉	통과 (0.23ms, 33.5MB)
테스트 11 〉	통과 (0.27ms, 33.5MB)
테스트 12 〉	통과 (0.33ms, 33.6MB)
테스트 13 〉	통과 (0.29ms, 33.5MB)
테스트 14 〉	통과 (0.24ms, 33.4MB)
테스트 15 〉	통과 (0.27ms, 33.4MB)
테스트 16 〉	통과 (0.44ms, 33.6MB)
테스트 17 〉	통과 (0.22ms, 33.5MB)
테스트 18 〉	통과 (0.29ms, 33.6MB)
테스트 19 〉	통과 (0.40ms, 33.4MB)
테스트 20 〉	통과 (0.25ms, 33.6MB)
테스트 21 〉	통과 (0.09ms, 33.4MB)
테스트 22 〉	통과 (0.12ms, 33.5MB)
테스트 23 〉	통과 (0.10ms, 33.4MB)
테스트 24 〉	통과 (0.08ms, 33.5MB)
테스트 25 〉	통과 (0.56ms, 33.6MB)
테스트 26 〉	통과 (0.28ms, 33.4MB)
테스트 27 〉	통과 (0.41ms, 33.6MB)
테스트 28 〉	통과 (0.21ms, 33.4MB)
테스트 29 〉	통과 (0.41ms, 33.4MB)
테스트 30 〉	통과 (0.47ms, 33.4MB)
테스트 31 〉	통과 (0.32ms, 33.6MB)
*/


//
function solution(wallpaper) {

    // 파일을 한번에 삭제하기 위한 최소 이동 거리
    const [n, m] = [wallpaper.length, wallpaper[0].length]
    const minVals = [n+1, m+1]
    const maxVals = [-1, -1]
    for (let i = 0; i < n; i += 1) {
        for (let j = 0; j < m; j += 1) {
            if (wallpaper[i][j] === '#') {
                [i, j].forEach((k, idx) => {
                    if (k < minVals[idx]) {
                        minVals[idx] = k
                    }
                    if (k > maxVals[idx]) {
                        maxVals[idx] = k
                    }
                })

            }
        }
    }

    for (let k = 0; k < 2; k += 1) {
        maxVals[k] = Math.max(minVals[k], maxVals[k]) + 1
    }

    return [...minVals, ...maxVals]
}

/*
정확성  테스트
테스트 1 〉	통과 (0.25ms, 33.4MB)
테스트 2 〉	통과 (0.12ms, 33.5MB)
테스트 3 〉	통과 (0.11ms, 33.5MB)
테스트 4 〉	통과 (0.25ms, 33.4MB)
테스트 5 〉	통과 (0.26ms, 33.5MB)
테스트 6 〉	통과 (0.26ms, 33.6MB)
테스트 7 〉	통과 (0.34ms, 33.4MB)
테스트 8 〉	통과 (0.39ms, 33.5MB)
테스트 9 〉	통과 (0.54ms, 33.6MB)
테스트 10 〉	통과 (0.36ms, 33.5MB)
테스트 11 〉	통과 (0.31ms, 33.5MB)
테스트 12 〉	통과 (0.31ms, 33.4MB)
테스트 13 〉	통과 (0.27ms, 33.4MB)
테스트 14 〉	통과 (0.32ms, 33.5MB)
테스트 15 〉	통과 (0.31ms, 33.4MB)
테스트 16 〉	통과 (0.34ms, 33.5MB)
테스트 17 〉	통과 (0.37ms, 33.5MB)
테스트 18 〉	통과 (0.42ms, 33.6MB)
테스트 19 〉	통과 (0.35ms, 33.6MB)
테스트 20 〉	통과 (0.44ms, 33.6MB)
테스트 21 〉	통과 (0.13ms, 33.5MB)
테스트 22 〉	통과 (0.11ms, 33.4MB)
테스트 23 〉	통과 (0.26ms, 33.4MB)
테스트 24 〉	통과 (0.26ms, 33.5MB)
테스트 25 〉	통과 (0.35ms, 33.5MB)
테스트 26 〉	통과 (0.38ms, 33.4MB)
테스트 27 〉	통과 (0.31ms, 33.5MB)
테스트 28 〉	통과 (0.31ms, 33.4MB)
테스트 29 〉	통과 (0.32ms, 33.5MB)
테스트 30 〉	통과 (0.69ms, 33.7MB)
테스트 31 〉	통과 (0.52ms, 33.4MB)
*/



//
function solution(wallpaper) {

    // 파일을 한번에 삭제하기 위한 최소 이동 거리
    const [n, m] = [wallpaper.length, wallpaper[0].length]
    let [minX, minY, maxX, maxY] = [n+1, m+1, -1, -1]
    for (let i = 0; i < n; i += 1) {
        for (let j = 0; j < m; j += 1) {
            if (wallpaper[i][j] === '#') {
                if (i < minX) {
                    minX = i
                }
                if (i >= maxX) {
                    maxX = i+1
                }

                if (j < minY) {
                    minY = j
                }
                if (j >= maxY) {
                    maxY = j+1
                }
            }
        }
    }

    return [minX, minY, maxX, maxY]
}

/*
정확성  테스트
테스트 1 〉	통과 (0.07ms, 33.5MB)
테스트 2 〉	통과 (0.08ms, 33.4MB)
테스트 3 〉	통과 (0.07ms, 33.5MB)
테스트 4 〉	통과 (0.07ms, 33.4MB)
테스트 5 〉	통과 (0.17ms, 33.5MB)
테스트 6 〉	통과 (0.10ms, 33.6MB)
테스트 7 〉	통과 (0.21ms, 33.5MB)
테스트 8 〉	통과 (0.22ms, 33.5MB)
테스트 9 〉	통과 (0.26ms, 33.5MB)
테스트 10 〉	통과 (0.20ms, 33.5MB)
테스트 11 〉	통과 (0.20ms, 33.4MB)
테스트 12 〉	통과 (0.21ms, 33.4MB)
테스트 13 〉	통과 (0.30ms, 33.5MB)
테스트 14 〉	통과 (0.21ms, 33.4MB)
테스트 15 〉	통과 (0.22ms, 33.6MB)
테스트 16 〉	통과 (0.26ms, 33.6MB)
테스트 17 〉	통과 (0.19ms, 33.4MB)
테스트 18 〉	통과 (0.25ms, 33.5MB)
테스트 19 〉	통과 (0.22ms, 33.4MB)
테스트 20 〉	통과 (0.27ms, 33.4MB)
테스트 21 〉	통과 (0.07ms, 33.4MB)
테스트 22 〉	통과 (0.07ms, 33.5MB)
테스트 23 〉	통과 (0.07ms, 33.4MB)
테스트 24 〉	통과 (0.07ms, 33.5MB)
테스트 25 〉	통과 (0.23ms, 33.5MB)
테스트 26 〉	통과 (0.22ms, 33.5MB)
테스트 27 〉	통과 (0.22ms, 33.4MB)
테스트 28 〉	통과 (0.20ms, 33.4MB)
테스트 29 〉	통과 (0.20ms, 33.4MB)
테스트 30 〉	통과 (0.26ms, 33.5MB)
테스트 31 〉	통과 (0.28ms, 33.5MB)
*/




//
function solution(wallpaper) {

    // 파일을 한번에 삭제하기 위한 최소 이동 거리
    const [n, m] = [wallpaper.length, wallpaper[0].length]
    const minVals = [n+1, m+1]
    const maxVals = [-1, -1]
    for (let i = 0; i < n; i += 1) {
        for (let j = 0; j < m; j += 1) {
            if (wallpaper[i][j] === '#') {
                [i, j].forEach((k, idx) => {
                    if (k < minVals[idx]) {
                        minVals[idx] = k
                    }
                    if (k >= maxVals[idx]) {
                        maxVals[idx] = k+1
                    }
                })

            }
        }
    }

    return [...minVals, ...maxVals]
}



/*
정확성  테스트
테스트 1 〉	통과 (0.23ms, 33.4MB)
테스트 2 〉	통과 (0.11ms, 33.5MB)
테스트 3 〉	통과 (0.11ms, 33.5MB)
테스트 4 〉	통과 (0.25ms, 33.5MB)
테스트 5 〉	통과 (0.25ms, 33.5MB)
테스트 6 〉	통과 (0.24ms, 31.8MB)
테스트 7 〉	통과 (0.33ms, 31.6MB)
테스트 8 〉	통과 (0.37ms, 33.5MB)
테스트 9 〉	통과 (0.55ms, 33.6MB)
테스트 10 〉	통과 (0.32ms, 33.5MB)
테스트 11 〉	통과 (0.28ms, 33.4MB)
테스트 12 〉	통과 (0.32ms, 33.5MB)
테스트 13 〉	통과 (0.26ms, 33.5MB)
테스트 14 〉	통과 (0.29ms, 33.4MB)
테스트 15 〉	통과 (0.30ms, 33.5MB)
테스트 16 〉	통과 (0.37ms, 33.5MB)
테스트 17 〉	통과 (0.26ms, 33.5MB)
테스트 18 〉	통과 (0.41ms, 33.5MB)
테스트 19 〉	통과 (0.34ms, 33.5MB)
테스트 20 〉	통과 (0.47ms, 33.5MB)
테스트 21 〉	통과 (0.12ms, 33.5MB)
테스트 22 〉	통과 (0.11ms, 33.4MB)
테스트 23 〉	통과 (0.24ms, 33.5MB)
테스트 24 〉	통과 (0.24ms, 33.4MB)
테스트 25 〉	통과 (0.34ms, 33.5MB)
테스트 26 〉	통과 (0.37ms, 33.5MB)
테스트 27 〉	통과 (0.29ms, 33.5MB)
테스트 28 〉	통과 (0.31ms, 33.6MB)
테스트 29 〉	통과 (0.29ms, 33.6MB)
테스트 30 〉	통과 (0.68ms, 33.6MB)
테스트 31 〉	통과 (0.36ms, 33.5MB)
*/