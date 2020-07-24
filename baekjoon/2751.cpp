#include <iostream>
#include <stdio.h>  // 이거써야되네
#include <algorithm>

using namespace std;

int main() {
    int n; int v[1000000]; scanf("%d", &n);
    for(int i=0; i<n; i++) { scanf("%d", &v[i]); }

    // 야매
    sort(v, v+n);

    for(int i=0; i<n; i++) { printf("%d\n", v[i]); }
}