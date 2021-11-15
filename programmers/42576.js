function solution(participant, completion) {
	const [p, c] = [participant.sort(), completion.sort()];
	let ret = "";
	for (const i in p) {
		if (p[i] !== c[i]) {
			ret = p[i];
			break;
		}
	}
	return ret;
}
