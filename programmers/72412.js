const infoMap = new Map();

function combination(s, score, start) {
	const key = s.join("");
	if (infoMap[key]) infoMap[key].push(+score);
	else infoMap[key] = [+score];

	for (let i = start; i < s.length; i++) {
		const t = [...s];
		t[i] = "-";
		combination(t, score, i + 1);
	}
}

function solution(info, query) {
	let answer = [];

	for (let i = 0; i < info.length; i++) {
		const s = info[i].split(" ");
		const score = s.pop();
		combination(s, score, 0);
	}

	for (const key in infoMap) infoMap[key].sort((a, b) => a - b);

	// query
	for (const q of query) {
		const splited = q.split(/ and | /g);
		const score = +splited.pop();
		const key = splited.join("");
		const arr = infoMap[key];

		if (!arr) {
			answer.push(0);
			continue;
		}

		let [left, right] = [0, arr.length];
		while (left < right) {
			let mid = Math.floor((left + right) / 2);
			if (score <= arr[mid]) {
				right = mid;
			} else if (arr[mid] < score) {
				left = mid + 1;
			}
		}
		const result = arr.length - left;
		answer.push(result);
	}

	return answer;
}

console.log(
	solution(
		[
			"java backend junior pizza 150",
			"python frontend senior chicken 210",
			"python frontend senior chicken 150",
			"cpp backend senior pizza 260",
			"java backend junior chicken 80",
			"python backend senior chicken 50",
		],
		[
			"java and backend and junior and pizza 100",
			"python and frontend and senior and chicken 200",
			"cpp and - and senior and pizza 250",
			"- and backend and senior and - 150",
			"- and - and - and chicken 100",
			"- and - and - and - 150",
		]
	)
);
