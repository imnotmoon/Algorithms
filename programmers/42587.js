function solution(priorities, location) {
	let answer = 0;
	const queue = Array.from({ length: priorities.length }).map((_, idx) => idx);
	while (queue.length) {
		const t = queue.shift();
		const p = priorities.reduce((prev, cur, idx) => {
			if (priorities[prev] < cur) return idx;
			else return prev;
		}, 0);
		if (p !== 0) {
			queue.push(t);
			priorities.push(priorities.shift());
		} else {
			if (t === location) return ++answer;
			else {
				++answer;
				priorities.shift();
			}
		}
	}
}

console.log(solution([2, 3, 3, 2, 9, 3, 3], 3));
