function solution(places) {
	return places.map((place) => {
		for (let i = 0; i < 5; i++) {
			for (let j = 0; j < 5; j++) {
				if (place[i][j] === "P" && !bfs(place, i, j)) return 0;
			}
		}
		return 1;
	});
}

function bfs(place, i, j) {
	const [dy, dx] = [
		[0, 1, 0, -1],
		[1, 0, -1, 0],
	];
	const queue = [[i, j, 0]];
	while (queue.length) {
		const [y, x, d] = queue.shift();
		if (d > 2) continue;
		if (y !== i || x !== j) {
			if (place[y][x] === "P") {
				return false;
			}
		}
		for (let i = 0; i < 4; i++) {
			const [yy, xx] = [y + dy[i], x + dx[i]];
			if (yy >= 0 && yy < 5 && xx >= 0 && xx < 5) {
				if (place[yy][xx] === "X") continue;
				queue.push([yy, xx, d + 1]);
			}
		}
	}
	return true;
}

console.log(
	solution([
		// ["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
		["POOPX", "OXPXP", "PXXXO", "OXXXP", "OOOPO"],
		// ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"],
		// ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
		// ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"],
	])
);
