// kakao #2 최소 횟수로 물건 옮기기

function solution(weight) {
	let result = 0;
	weight.sort((a, b) => a - b);

	while (weight.length) {
		const current = weight.shift();

		let [left, right] = [0, weight.length - 1];
		let pos = -1;
		while (left < right) {
			const mid = Math.floor((left + right) / 2);
			if (weight[mid] + current > 3.0) {
				right = mid;
			} else {
				pos = mid;
				left = mid + 1;
			}
		}
		if (pos > -1) {
			weight.splice(pos, 1);
		}
		result += 1;
	}
	return result;
}

console.log(solution([1.4, 1.01, 2.4, 1.01, 1.01]));
