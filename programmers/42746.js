function solution(numbers) {
	numbers = numbers.map((i) => `${i}`);
	let answer = numbers.sort((a, b) => b + a - (a + b)).reduce((prev, cur) => prev + cur, "");
	answer = BigInt(answer).toString();
	return answer;
}

console.log(solution([3, 30, 34, 5, 9]));
