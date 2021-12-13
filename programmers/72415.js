const [dy, dx] = [
	[0, 1, 0, -1],
	[1, 0, -1, 0],
];

function solution(board, r, c) {
	const remains = [];
	for (let i = 0; i < 4; i++) {
		for (let j = 0; j < 4; j++) {
			if (board[i][j] > 0) remains.push([i, j, board[i][j]]);
		}
	}
	return backtracking(r, c, remains) + remains.length;
}

function backtracking(curY, curX, remains) {
	if (remains.length === 0) return 0;
	let min = 256;
	const board = Array.from(Array(4), () => new Array(4).fill(0));
	remains.forEach(([y, x, i]) => (board[y][x] = i));

	// 짝을 맞춰야 하는 경우
	if (board[curY][curX] > 0) {
		const currentCard = board[curY][curX];
		const [targetY, targetX] = remains.filter(([y, x, n]) => n === currentCard && (y !== curY || x !== curX))[0];
		const newRemains = remains.filter(([_, __, n]) => n !== currentCard);
		min = Math.min(backtracking(targetY, targetX, newRemains) + findPath(targetY, targetX, curY, curX, board), min);
	}

	// 새 카드 쌍을 찾아야 하는 경우
	else {
		remains.forEach(([y, x], idx) => {
			min = Math.min(backtracking(y, x, remains) + findPath(y, x, curY, curX, board), min);
		});
	}

	return min;
}

function findPath(targetY, targetX, curY, curX, board) {
	const queue = [[curY, curX, 0]];
	const visited = Array.from(Array(4), () => new Array(4).fill(0));
	let min = 16;

	while (queue.length) {
		const [y, x, k] = queue.shift();
		if (y == targetY && x == targetX) {
			min = Math.min(min, k);
			continue;
		}
		if (visited[y][x]) continue;
		visited[y][x] = 1;

		// 상하좌우 4방향
		for (let i = 0; i < 4; i++) {
			const [yy, xx] = [y + dy[i], x + dx[i]];
			if (yy < 4 && yy >= 0 && xx < 4 && xx >= 0 && !visited[yy][xx]) queue.push([yy, xx, k + 1]);
		}

		// ctrl 키를 누른 상태로 4방향
		if (y > 0) {
			// top
			let added = 0;
			for (let i = y - 1; i >= 0; i--) {
				if (board[i][x] > 0) {
					queue.push([i, x, k + 1]);
					added = 1;
					break;
				}
			}
			if (!added) queue.push([0, x, k + 1]);
		}

		if (y < 3) {
			// bottom
			let added = 0;
			for (let i = y + 1; i < 4; i++) {
				if (board[i][x] > 0) {
					queue.push([i, x, k + 1]);
					added = 1;
					break;
				}
			}
			if (!added) queue.push([3, x, k + 1]);
		}

		if (x > 0) {
			// left
			let added = 0;
			for (let i = x - 1; i >= 0; i--) {
				if (board[y][i] > 0) {
					queue.push([y, i, k + 1]);
					added = 1;
					break;
				}
			}
			if (!added) queue.push([y, 0, k + 1]);
		}

		if (x < 3) {
			// right
			let added = 0;
			for (let i = x + 1; i < 4; i++) {
				if (board[y][i] > 0) {
					queue.push([y, i, k + 1]);
					added = 1;
					break;
				}
			}
			if (!added) queue.push([y, 3, k + 1]);
		}
	}
	return min;
}
