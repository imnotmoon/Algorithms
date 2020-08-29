#include <iostream>
#include <queue>
#include <vector>

// 헷갈리던거
// 1. 노드를 만들어야하나? : 그럴필요 없음. 그냥 인덱스를 노드처럼 쓴다.
// 2. 그래프를 그려야 하나? : 그래프 안그리고 인접리스트로 푼다.
//     그래프로 입력받더라도 인접리스트로 바꾸는 과정이 필요한가? : 몰라

using namespace std;

int number = 7;
int c[7];   // visited, checked
vector<int> a[8];   // index start with 1   // 8개의 벡터가 들어가는 배열임.(2차원)

void bfs(int start) {
    queue<int> q;   // 큐 사용
    q.push(start);
    c[start] = true;
    while(!q.empty()) {
        int x = q.front();
        q.pop();
        printf("%d ", x);
        for(int i=0; i<a[x].size(); i++) {  // 인접한 노드들 방문
            int y = a[x][i];
            if(!c[y]) {
                q.push(y);
                c[y] = true;
            }
        }
    }
}

int main(void) {
    // 연결여부를 표현
    // 1과 2를 연결
    a[1].push_back(2);
    a[2].push_back(1);

    a[1].push_back(3);
    a[3].push_back(1);

    a[2].push_back(3);
    a[3].push_back(2);

    .
    .
    .

    bfs(1); // 시작점 1
    return 0;
}