let l = 0;
const delHistory = [];

class Node {
	constructor(idx, prev) {
		this.idx = idx;
		this.prev = prev;
		this.next;
	}
}

function solution(n, k, cmd) {
	let answer = Array(n).fill("O");
	let root = new Node(0);
	let curNode = root;
	let prevNode = root;
	for (let i = 1; i < n; i++) {
		const t = new Node(i, prevNode);
		prevNode.next = t;
		prevNode = t;
		if (i === k) curNode = t;
	}

	cmd.forEach((c) => {
		const [command, count] = c.split(" ");
		let i = 0;
		if (command === "U") {
			while (i < count && curNode.prev) {
				curNode = curNode.prev;
				i++;
			}
		} else if (command === "D") {
			while (i < count && curNode.next) {
				curNode = curNode.next;
				i++;
			}
		} else if (command === "C") {
			delHistory.push(curNode);
			const [prev, next] = [curNode.prev, curNode.next];
			if (prev && next) {
				prev.next = next;
				next.prev = prev;
				curNode = next;
			} else if (prev) {
				prev.next = null;
				curNode = prev;
			} else if (next) {
				next.prev = null;
				curNode = next;
			}
		} else {
			const node = delHistory.pop();
			const [prev, next] = [node.prev, node.next];
			if (prev) {
				prev.next = node;
			}
			if (next) {
				next.prev = node;
			}
		}
	});

	delHistory.forEach((n) => {
		answer[n.idx] = "X";
	});

	return answer.join("");
}

console.log(solution(8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z", "U 1", "C"]));
