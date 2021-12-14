/**
 *
 * @param {Array<number>} citations
 * @returns
 */
function solution(citations) {
	citations.sort((a, b) => +a - +b);
	const [min, max] = [citations[0], citations[citations.length - 1]];
	let answer = min;
	for (let i = min; i < max; i++) {
		for (let j = 0; j < citations.length - 1; j++) {
			if (i >= citations[j] && i <= citations[j + 1]) {
				if (j + 1 <= i && citations.length - j - 1 >= i) answer = Math.max(answer, i);
			}
		}
	}
	return Math.min(citations.length, answer);
}

console.log(solution([22, 42]));
