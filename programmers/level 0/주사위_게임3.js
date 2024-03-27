// 240326
function add_num(object, num) {
    if (num in object) {
        object[num] += 1
    } else {
        object[num] = 1
    }
}
function solution(a, b, c, d) {
    const object = {}
    add_num(object, a)
    add_num(object, b)
    add_num(object, c)
    add_num(object, d)
    const key_arr = Object.keys(object)
    const length = key_arr.length
    if (length === 1) {
        return a*1111
    } else if (length == 4) {
        return Math.min(a*1, b*1, c*1, d*1)
    } else if (length === 3) {
        const [p, q, r] = key_arr
        if (object[p] === 2) {
            return q*r
        } else if (object[q] === 2) {
            return p*r
        }
        return p*q
    } else if (object[a] === 2) {
        const [p, q] = key_arr
        return (p*1+q*1) * (p > q ? p-q : q-p)
    } else {
        const [p, q] = key_arr
        return object[p] === 3 ? (10*p+1*q)**2 : (10*q+1*p)**2
    }
}