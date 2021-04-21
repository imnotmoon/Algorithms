function solution(d, budget) {
    var answer = 0;
    var b = budget;
    let arr = d.sort((a, b) => a-b)
    arr.forEach((cost, idx) => {
        if(b >= cost) {
            b -= cost;
            answer += 1;
        }
    })
    console.log(answer)
    return answer;
}

solution([1, 1, 1, 1, 2], 9)
// solution([2, 1, 3, 3, 4], 15)