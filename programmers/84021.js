const [dy, dx] = [
	[1, 0, -1, 0],
	[0, 1, 0, -1],
];

function solution(board, table) {
	let answer = 0;
	let spaces = [],
		puzzles = [];

	for (let i = 0; i < table.length; i++) {
		for (let j = 0; j < table.length; j++) {
			board[i][j] === 0 && spaces.push(rotate(resetZero(dfs(board, j, i, 0))));
			table[i][j] === 1 && puzzles.push(rotate(resetZero(dfs(table, j, i, 1))));
		}
	}

	for (const space of spaces) {
		for (let i = 0; i < puzzles.length; i++) {
			if (JSON.stringify(space) === JSON.stringify(puzzles[i])) {
				answer += puzzles[i].length;
				puzzles = puzzles.map((p, idx) => (idx === i ? [] : p));
				break;
			}
		}
	}

	return answer;
}

function dfs(table, x, y, find) {
	const stack = [[x, y]];
	const result = [[x, y]];

	while (stack.length) {
		let [a, b] = stack.pop();
		table[y][x] = -1;
		for (let i = 0; i < 4; i++) {
			const [moveX, moveY] = [a + dx[i], b + dy[i]];
			if (moveX < 0 || moveX >= table.length || moveY < 0 || moveY >= table.length) continue;
			if (table[moveY][moveX] === find) {
				table[moveY][moveX] = -1;
				[stack, result].forEach((l) => {
					l.push([moveX, moveY]);
				});
			}
		}
	}
	return result;
}

function resetZero(lst) {
	const minX = Math.min(...lst.map((c) => c[0]));
	const minY = Math.min(...lst.map((c) => c[1]));
	return lst.map((c) => [c[0] - minX, c[1] - minY]).sort();
}

function rotate(lst) {
	if (lst.length === 1) return lst;
	const result = [];
	let shape = [...lst];
	let width = Math.max(...shape.map((s) => s[1])) - Math.min(...shape.map((s) => s[1]));
	let height = Math.max(...shape.map((s) => s[0])) - Math.min(...shape.map((s) => s[0]));

	for (let i = 0; i < 4; i++) {
		let t = resetZero(shape.map((c) => [c[1], width - c[0]]));
		shape = t;
		result.push(shape);
		[width, height] = [height, width];
	}

	return result.sort()[0];
}

console.log(
	solution(
		[
			[1, 1, 0, 0, 1, 0],
			[0, 0, 1, 0, 1, 0],
			[0, 1, 1, 0, 0, 1],
			[1, 1, 0, 1, 1, 1],
			[1, 0, 0, 0, 1, 0],
			[0, 1, 1, 1, 0, 0],
		],
		[
			[1, 0, 0, 1, 1, 0],
			[1, 0, 1, 0, 1, 0],
			[0, 1, 1, 0, 1, 1],
			[0, 0, 1, 0, 0, 0],
			[1, 1, 0, 1, 1, 0],
			[0, 1, 0, 0, 0, 0],
		]
	)
);
