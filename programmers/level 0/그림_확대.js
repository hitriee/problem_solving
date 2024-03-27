// 240326
function solution(picture, k) {
    const answer = []
    picture.forEach((pixels, index) => {
        const length = pixels.length
        let [cnt, element] = [k, pixels[0]]
        const temp = []
        for (let i = 1; i < length; i += 1) {
            if (pixels[i] === element) {
                cnt += k
            } else {
                temp.push(element.repeat(cnt))
                cnt = k
                element = pixels[i]
            }
        }
        temp.push(element.repeat(cnt))
        result = temp.join('')
        for (let i = 0; i < k; i += 1) {
            answer.push(result)
        }
    })
    return answer;
}