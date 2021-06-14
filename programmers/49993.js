function solution(skill, skill_trees) {
	var answer = 0;

	skill_trees.forEach((tree, idx) => {
		answer += checkSkillTree(skill, tree);
	});

	console.log(answer);
	return answer;
}

const checkSkillTree = (skill, tree) => {
	// "CBD", "BACDE"
	let result = [];
	for (let i = 0; i < skill.length; i++) {
		let t = tree.indexOf(skill[i]);
		result.push(t);
	}
	console.log(result);

	let ret = 1;

	for (let i = 0; i < result.length; i++) {
		if (result[i] == -1) {
			if (i != result.length - 1 && result[i + 1] > -1) ret = 0;
			continue;
		}
		if (i > 0) {
			if (result[i - 1] > result[i]) ret = 0;
		}
	}

	console.log("ret : ", ret);
	return ret;
};

solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]);
