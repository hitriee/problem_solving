// 250724
function solution(n, t, m, p) {
    // 진법, 숫자 개수, 인원, 튜브 순서
    let answer = ''
    let [length, cnt, num] = [0, 0, 0]
    let total = ''
    const numToStr = Array.from({length: 10}, (_, i) => i.toString())
    numToStr.push(...['A', 'B', 'C', 'D', 'E', 'F'])

    function newNumber(target) {
        if (target === 0) {
            return '0'
        }
        const result = []
        while (target > 0) {
            result.push(numToStr[target % n])
            target = Math.floor(target/n)
        }

        return result.reverse().join('')
    }

    while (length < m*t) {
        const strNum = newNumber(num)
        length += strNum.length
        total += strNum
        num += 1
    }


    let i = p-1
    while (cnt < t) {
        answer += total[i]
        cnt += 1
        i += m
    }

    return answer
}