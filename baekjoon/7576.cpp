//
// 19.07.30
// baekjoon online judge 7576
//

#include <iostream>
#include <queue>

using namespace std;

// put x,ys in queue;
queue<pair<int,int> > que;

// to determine which points are available
int a[4] = {1,0,-1,0};
int b[4] = {0,1,0,-1};

int tomato() {
    int M, N;
    int day = 0;
    int count = 0;
    
    cin >> N >> M;
    int array[1000][1000];
    for(int i=0; i<M; i++) {
        for(int j=0; j<N; j++) {
            cin >> array[i][j];
            if(array[i][j] == 1) {
                que.push(pair<int, int>(i,j));
            }
        }
    }
    while(!que.empty()) {
        // make variables x, y to save the point of where the rotten tomato is
        int x = que.front().first;
        int y = que.front().second;
        day = array[x][y];
        // 하나씩 돌면서 범위 체크, 0이면 1로 올리고 1로 바뀐 것들은 큐에 저장
        for(int i=0; i<4; i++) {
            if(x+a[i]<0 || x+a[i]>=M || y+b[i]<0 || y+b[i]>=N) continue;
            if(array[x+a[i]][y+b[i]] == 0) {
                array[x+a[i]][y+b[i]] = array[x][y] + 1;
                que.push(pair<int, int>(x+a[i],y+b[i]));
            }
        }
        que.pop();
    }
    
    for(int i=0; i<M; i++) {
        for(int j=0; j<N; j++) {
            if(array[i][j] == 0) {
                count++;
                break;
            }
        }
    }
    if(count == 0) {
        return --day;
    } else {
        return -1;
    }
}

int main() {
    cout << tomato();
}
