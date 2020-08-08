// 다시풀래서 다시품

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int N;
vector<int> P;
vector<int> dp;

int main() {
    cin >> N;
    for(int i=0; i<N; i++) {
        int t; cin >> t; P.push_back(t);
    }
    sort(P.begin(), P.end());
    int ret = 0; int total = 0;
    dp.push_back(0);
    for(int i=0; i<N; i++) {
        total =  dp[i] + P[i];
        dp.push_back(total);
        ret += total;
    }
    cout << ret << endl;
}