function solution(v) {
	var answer = [];
	let [x, y] = [v[0][0], v[0][1]];
	if (v[1][0] === x) {
		answer.push(v[2][0]);
	} else {
		if (v[2][0] === x) {
			answer.push(v[1][0]);
		} else {
			answer.push(x);
		}
	}
	if (v[1][1] === y) {
		answer.push(v[2][1]);
	} else {
		if (v[2][1] === x) {
			answer.push(v[1][1]);
		} else {
			answer.push(y);
		}
	}

	return answer;
}

solution([
	[1, 4],
	[3, 4],
	[3, 10],
]);
solution([
	[1, 1],
	[2, 2],
	[1, 2],
]);
