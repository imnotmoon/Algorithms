function solution(num) {
    var answer = 0;
    while(answer < 500) {
        if(num === 1) {
            break
        }
        if(num % 2 === 0) num /= 2
        else if(num % 2 === 1) num = num*3+1
        answer += 1
    }
    return answer === 500 ? -1 : answer;
}

solution(6)
solution(16)
solution(626331)