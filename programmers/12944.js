function solution(arr) {
	var answer = arr.reduce((acc, cur) => (acc += cur), 0) / arr.length;
	return answer;
}

solution([1, 2, 3, 4]);
solution([5, 5]);
