//
//  panda.cpp
//  
//
//  Created by 문상혁 on 18/08/2019.
//

#include <stdio.h>
#include <iostream>
#include <vector>

using namespace std;

int max_day = 1;
int n;
vector<vector<int> > v;
vector<vector<int> > dp;
int x[4] = {1,0,-1,0};
int y[4] = {0,1,0,-1};

int findWays(int a, int b) {
    int cnt = 0;
    for(int i=0; i<4; i++) {
        if(a+x[i]<n && b+y[i]<n && a+x[i]>=0 && b+y[i]>=0) {    // 상하좌우
            if(v[a+x[i]][b+y[i]] > v[a][b]) {   // 옆칸이 지금칸보다 클때
                if(dp[a+x[i]][b+y[i]] != 0) {   // dp가 이미 있을때
                    if(dp[a][b] < dp[a+x[i]][b+y[i]]+1) {
                        dp[a][b] = dp[a+x[i]][b+y[i]] + 1;
                    }
                } else {    // 근접칸 dp가 0일때
                    int tmp = findWays(a+x[i],b+y[i]) + 1;
                    if(dp[a][b] < tmp) dp[a][b] = tmp;
                }
            } else { cnt++; }   // 옆칸이 지금 칸보다 작아서 못갈때
        } else { cnt++; }
    }
    if(cnt == 4) {
        dp[a][b] = 1;
    }
    return dp[a][b];
}

int main() {
    cin >> n;
    for(int i=0; i<n; i++) {
        vector<int> t; vector<int> d;
        for(int j=0; j<n; j++) {
            int tmp; cin >> tmp;
            t.push_back(tmp);
            d.push_back(0);
        }
        v.push_back(t);
        dp.push_back(d);
        t.clear(); d.clear();
    }
    for(int i=0; i<n; i++) {
        for(int j=0; j<n; j++) {
           findWays(i,j);
            int tmp = dp[i][j];
            if(tmp > max_day) max_day = tmp;
        }
    }
    cout << max_day << endl;
}
