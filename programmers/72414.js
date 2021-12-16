// programmers 72414

function solution(play_time, adv_time, logs) {
	let answer = 0;
	let max = 0;
	const length = convertTimeToNumber(play_time);
	const advLength = convertTimeToNumber(adv_time);
	const timeCross = Array(length).fill(0);
	const dp = Array(length - advLength + 2).fill(0);
	const [start, end] = [[], []];

	logs.forEach((duration) => {
		let [s, e] = duration.split("-");
		[s, e] = [convertTimeToNumber(s), convertTimeToNumber(e)];
		start.push(s);
		end.push(e);

		timeCross[s]++;
		timeCross[e]--;
	});

	for (let i = 1; i < length; i++) {
		timeCross[i] += timeCross[i - 1];
	}

	for (let i = 1; i < length; i++) {
		timeCross[i] += timeCross[i - 1];
	}

	let acc = timeCross[advLength - 1];
	let idx = 0;
	for (let i = 0; i < length; i++) {
		if (timeCross[i + advLength] - timeCross[i] > acc) {
			acc = timeCross[i + advLength] - timeCross[i];
			idx = i + 1;
		}
	}
	console.table(timeCross);
	return convertNumberToTime(idx);
}

function convertTimeToNumber(t) {
	return t.split(":").reduce((prev, cur) => prev * 60 + +cur, 0);
}

function convertNumberToTime(t) {
	const ss = t % 60;
	t = Math.floor(t / 60);
	const mm = t % 60;
	t = Math.floor(t / 60);
	return `${`${t}`.padStart(3 - `${t}`.length, 0)}:${`${mm}`.padStart(3 - `${mm}`.length, 0)}:${`${ss}`.padStart(
		3 - `${ss}`.length,
		0
	)}`;
}

// console.log(
// 	solution("99:59:59", "25:00:00", [
// 		"69:59:59-89:59:59",
// 		"01:00:00-21:00:00",
// 		"79:59:59-99:59:59",
// 		"11:00:00-31:00:00",
// 	])
// );

console.log(solution("00:01:00", "00:00:30", ["00:00:10-00:00:30", "00:00:20-00:00:30", "00:00:25-00:00:45"]));
