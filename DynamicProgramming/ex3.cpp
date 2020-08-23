// 백준 11727

// 앞에 이미 특정 길이만큼 타일이 갖춰졌다 생각하고
// +1이면 한가지 경우
// +2이면 2가지 // 이외의 경우는 없음
// D[n] = D[n-1] + 2xD[n-2]

#include <stdio.h>

int d[1001];

int dp(int x) {
    if(x == 1) return 1;
    if(x == 2) return 3;
    if(d[x] != 0) return d[x];
    return d[x] = (dp(x-1) + 2 * dp(x-2)) % 10007;
    // 나머지를 출력하라고 하는 경우는 값이 커지는 경우
}

int main(void) {
    int x;
    scanf("%d", &x);
    printf("%d", dp(x));
}