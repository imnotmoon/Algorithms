function solution(record) {
	const nicknames = new Map();
	return record
		.map((rec) => {
			const [command, uid, nickname] = rec.split(" ");
			if (command !== "Leave") nicknames.set(uid, nickname);
			return rec;
		})
		.map((rec) => {
			const [command, uid] = rec.split(" ");
			return command === "Enter"
				? `${nicknames.get(uid)}님이 들어왔습니다.`
				: command === "Leave"
				? `${nicknames.get(uid)}님이 나갔습니다.`
				: undefined;
		})
		.filter((s) => s);
}

console.log(
	solution([
		"Enter uid1234 Muzi",
		"Enter uid4567 Prodo",
		"Leave uid1234",
		"Enter uid1234 Prodo",
		"Change uid4567 Ryan",
	])
);
