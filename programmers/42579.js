function solution(genres, plays) {
	const answer = [];
	const obj = {};
	const sum = {};
	genres.forEach((g, i) => {
		if (!obj[g]) {
			obj[g] = [i];
			sum[g] = +plays[i];
		} else {
			obj[g].push(i);
			sum[g] += +plays[i];
		}
	});
	const sortedSum = Object.entries(sum).sort((a, b) => b[1] - a[1]);
	for (const key of Object.keys(obj)) {
		obj[key] = obj[key].sort((a, b) => plays[b] - plays[a]);
	}
	sortedSum.forEach(([genre]) => {
		if (obj[genre].length === 1) answer.push(obj[genre][0]);
		else answer.push(obj[genre][0], obj[genre][1]);
	});

	return answer;
}

solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]);
