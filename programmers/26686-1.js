function solution(nums) {
	var answer = 0;

	let cnt = new Set(nums);
	// console.log(cnt);
	if (cnt.size >= nums.length / 2) {
		answer = nums.length / 2;
	} else {
		answer = cnt.size;
	}

	console.log(answer);
	return answer;
}

solution([3, 1, 2, 3]);
solution([3, 3, 3, 2, 2, 4]);
solution([3, 3, 3, 2, 2, 2]);
