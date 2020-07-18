//
//  a.cpp
//  
//
//  Created by 문상혁 on 02/01/2020.
//

#include <stdio.h>
#include <iostream>
#include <vector>

using namespace std;

int N;

int main() {
    cin >> N;
    vector<int> dp(N+1,10000);
    dp[1] = 0;
    for(int i=1; i<N; i++) {
        if(dp[i+1] > dp[i]+1) dp[i+1] = dp[i] + 1;
        if(i*2<=N && dp[i*2] > dp[i]+1) dp[i*2] = dp[i] + 1;
        if(i*3<=N && dp[i*3] > dp[i]+1) dp[i*3] = dp[i] + 1;
//        for(int j=1; j<=N; j++) {
//            cout << dp[j] << " ";
//        }
//        cout << endl;
    }
    cout << dp[N] << endl;
}
