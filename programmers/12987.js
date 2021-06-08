function solution(A, B) {
	var answer = 0;

	let AA = A.sort((a, b) => a - b);
	let BB = B.sort((a, b) => a - b);

	let i = 0; // A idx
	let j = 0; // B idx
	while (i < AA.length && j < BB.length) {
		if (AA[i] < BB[j]) {
			i++;
			j++;
			answer++;
		} else if (AA[i] > BB[j]) {
			j++;
		} else if (AA[i] == BB[j]) {
			j++;
		}
	}

	return answer;
}
