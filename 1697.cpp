//
//  1697.cpp
//  
//
//  Created by 문상혁 on 30/07/2019.
//

#include <iostream>
#include <queue>

using namespace std;

queue <pair<int, int> > que;

int main() {
    int count = 0;
    int N, K;
    cin >> N >> K;
    int visit[100000] = {0}; visit[N] = 1;
    que.push(pair<int,int>(N,1));
    
    while(!(que.front().first == K)) {
        if(que.front().first + 1 <100000 && visit[(que.front().first) + 1] == 0) {
            visit[(que.front().first) + 1] = 1;
            count = que.front().second + 1;
            que.push(pair<int,int>(que.front().first+1,que.front().second+1));
            if(que.front().first+1 == K) break;
        }
        if(que.front().first - 1 > 0 && visit[(que.front().first - 1)] == 0) {
            visit[(que.front().first) - 1] = 1;
            count = que.front().second + 1;
            que.push(pair<int,int>(que.front().first-1,que.front().second+1));
            if(que.front().first-1 == K) break;
        }
        if(que.front().first * 2 < 100000 && visit[(que.front().first) *2] == 0) {
            visit[(que.front().first) * 2] = 1;
            count = que.front().second + 1;
            que.push(pair<int,int>(que.front().first*2,que.front().second+1));
            if(que.front().first*2 == K) break;
        }
        que.pop();
    }
    if(N == K) {
        cout << "0" << endl;
    } else {
        cout << --count << endl;
    }
}
