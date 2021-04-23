function solution(arr) {
    let arr2 = [...arr]
    var answer = [];
    if(arr.length == 1) {
        answer = [-1]
    } else {
        let min = (arr2.sort((a, b) => a - b))[0]
        let minIdx = arr.findIndex(item => item === min)
        arr.splice(minIdx, 1)
        answer = arr
    }
    console.log(answer)
    return answer;
}

solution([4,3,2,1])
solution([10])