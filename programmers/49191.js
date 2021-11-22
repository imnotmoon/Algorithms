function solution(n, results) {
	let answer = 0;
	const board = Array.from({ length: n }).map((_, i) => {
		return Array.from({ length: n }).map((_, j) => (i === j ? 0 : false));
	});

	results.forEach(([a, b]) => {
		board[a - 1][b - 1] = 1;
		board[b - 1][a - 1] = -1;
	});

	for (let i = 0; i < n; i++) {
		for (let a = 0; a < n; a++) {
			for (let b = 0; b < n; b++) {
				if (a === b) continue;
				if (board[a][i] === 1 && board[i][b] === 1) board[a][b] = 1;
				if (board[a][i] === -1 && board[i][b] === -1) board[a][b] = -1;
			}
		}
	}

	board.forEach((r) => {
		if (!r.some((c) => c === false)) answer++;
	});

	return answer;
}

console.log(
	solution(5, [
		[4, 3],
		[4, 2],
		[3, 2],
		[1, 2],
		[2, 5],
	])
);
