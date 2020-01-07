//
//  2naver.cpp
//  
//
//  Created by 문상혁 on 07/01/2020.
//

#include <stdio.h>
#include <iostream>

using namespace std;

int members;
int numbersOfRank[100000] = {0};
int highestRank = 0;

int solution(int ranks[members]) {
    int total = 0;

    // 계급별로 몇명씩 있는지 카운트
    for(int i=0; i<members; i++) {
        numbersOfRank[ranks[i]]++;
    }
    
    // 가장 낮은 랭크부터 시작
    for(int i=0; i<highestRank; i++) {
        // 상위 계급자가 없을 경우 보고 안함 -> 있을 경우 보고 횟수 카운트
        if(numbersOfRank[i+1] != 0) {
            total = total + numbersOfRank[i];
        }
    }
    return total;
}

int main() {
    cin >> members;
    int ranks[100000] = {0};   // 아까 이거 안되던데
    for(int i=0; i<members; i++) {
        cin >> ranks[i];
        if(i != 0 && ranks[i] > highestRank) highestRank = ranks[i];
    }
    cout << solution(ranks) << endl;
}
