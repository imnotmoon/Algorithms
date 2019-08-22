//
//  transfer.cpp
//  
//
//  Created by 문상혁 on 22/08/2019.
//

#include <stdio.h>
#include <iostream>
#include <vector>
#include <queue>

using namespace std;

int N, K, M;
int arr[1000][1000] = {0};    // 0 짜리 인덱스 안씀
int connected[1000][1000] = {0};


class Station {
public:
    Station() {
        for(int i=0; i<M; i++) {
            // 입력받은 행렬 순환하면서 그래프행렬에 추가
            for(int j=0; j<K; j++) {
                for(int k=j+1; k<K; k++) {
                    connected[arr[k][i]][arr[j][i]] = 1;
                    connected[arr[j][i]][arr[k][i]] = 1;
                }
            }
        }
    }
    
    bool isConnected(int from, int to) {
        if(connected[from][to] == 1 || connected[to][from] == 1) {
            return true;
        }
        return false;
    }
    
    int bfs() {
        int cnt[1000] = {0};
        cnt[1] = 1;
        queue<int> q;
        q.push(1);
        while(!q.empty()) {
            for(int i=0; i<=N; i++) {
                if(isConnected(q.front(), i)) {
                    if(cnt[i] == 0) {
                        q.push(i);
                        cnt[i] = cnt[q.front()] + 1;
                    }
                }
            }
            q.pop();
        }

        
        return cnt[N];
    }
};

int main() {
    cin >> N >> K >> M;
    for(int i=0; i<M; i++) {
        for(int j=0; j<K; j++) {
            cin >> arr[j][i];
        }
    }
    
    Station s;
    cout << s.bfs() << endl;
}
