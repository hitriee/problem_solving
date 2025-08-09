// 250717
function solution(...arr) {
    const n = arr[0].length
    let answer = 0

    arr.forEach((element, idx) => {
        element.sort((a, b) => b-a)
        let gcd = element[0]
        for (let i = 1; i < n; i += 1) {
            let num = element[i]
            while (num) {
                [gcd, num] = [num, gcd % num]
            }

        }

        let possible = true
        for (let j = 0; j < n; j += 1) {
            if (arr[1-idx][j] % gcd === 0) {
                possible = false
                break
            }
        }
        if (possible) {
            answer = Math.max(answer, gcd)
        }

    })


    return answer
}