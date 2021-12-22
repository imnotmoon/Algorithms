function gcd(w, h) {
	const mod = w % h;
	if (mod === 0) return h;
	return gcd(h, mod);
}

function solution(w, h) {
	const GCD = gcd(w, h);
	return w * h - (w + h - GCD);
}

console.log(solution(8, 12));
