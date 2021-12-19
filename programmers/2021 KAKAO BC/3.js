// kakao #3 타짜 어피치

function solution(cards) {
	const size = cards[0];
	cards = cards.slice(1);
	let result = -1;
	const sum = [0, 0, cards[0], cards[1]];
	for (let i = 2; i < cards.length; i++) {
		sum.push(sum[sum.length - 2] + cards[i]);
	}
	console.log(sum);
	const lastSumIndex = sum.length - 1;

	for (let i = 2; i < sum.length; i++) {
		// 소거할 카드 번호 : i
		const deltaForNext = sum[i - 2] - sum[i - 1];
		const deltaForNextNext = sum[i - 1] - sum[i];
		// console.log(sum[lastSumIndex - 1], sum[lastSumIndex]);
		const [last, beforeLast] = [
			i % 2 === lastSumIndex % 2 ? sum[lastSumIndex] + deltaForNextNext : sum[lastSumIndex] + deltaForNext,
			i % 2 === (lastSumIndex - 1) % 2
				? sum[lastSumIndex - 1] + deltaForNextNext
				: sum[lastSumIndex - 1] + deltaForNext,
		];
		console.log(last, beforeLast);
		if (last === beforeLast) {
			result = i - 1;
			break;
		}
	}
	return result;
}

console.log(solution([4, 2, 5, 3, 1]));
