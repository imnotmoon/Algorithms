function solution(numbers, hand) {
    var answer = '';
    let [currentLeft, currentRight] = [[3,0], [3,2]]
    numbers.forEach((num) => {
        if([1, 4, 7].includes(num)) {
            answer += "L"
            currentLeft = [[1, 4, 7].indexOf(num), 0]
        } else if([3, 6, 9].includes(num)) {
            answer += "R"
            currentRight = [[3, 6, 9].indexOf(num), 2]
        } else {
            let arr = [2, 5, 8, 0]
            // 두 손가락으로부터 거리가 같다면 hand로 결정
            let currentPos = [arr.indexOf(num), 1]
            let [leftThumbToNum, rightThumbToNum] = [Math.abs(currentLeft[0]-currentPos[0]) + Math.abs(currentLeft[1]-currentPos[1]), Math.abs(currentRight[0]-currentPos[0]) + Math.abs(currentRight[1]-currentPos[1])]
            if(leftThumbToNum < rightThumbToNum) {
                answer += "L"
                currentLeft = currentPos
            } else if(leftThumbToNum > rightThumbToNum) {
                answer += "R"
                currentRight = currentPos
            } else {
                if(hand === "right") {
                    answer += 'R'
                    currentRight = currentPos
                } else {
                    answer += 'L'
                    currentLeft = currentPos
                }
            }
        }
    })
    console.log(answer)
    return answer;
}

solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right")
// solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left")
// solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "right")