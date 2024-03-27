// 240326
function solution(arr, query) {
    let answer = [...arr]
    query.forEach((value, index) => {
        if (index % 2 === 0) {
            answer.splice(value+1)
        } else {
            answer = answer.splice(value)
        }
    })
    return answer
}