/**
 *
 * @param {string} number
 * @param {number} k
 */
function solution(number, k) {
	const stack = [];
	for (const n of number) {
		while (k > 0 && stack.length && +stack[stack.length - 1] < +n) {
			stack.pop();
			k -= 1;
		}
		stack.push(n);
	}
	return stack.slice(0, stack.length - k).reduce((prev, cur) => prev + cur, "");
}

console.log(solution("1231234", 3));
