let visited;

function solution(n, computers) {
	let answer = 0;
	visited = Array(n).fill(false);
	for (let i = 0; i < n; i++) {
		if (!visited[i]) answer++;
		else continue;
		const queue = [i];
		while (queue.length) {
			const current = queue.shift();
			visited[current] = true;
			for (let j = 0; j < n; j++) {
				if (j !== current && computers[current][j] && !visited[j]) {
					queue.push(j);
				}
			}
		}
	}

	return answer;
}

console.log(
	solution(3, [
		[1, 1, 0],
		[1, 1, 0],
		[0, 0, 1],
	])
);
