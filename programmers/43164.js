function solution(t) {
	let remain = {};
	const tickets = {};
	let answer = [];

	t.forEach(([s, e]) => {
		if (tickets[s]) {
			tickets[s].push(e);
		} else {
			tickets[s] = [e];
			remain[s] = {};
		}
		if (remain[s][e]) remain[s][e]++;
		else remain[s][e] = 1;
	});

	for (const k in tickets) {
		tickets[k].sort();
	}

	function backtracking(start, path) {
		if (path.length === t.length + 1) {
			if (answer.length) return;
			answer = path;
			return;
		}
		if (!tickets[start]) return;
		for (let i = 0; i < tickets[start].length; i++) {
			const destination = tickets[start][i];
			if (remain[start][destination]) {
				remain[start][destination]--;
				backtracking(destination, [...path, destination]);
				remain[start][destination]++;
			}
		}
	}

	backtracking("ICN", ["ICN"]);

	return answer;
}

console.log(
	solution([
		["ICN", "COO"],
		["ICN", "BOO"],
		["COO", "ICN"],
		["BOO", "DOO"],
	])
);
