// 250627
function solution(expression) {
    function calc(num1, num2, operator) {
        switch (operator) {
            case '+':
                return num1 + num2
            case '-':
                return num1 - num2
            default:
                return num1 * num2
        }
    }



    function determine_priority(level, operland, operator, maxVal) {
        if (level === LIMIT) {
            return Math.max(Math.abs(operland[0]), maxVal)
        }

        operatorArr.forEach((one, i) => {
            if (!visited[i]) {
                const new_operland = [operland[0]]
                const new_operator = operator.filter((element, idx) => {
                if (element === one) {
                    new_operland.push(calc(new_operland.pop(), operland[idx+1], element))
                    return false
                } else {
                    new_operland.push(operland[idx+1])
                    return true
                }

                })
                visited[i] = true
                maxVal = Math.max(determine_priority(level+1, Array.from(new_operland), Array.from(new_operator), maxVal), maxVal)
                visited[i] = false
            }


        })
        return maxVal
    }



    let before = 0
    const N = expression.length
    const operatorArr = ['+', '-', '*']
    const operatorSet = new Set(operatorArr)
    const operland = []
    const operator = []

    for (let i = 0; i < N; i += 1) {
        const element = expression.charAt(i)
        if (operatorSet.has(element)) {
            operland.push(parseInt(expression.substring(before, i)))
            before = i+1
            operator.push(element)
        }
    }

    operland.push(parseInt(expression.substring(before)))

    const LIMIT = 3
    const visited = Array(LIMIT).fill(false)

    return determine_priority(0, Array.from(operland), Array.from(operator), 0)
}



/*
정확성  테스트
테스트 1 〉	통과 (0.31ms, 33.4MB)
테스트 2 〉	통과 (0.31ms, 33.4MB)
테스트 3 〉	통과 (0.34ms, 33.4MB)
테스트 4 〉	통과 (0.34ms, 33.4MB)
테스트 5 〉	통과 (0.34ms, 33.4MB)
테스트 6 〉	통과 (0.34ms, 33.5MB)
테스트 7 〉	통과 (0.38ms, 33.5MB)
테스트 8 〉	통과 (0.41ms, 33.5MB)
테스트 9 〉	통과 (0.44ms, 33.4MB)
테스트 10 〉	통과 (0.43ms, 33.4MB)
테스트 11 〉	통과 (0.42ms, 33.5MB)
테스트 12 〉	통과 (0.42ms, 33.5MB)
테스트 13 〉	통과 (0.42ms, 33.4MB)
테스트 14 〉	통과 (0.45ms, 33.5MB)
테스트 15 〉	통과 (0.46ms, 33.5MB)
테스트 16 〉	통과 (0.32ms, 33.4MB)
테스트 17 〉	통과 (0.32ms, 33.4MB)
테스트 18 〉	통과 (0.31ms, 33.4MB)
테스트 19 〉	통과 (0.32ms, 33.4MB)
테스트 20 〉	통과 (0.58ms, 33.5MB)
테스트 21 〉	통과 (0.42ms, 33.4MB)
테스트 22 〉	통과 (0.44ms, 33.6MB)
테스트 23 〉	통과 (0.32ms, 33.5MB)
테스트 24 〉	통과 (0.43ms, 33.4MB)
테스트 25 〉	통과 (0.44ms, 33.6MB)
테스트 26 〉	통과 (0.30ms, 33.4MB)
테스트 27 〉	통과 (0.49ms, 33.4MB)
테스트 28 〉	통과 (0.45ms, 33.4MB)
테스트 29 〉	통과 (0.43ms, 33.4MB)
테스트 30 〉	통과 (0.43ms, 33.5MB)
*/


//
const operatorArr = ['+', '-', '*']
const LIMIT = 3
const visited = Array(LIMIT).fill(false)
const operatorSet = new Set(operatorArr)


function calc(num1, num2, operator) {
    switch (operator) {
        case '+':
            return num1 + num2
        case '-':
            return num1 - num2
        default:
            return num1 * num2
    }
}

function determine_priority(level, operland, operator, maxVal) {
    if (level === LIMIT) {
        return Math.max(Math.abs(operland[0]), maxVal)
    }

    operatorArr.forEach((one, i) => {
        if (!visited[i]) {
            const new_operland = [operland[0]]
            const new_operator = operator.filter((element, idx) => {
            if (element === one) {
                new_operland.push(calc(new_operland.pop(), operland[idx+1], element))
                return false
            } else {
                new_operland.push(operland[idx+1])
                return true
            }

            })
            visited[i] = true
            maxVal = Math.max(determine_priority(level+1, Array.from(new_operland), Array.from(new_operator), maxVal), maxVal)
            visited[i] = false
        }


    })
    return maxVal
}


function fillArr(expression, operland, operator) {
    const N = expression.length
    let before = 0

    for (let i = 0; i < N; i += 1) {
        const element = expression.charAt(i)
        if (operatorSet.has(element)) {
            operland.push(parseInt(expression.substring(before, i)))
            before = i+1
            operator.push(element)
        }
    }

    operland.push(parseInt(expression.substring(before)))
}



function solution(expression) {
    const operland = []
    const operator = []

    fillArr(expression, operland, operator)


    return determine_priority(0, Array.from(operland), Array.from(operator), 0)
}

/*
정확성  테스트
테스트 1 〉	통과 (0.32ms, 33.5MB)
테스트 2 〉	통과 (0.40ms, 33.5MB)
테스트 3 〉	통과 (0.42ms, 33.5MB)
테스트 4 〉	통과 (0.37ms, 33.4MB)
테스트 5 〉	통과 (0.44ms, 33.5MB)
테스트 6 〉	통과 (0.40ms, 33.5MB)
테스트 7 〉	통과 (0.42ms, 33.4MB)
테스트 8 〉	통과 (0.38ms, 33.5MB)
테스트 9 〉	통과 (0.38ms, 33.4MB)
테스트 10 〉	통과 (0.38ms, 33.5MB)
테스트 11 〉	통과 (0.70ms, 33.5MB)
테스트 12 〉	통과 (0.60ms, 33.4MB)
테스트 13 〉	통과 (0.41ms, 33.6MB)
테스트 14 〉	통과 (0.42ms, 33.5MB)
테스트 15 〉	통과 (0.48ms, 33.5MB)
테스트 16 〉	통과 (0.60ms, 33.5MB)
테스트 17 〉	통과 (0.61ms, 33.5MB)
테스트 18 〉	통과 (0.36ms, 33.5MB)
테스트 19 〉	통과 (0.57ms, 33.6MB)
테스트 20 〉	통과 (0.36ms, 33.4MB)
테스트 21 〉	통과 (0.43ms, 33.4MB)
테스트 22 〉	통과 (0.39ms, 33.5MB)
테스트 23 〉	통과 (0.47ms, 33.6MB)
테스트 24 〉	통과 (0.41ms, 33.4MB)
테스트 25 〉	통과 (0.42ms, 33.5MB)
테스트 26 〉	통과 (0.33ms, 33.6MB)
테스트 27 〉	통과 (0.50ms, 33.6MB)
테스트 28 〉	통과 (0.46ms, 33.4MB)
테스트 29 〉	통과 (0.46ms, 33.4MB)
테스트 30 〉	통과 (0.42ms, 33.6MB)
*/