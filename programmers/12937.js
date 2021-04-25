function solution(num) {
    num = num < 0 ? num*(-1) : num
    return num%2 === 1 ? "Odd" : "Even"
}

console.log(solution(3))
console.log(solution(4))