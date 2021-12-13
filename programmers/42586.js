function solution(progresses, speeds) {
	let answer = [];
	const queue = [...progresses];
	while (queue.length > 0) {
		for (let i = 0; i < queue.length; i++) {
			queue[i] += speeds[i];
		}
		let cnt = 0;
		while (queue.length > 0) {
			if (queue[0] < 100) break;
			queue.shift();
			speeds.shift();
			cnt += 1;
		}
		cnt > 0 && answer.push(cnt);
	}
	return answer;
}

console.log(solution([93, 30, 55], [1, 30, 5]));
