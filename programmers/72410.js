function solution(new_id) {
	const answer = new_id
		.toLowerCase()
		.replace(/[^\w-_.]/g, "")
		.replace(/\.+/g, ".")
		.replace(/^\.|\.$/g, "")
		.padEnd(1, "a")
		.slice(0, 15)
		.replace(/^\.|\.$/g, "");
	return answer.padEnd(3, answer[answer.length - 1]);
}
