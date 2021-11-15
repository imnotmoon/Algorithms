function solution(clothes) {
	const parts = new Map();

	clothes.forEach(([name, part]) => {
		if (parts.has(part)) parts.set(part, [...parts.get(part), name]);
		else parts.set(part, [name]);
	});

	let total = 1;
	Array.from(parts.keys()).forEach((key) => {
		total = total * (parts.get(key).length + 1);
	});

	return total - 1;
}

solution([
	["yellowhat", "headgear"],
	["bluesunglasses", "eyewear"],
	["green_turban", "headgear"],
]);
