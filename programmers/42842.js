function solution(brown, yellow) {
	let answer = [];
	const candidates = [];
	for (let i = 3; i < brown + yellow; i++) {
		if ((brown + yellow) % i === 0 && (brown + yellow) / i >= i) candidates.push([(brown + yellow) / i, i]);
	}
	candidates.forEach(([x, y]) => {
		if ((y - 2) * (x - 2) === yellow) answer = [x, y];
	});
	return answer;
}

console.log(solution(8, 1));
