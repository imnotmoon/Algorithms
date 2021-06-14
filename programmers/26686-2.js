function solution(arr) {
	var answer = true;

	let sortedArr = arr.sort((a, b) => a - b);
	for (let i = 0; i < arr.length; i++) {
		if (i + 1 != arr[i]) return false;
	}

	console.log(answer);

	return answer;
}

solution([4, 1, 3, 2]);
solution([4, 1, 3]);
