const operations = [(a, b) => a + b, (a, b) => a - b, (a, b) => a * b, (a, b) => Math.floor(a / b)];

function getAllNumbersWithGivenNumber(number, dp) {
	const result = new Set([]);
	for (let i = 1; i < number; i++) {
		for (const f of operations) {
			for (const a of dp[i].values()) {
				for (const b of dp[number - i].values()) {
					result.add(f(a, b));
				}
			}
		}
	}
	return result;
}

function solution(N, number) {
	if (number === N) return 1;

	const dp = [];
	dp[1] = new Set([N]);
	for (let i = 2; i < 9; i++) {
		dp[i] = getAllNumbersWithGivenNumber(i, dp);
		dp[i].add(+"".padEnd(i, `${N}`));
		if (dp[i].has(number)) return i;
	}

	return -1;
}

console.log(solution(5, 12));
