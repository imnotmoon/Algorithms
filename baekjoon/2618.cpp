//
//  cop.cpp
//  
//
//  Created by 문상혁 on 24/08/2019.
//

#include <stdio.h>
#include <iostream>
#include <queue>
#include <vector>
#include <cmath> 
using namespace std;

int main() {
    int N; cin >> N;
    int W; cin >> W;
    
    // put in the queue
    queue<pair<int,int> > works;    // 사건 순서 큐 -> 사건의 좌표를 저장
    for(int i=0; i<W; i++) {
        int a, b;
        cin >> a >> b;
        works.push(pair<int,int>(a,b));
    }
    pair<int,int> c1; c1.first = 1; c1.second = 1;  // 경찰차 1번
    pair<int,int> c2; c2.first = N; c2.second = N;  // 경찰차 2번
    
    
    vector<int> order;  // 사건별로 어떤 경찰차가 이동했는지 저장
    int sum = 0;    // 경찰차 총 이동거리
    for(int i=0; i<W; i++) {
        int x = works.front().first;
        int y = works.front().second;
        
        // 각 경찰차로부터 사건의 거리
        int d_c1 = abs(x-c1.first) + abs(y-c1.second);
        int d_c2 = abs(x-c2.first) + abs(y-c2.second);
        
        //cout << d_c1 << " : " << d_c2 << endl;
        
        // 어떤 차가 더 가까운지
        if(d_c1 <= d_c2) {
            order.push_back(1); // 1번 차가 움직였음
            c1.first = x; c1.second = y;    // 1번 차 좌표 수정
            sum += d_c1;
        }
        if(d_c1 > d_c2) {
            order.push_back(2); // 2번 차가 움직였음
            c2.first = x; c2.second = y;    // 2번 차 좌표 수정
            sum += d_c2;
        }
        works.pop();    // 해결 사건 삭제
        
        //cout << "after work " << i+1 << "  / c1 : " << c1.first << " " << c1.second << "  / c2 : " << c2.first << " " << c2.second << endl;
    }
    
    cout << sum << endl;
    for(int i=0; i<W; i++) {
        cout << order[i] << endl;
    }
}
