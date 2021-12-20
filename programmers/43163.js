function solution(begin, target, words) {
	let answer = 50;
	if (!words.includes(target)) return 0;
	const conn = {};
	const visited = {};
	conn[`${begin}`] = [];
	words.forEach((k) => (conn[k] = []));

	words.forEach((word) => {
		visited[word] = false;
		let cnt = 0;
		for (let i = 0; i < word.length; i++) {
			if (word[i] !== begin[i]) cnt++;
		}
		cnt === 1 && conn[`${begin}`].push(word);
	});

	for (let i = 0; i < words.length; i++) {
		for (let j = i + 1; j < words.length; j++) {
			let cnt = 0;
			for (let k = 0; k < begin.length; k++) {
				if (words[i][k] !== words[j][k]) cnt += 1;
			}
			if (cnt === 1) {
				conn[words[i]].push(words[j]);
				conn[words[j]].push(words[i]);
			}
		}
	}

	const queue = [[begin, 0]];
	while (queue.length) {
		const [front, n] = queue.shift();
		visited[front] = true;
		if (front === target) answer = Math.min(answer, n);

		conn[front].forEach((w) => {
			if (!visited[w]) queue.push([w, n + 1]);
		});
	}

	return answer;
}

console.log(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]));
