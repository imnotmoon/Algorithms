function solution(bridge_length, weight, truck_weights) {
	let [answer, bridge] = [0, Array.from({ length: bridge_length }).map((_) => 0)];

	while (bridge.some((b) => b > 0) > 0 || truck_weights.length > 0) {
		answer += 1;
		bridge.shift();
		bridge.reduce((prev, cur) => prev + cur, 0) + truck_weights[0] <= weight
			? bridge.push(truck_weights.shift())
			: bridge.push(0);
	}

	return answer;
}

console.log(solution(2, 10, [7, 4, 5, 6]));
console.log(solution(100, 100, [10]));
console.log(solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]));
