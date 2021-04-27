let numArray = [];
const arr = [
	["+", "-", "*"],
	["+", "*", "-"],
	["-", "+", "*"],
	["-", "*", "+"],
	["*", "+", "-"],
	["*", "-", "+"],
];

function solution(expression) {
	const sign = [];
	for (let i = 0; i < expression.length; i++) {
		if (
			expression[i] === "*" ||
			expression[i] === "+" ||
			expression[i] === "-"
		) {
			sign.push(expression[i]);
		}
	}
	expression.split("*").forEach((el) => {
		el.split("+").forEach((elem) => {
			numArray.push(...elem.split("-"));
		});
	});

	for (let i = 0; i < numArray.length; i++) {
		numArray[i] = Number(numArray[i]);
	}

	console.log(numArray);
	console.log(sign);

	let maxNumber = 0;
	let ret = 0;
	for (let i = 0; i < arr.length; i++) {
		// 얕은복사
		ret = calculate(numArray.slice(), sign.slice(), i);
		maxNumber = Math.max(maxNumber, ret);
	}
	return maxNumber;
}

const calculate = (copyNum, copySign, i) => {
	for (let j = 0; j < arr[i].length; j++) {
		for (let k = 0; k < copySign.length; k++) {
			if (copySign[k] === arr[i][j]) {
				// 지금 sign과 순서가 맞음
				if (copySign[k] === "*") {
					// *로 같을 경우
					copyNum[k] *= copyNum[k + 1];
					copyNum.splice(k + 1, 1);
					copySign.splice(k, 1);
					k -= 1;
				} else if (copySign[k] === "+") {
					// +로 같을 경우
					copyNum[k] += copyNum[k + 1];
					copyNum.splice(k + 1, 1);
					copySign.splice(k, 1);
					k -= 1;
				} else if (copySign[k] === "-") {
					// -로 같을 경우
					copyNum[k] -= copyNum[k + 1];
					copyNum.splice(k + 1, 1);
					copySign.splice(k, 1);
					k -= 1;
				}
			}
		}
	}
	return Math.abs(copyNum[0]);
};

solution("100-200*300-500+20");
// solution("50*6-3*2");
