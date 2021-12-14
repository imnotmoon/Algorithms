function solution(name) {
	let answer = 0;
	let current = Array.from("".padEnd(name.length, "A"));
	name = Array.from(name);
	let i = 0;
	while (JSON.stringify(name) !== JSON.stringify(current)) {
		const [idx, move] = toNearestCharacter(i, current, name);
		i = idx;
		answer += move;
		answer += Math.min(name[i].charCodeAt() - 65, 91 - name[i].charCodeAt());
		current[i] = name[i];
	}
	return answer;
}

function toNearestCharacter(idx, current, name) {
	for (let i = 0; i < current.length; i++) {
		const [left, right] = [(idx + i) % current.length, (idx - i + current.length) % current.length];
		if (name[left] !== "A" && current[left] !== name[left]) {
			return [left, i];
		}
		if (name[right] !== "A" && current[right] !== name[right]) {
			return [right, i];
		}
	}
}

console.log(solution("ABAAAAAAAAABB"));
