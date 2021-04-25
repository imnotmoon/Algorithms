function solution(n, m) {
    var answer = [];
    let [GCD, LCM] = [0, 0]
    for(let i=1; i<=Math.min(n, m); i++) {
        if(n % i === 0 && m % i === 0) GCD = i
    }
    answer = [GCD, GCD*(n/GCD)*(m/GCD)]
    return answer;
}

solution(3, 12)
solution(2, 5)