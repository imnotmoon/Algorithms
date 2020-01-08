//
//  3naver.cpp
//  
//
//  Created by 문상혁 on 08/01/2020.
//

#include <stdio.h>
#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

// longest/2 - 1 up
// (sum_else + 1) * 2 = longest

int A, B, C;

string solution(int a, int b, int c) {
    vector<pair<char,int> > v; pair<char,int> t;
    string ret;
    t.first = 'a'; t.second = a; v.push_back(t);
    t.first = 'b'; t.second = b; v.push_back(t);
    t.first = 'c'; t.second = c; v.push_back(t);
    
    // sort - 숫자가 3개라 이게 빠름 O(1)
    if(v[0].second > v[1].second) swap(v[0], v[1]);
    if(v[1].second > v[2].second) swap(v[1], v[2]);
    if(v[0].second > v[1].second) swap(v[0], v[1]);
    
    int longestWordCanMake = (v[0].second + v[1].second + 1) * 2;
    
    if(longestWordCanMake < v[2].second) {
        // extra case
        for(int i=0; i<longestWordCanMake; i++) {
            ret += v[2].first;
            if(i%2 == 1) {
                if(v[1].second != 0) {
                    ret += v[1].first;
                    (v[1].second)--;
                } else if(v[1].second == 0 && v[0].second != 0) {
                    ret += v[0].first;
                    (v[0].second)--;
                }
            }
        }
    } else {
        // normal case
        for(int i=0; i<v[2].second; i++) {
            ret += v[2].first;
            // 짝수번째마다 끝에 다른 문자 출력
            if(i%2 == 1) {
                if(v[1].second != 0) {
                    (v[1].second)--;
                    ret += v[1].first;
                } else if(v[1].second == 0 && v[0].second != 0) {
                    (v[0].second)--;
                    ret += v[0].first;
                }
            }
        }
        // 입력이 끝났는데 찍어야 할 적은 수의 문자가 남은 경우 ex) 12, 11, 1
        if(v[1].second > 0) {
            if(v[0].second > v[1].second) swap(v[0], v[1]);
            for(int i=0; i<min((v[0].second+1)*2, v[1].second); i++) {
                ret += v[1].first;
                if(i%2 == 1 && v[0].second != 0) {
                    ret += v[0].first;
                    (v[0].second)--;
                }
            }
        }
        // 그래도 남은 경우 ex 10, 10, 10
        for(int i=0; i<1; i++) {
            ret += v[0].first;
        }
    }
    return ret;
}

int main() {
    cin >> A >> B >> C;
    
    cout << solution(A, B, C) << endl;
}
