function solution(x) {
	var answer = true;
	let sum = 0;
	for (let i = 0; i < String(x).length; i++) {
		sum += Number(String(x)[i]);
	}
	answer = x % sum === 0 ? true : false;
	console.log(answer);
	return answer;
}

solution(10);
solution(12);
solution(11);
solution(13);
