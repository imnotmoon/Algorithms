const table = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"];

function solution(s) {
	let answer = s;
	table.forEach((key, idx) => {
		const reg = new RegExp(`${key}`, "g");
		if (answer.includes(key)) answer = answer.replace(reg, `${idx}`);
	});
	return +answer;
}

console.log(solution("one4seveneight"));
