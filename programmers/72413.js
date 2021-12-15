let dp = [];

function solution(n, s, a, b, fares) {
	let answer = 0;
	dp = Array.from(Array(n + 1), () => Array(n + 1).fill(Infinity));
	for (let i = 0; i < fares.length; i++) {
		const [c, d, f] = fares[i];
		dp[d][c] = dp[c][d] = f;
	}
	for (let i = 0; i < n + 1; i++) {
		dp[i][i] = 0;
	}
	floydWarshall(n);

	answer = Math.min(dp[s][a] + dp[a][b], dp[s][b] + dp[b][a], dp[s][a] + dp[s][b]);

	for (let i = 1; i < n + 1; i++) {
		if (i === a || i === b) continue;
		answer = Math.min(dp[s][i] + dp[i][b] + dp[i][a], answer);
	}
	return answer;
}

function floydWarshall(n) {
	for (let k = 1; k < n + 1; k++) {
		for (let j = 1; j < n + 1; j++) {
			for (let i = 1; i < n + 1; i++) {
				if (dp[i][k] + dp[k][j] < dp[i][j]) dp[i][j] = dp[i][k] + dp[k][j];
			}
		}
	}
}

console.log(
	solution(6, 4, 6, 2, [
		[4, 1, 10],
		[3, 5, 24],
		[5, 6, 2],
		[3, 1, 41],
		[5, 1, 24],
		[4, 6, 50],
		[2, 4, 66],
		[2, 3, 22],
		[1, 6, 25],
	])
);
