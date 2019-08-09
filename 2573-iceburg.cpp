//
//  iceburg.cpp
//  
//
//  Created by 문상혁 on 07/08/2019.
//

#include <stdio.h>
#include <iostream>
#include <vector>
#include <stack>

using namespace std;

vector<pair<int,int> > exist;       // 빙산좌표
vector<pair<int,int> > iceburg;     // <빙산높이, 인접바다>

vector<pair<int,int> > visited;
stack<pair<int,int> > s;

int a[4] = {1,0,-1,0};
int b[4] = {0,1,0,-1};

int cnt_DFS = 0;

int isVisited(int **arr, int X, int Y) {
    for(int i=0; i<visited.size(); i++) {
        if(pair<int,int>(X,Y) == visited[i]) {
            return 0;   // visited 안에 있을 경우
        }
    }
    return 1;   // visited 안에 없을 경우
}

int DFS(int **arr, int X, int Y) {
    while(!(s.empty()) && s.top().first != -1) {   // 스택이 비지 않았을 때
        int connected = 0;
        for(int i=0; i<4; i++) {
            if(s.top().first+a[i] >= 0 && s.top().first+a[i] < X && s.top().second+b[i] >= 0 && s.top().second+b[i] < Y && arr[s.top().first + a[i]][s.top().second + b[i]] != 0) { // 인접 노드가 arr안에 있고 0이 아닐 경우
                if(isVisited(arr,s.top().first+a[i],s.top().second+b[i]) == 1) {    // 그 인접 노드가 visited 벡터에 없을 때
                    connected++;
                    visited.push_back(pair<int,int>(s.top().first + a[i],s.top().second+b[i]));   // visited에 추가
                    s.push(pair<int,int>(s.top().first+a[i],s.top().second+b[i]));       // 큐에 추가
                    DFS(arr, X, Y);   // 그 인접 노드에 대해 다시 다음 노드를 탐색
                }
            }
        }

        if(s.size() == 1) {
            s.top().first = -1;
        } else {
            s.pop();
        }
    }
    return visited.size();
}

int countLeftIceburgs() {
    int cnt = 0;
    for(int i = 0; i<iceburg.size(); i++) {
        if(iceburg[i].first != 0) {
            cnt++;
        }
    }
    return cnt;
}

void makeVectorIceburg(int X, int Y, int **arr) {   // 현재 있는 빙산 현황으로 iceburg를 재구성
    exist.clear();
    iceburg.clear();
    
    for(int i=0; i<X; i++) {
        for(int j=0; j<Y; j++) {
            if(arr[i][j] > 0) {
                exist.push_back(pair<int,int>(i,j));
                int close = 0;
                for(int k=0; k<4; k++) {
                    if(i + a[k] < X && j + b[k] < Y && i + a[k] >= 0 && j + b[k] >= 0) {
                        if(arr[i + a[k]][j + b[k]] == 0) {
                            close ++;
                        }
                    }
                }
                iceburg.push_back(pair<int,int>(arr[exist[i].first][exist[i].second],close));
            }
        }
    }
    /*
    cout << endl;
    cout << "exist : " << endl;
    for(int i=0; i<exist.size(); i++) {
        cout << "<" << exist[i].first << " " << exist[i].second << ">  ";
    }
    cout << endl;
    cout << "iceburg : " << endl;
    for(int i=0; i<iceburg.size(); i++) {
        cout << "<" << iceburg[i].first << " " << iceburg[i].second << ">  ";
    }
     */
}

void passYear(int X, int Y, int **arr) {
    for(int i=0; i<iceburg.size(); i++) {
        if(arr[exist[i].first][exist[i].second] < iceburg[i].second) {
            arr[exist[i].first][exist[i].second] = 0;
        } else {
            arr[exist[i].first][exist[i].second] -= iceburg[i].second;
        }
    }
    /*
    cout << endl;
    for(int i=0; i<X; i++) {
        for(int j=0; j<Y; j++) {
            cout << arr[i][j] << " ";
        }
        cout << endl;
    }
     */
    makeVectorIceburg(X,Y,arr);
}

int main() {
    int X, Y; cin >> X >> Y;
    int **arr = new int*[X];
    int year = 0;
    for(int i=0; i<X; i++) {
        arr[i] = new int[Y];
    }
    for(int i=0; i<X; i++) {
        for(int j=0; j<Y; j++) {
            cin >> arr[i][j];
            if(arr[i][j] != 0) {
                exist.push_back(pair<int,int>(i,j));
            }
        }
    }
    makeVectorIceburg(X,Y,arr);     // 초기 빙산값
    
    // 빙산 갯수 세기 전 / exist의 첫번째 좌표 -> visited, s
    if(!(exist.empty())) {  // 벡터 empty 되나
        visited.push_back(exist[0]); s.push(exist[0]);
    } else {
        return -1;  // 빙산이 아예 없을경우 -1 리턴
    }
    
    while(DFS(arr,X,Y) == countLeftIceburgs()) {
        //cout << "DFS : " << DFS(arr,X,Y) << "   빙산 수 " << countLeftIceburgs() << endl;
        passYear(X,Y,arr); year++; makeVectorIceburg(X,Y,arr); visited.clear(); s.pop();
        if(!(exist.empty())) {
            visited.push_back(exist[0]); s.push(exist[0]);
        }
    }
    cout << year << endl;
}
