// 백준 2133

// 3xn 크기의 벽을 2x1, 1x2로 채우는 경우
// 앞에 이미 n만큼 길이가 있다하고
// +1 : x
// +2 : 3가지 경우
// 다른 경우는 없음
// D[n] = 3 * D[n-2]. 근데 이게 정답은 아님
// +3 : 3*3 = 9칸을 짝수크기의 타일로는 못채움

// +4 : +2, +2로 쪼개지 못하는 경우가 존재함.
// +4개일때는 2가지 경우가 특별하게 더 존재.
// +6개일때는 2가지 경우가 특별하게 더 존재.
// =>>>> D[n] = 3 * D[n-2] + (2*D[n-4]) + (2*D[n-6]) + ....

#include <stdio.h>

int d[1001];

int dp(int x) {
    if(x == 0) return 1;
    if(x == 1) return 0;
    if(x == 2) return 3;
    if(d[x] != 0) return d[x];

    int result = 3 * dp(x-2);
    for(int i=3; i<=x; i++) {
        if(i%2 == 0) {
            result += 2 * dp(x-i);
        }
    }
    return d[x] = result;
}

int main(void) {
    int x;
    scanf("%d", &x);
    printf("%d", dp(x));
}