#include <stdio.h>

int d[100];
// 초기화 안해도 일단 0으로 맞춰져있음

// O(n)으로 줄어든다.
// 원래 트리구조에서 내려갈때마다 두배였는데 dp로 인해서 하나밖에 안거침


int dp(int x) {
    // 재귀함수가 종료되는 조건을 명시해아 함.
    if(x == 1) return 1;
    if(x == 2) return 1;
    if(d[x] != 0) return d[x];
    return dp(x-1) + dp(x-2);
}

int main(void) {
    int n;
    scanf("%d", &n);
    printf("%d", dp(n));
}