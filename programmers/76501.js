function solution(absolutes, signs) {
    var answer = 0;
    absolutes.map((value, idx) => {
        signs[idx] ? answer = answer+value : answer = answer-value;
    })
    return answer;
}

solution([4, 7, 12], [true, false, true])
solution([1, 2, 3], [false, false, true])