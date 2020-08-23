// dp 타일링 문제
// 백준 11726 2n 타일링

// n = 1 : 2x1짜리는 2x1 하나로만 가능하다
// n = 2 : 2x2짜리는 2가지
// n = 3 : 2x3짜리는 3가지 경우
// 여기서 규칙성을 찾아야 함 -> 점화식을 세우는게 중요
// + 1칸일 경우에는 1가지 경우밖에 늘지 않음
// + 2칸일 경우에는 (2-1)가지 경우밖에 늘지 않음
// D[n] = D[n-1] + D[n-2]

#include <stdio.h>

int d[1001];

int dp(int x) {
    if(x == 1) return 1;
    if(x == 2) return 2;
    if(d[x] != 0) return d[x];
    return d[x] = (dp(x-1) + dp(x-2)) % 10007;
    // 나머지를 출력하라고 하는 경우는 값이 커지는 경우
}

int main(void) {
    int x;
    scanf("%d", &x);
    printf("%d", dp(x));
}