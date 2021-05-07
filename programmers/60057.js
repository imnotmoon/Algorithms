function solution(s) {
	let length = [];
	let result = "";

	if (s.length === 1) return 1;

	for (let cut = 1; cut < s.length / 2 + 1; cut += cut) {
		let count = 1;
		let tempStr = s.slice(0, cut);

		for (let i = cut; i < s.length; i += cut) {
			if (s.slice(i, i + cut) === tempStr) {
				// console.log(tempStr, s.slice(i, i + cut));
				count += 1;
			} else {
				if (count === 1) count = "";
				result += `${count}${tempStr}`;
				tempStr = s.slice(i, i + cut);
				count = 1;
			}
		}

		if (count === 1) count = "";
		result += `${count}${tempStr}`;
		// console.log(result);
		length.push(result.length);
		result = "";
	}
	// console.log(length);
	// console.log(Math.min(...length));
	return Math.min(length);
}

// solution("aabbaccc");
// solution("ababcdcdababcdcd");
solution("xababcdcdababcdcd");
