// kakao #1 비밀번호 입력하기

function solution(s, keypad) {
	keypad = [
		[keypad[0], keypad[1], keypad[2]],
		[keypad[3], keypad[4], keypad[5]],
		[keypad[6], keypad[7], keypad[8]],
	];

	let total = 0;
	const [dy, dx] = [
		[0, 1, -1],
		[1, -1, 0],
	];

	for (let i = 0; i < s.length - 1; i++) {
		const oneSteps = [];
		let current;
		for (let j = 0; j < 3; j++) {
			for (let k = 0; k < 3; k++) {
				if (keypad[j][k] === s[i]) current = [j, k];
			}
		}

		if (s[i + 1] === s[i]) {
			total += 0;
			continue;
		}
		for (let j = 0; j < 4; j++) {
			for (let k = 0; k < 4; k++) {
				const [yy, xx] = [current[0] + dy[j], current[1] + dx[k]];
				if (yy >= 0 && yy < 3 && xx >= 0 && xx < 3) {
					oneSteps.push(keypad[yy][xx]);
				}
			}
		}
		if (oneSteps.includes(s[i + 1])) total += 1;
		else total += 2;
		console.log(s[i], "to", s[i + 1], total);
	}

	return total;
}

console.log(solution("13722327", "481729356"));
