function solution(p) {
	return buildCorrectString(p);
}

function buildCorrectString(u) {
	if (u.length === 0) return u;
	const stack = [];
	let i = 0;
	let [open, close] = [0, 0];
	while (i < u.length) {
		if (u[i] === "(") {
			stack.push("(");
			open += 1;
		} else {
			if (stack.length && stack[stack.length - 1] === "(") stack.pop();
			else stack.push(")");
			close += 1;
		}
		if (open === close) {
			break;
		}
		i++;
	}

	// 균형잡힌 문자열인지?
	if (stack.length === 0) {
		return u.slice(0, i + 1) + buildCorrectString(u.slice(i + 1)); //! Errorable
	} else {
		let r = "(" + buildCorrectString(u.slice(i + 1)) + ")"; //! Errorable
		return (
			r +
			Array.from(u.slice(0, i + 1)).reduce((prev, cur, idx) => {
				if (idx === 0 || idx === i) return prev;
				return cur === "(" ? prev + ")" : prev + "(";
			}, "")
		);
	}
}

console.log(solution("(()())()"));
// console.log(solution(")("));
// console.log(solution("()))((()"));
