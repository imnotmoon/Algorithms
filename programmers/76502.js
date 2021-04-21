function solution(s) {
    var answer = 0;
    let new_s = s
    for (let i = 0; i < s.length; i++) {
        new_s = new_s.slice(1, new_s.length) + s[i]
        check(new_s) && answer++
    }
    if (s.length % 2 === 1) {
        answer = 0
    }
    console.log(answer)
    return answer;
}

const check = (s) => {
    console.log(s)
    const close = {
        '[': ']',
        '(': ')',
        '{': '}',
    }
    let stack = [''];
    for (let i = 0; i < s.length; i++) {
        if (s[i] === '{' || s[i] === '[' || s[i] === '(') {
            stack.push(s[i])
        } else {
            if (close[stack[stack.length - 1]] === s[i]) stack.pop()
            else return false
        }
    }
    return true
}

// solution("[](){}")
// solution("}]()[{")
// solution("[)(]")
// solution("}}}")
solution("{")