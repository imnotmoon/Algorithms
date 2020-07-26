// 20.07.25. 13:39 정답

#include <iostream>
#include <algorithm>
#include <vector>
#include <stdio.h>

using namespace std;

int main() {
    int n=0; int target = 0;
    vector<long long> v;
    scanf("%d %d", &n, &target);

    for(int i=0; i<n; i++) {
        // cin >> v[i];
        long long t; scanf("%lld", &t); v.push_back(t);
    }

    sort(v.begin(), v.end());

    printf("%lld", v[target-1]);
}