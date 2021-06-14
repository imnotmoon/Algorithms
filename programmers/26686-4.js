function solution(board) {
	var answer = 0;

	let dp = [];
	for (let i = 0; i < board.length; i++) {
		let t = [];
		for (let j = 0; j < board[i].length; j++) {
			if (i == 0 || j == 0) {
				if (board[i][j] == 1) t.push(1);
				else t.push(0);
			} else {
				t.push(0);
			}
		}
		dp.push(t);
	}

	if (board.length == 1 || board[0].length == 1) {
		return 1;
	}

	for (let i = 1; i < dp.length; i++) {
		for (let j = 1; j < dp[i].length; j++) {
			if (board[i][j] == 1) {
				dp[i][j] =
					Math.min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1;
			}
			if (answer < dp[i][j]) answer = dp[i][j];
		}
	}

	console.log(answer ** 2);

	return answer ** 2;
}

solution([
	[0, 1, 1, 1],
	[1, 1, 1, 1],
	[1, 1, 1, 1],
	[0, 0, 1, 0],
]);
