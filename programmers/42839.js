const isPrime = (n) => {
	if (n <= 1) return false;
	for (let i = 2; i <= Math.sqrt(n); i++) {
		if (n % i === 0) return false;
	}
	return true;
};

function solution(numbers) {
	let answer = 0;
	const used = Array.from({ length: numbers.length }).map(() => 0);
	const v = {};

	(function f(depth, n) {
		if (depth > 0) {
			if (!v[+n] && isPrime(+n)) {
				answer++;
				v[+n] = 1;
			}
		}
		if (depth === numbers.length) return;
		for (let i = 0; i < numbers.length; i++) {
			if (used[i]) continue;
			used[i] = 1;
			f(depth + 1, n + numbers[i]);
			used[i] = 0;
		}
	})(0, "");

	return answer;
}
