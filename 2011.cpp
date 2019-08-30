//
//  code.cpp
//  
//
//  Created by 문상혁 on 14/08/2019.
//

#include <stdio.h>
#include <stdlib.h>
#include <iostream>


using namespace std;
char S[5000] = {""};  // input value
int dp[100000] = {0};
int size=0;

bool inRange(int number) {
    if(number <= 26 && number > 0) return true;
    return false;
}

int makeNumber(int front, int end) {
    int ret = 0;
    for(int i=front; i<=end; i++) {
        ret = ret*10 + S[i]-48;
    }
    return ret;
}

int countSet(int front, int end) {
    /*
    cout << endl;
    cout << "reculsive starts" << endl;
    cout << "front : end   " << front << " " << end << endl;
    for(int i=0; i<25114; i++) {
        if(dp[i] != 0) {
            cout << "i = " << i << "    val : " << dp[i] << endl;
        }
    }
    // 이미 갯수를 파악한 수의 경우 그 갯수를 반환
    cout << "looking : " << makeNumber(front, end) << endl;
    */
    if(dp[makeNumber(front, end)] != 0) return dp[makeNumber(front, end)];
    // 숫자 하나일 경우
    if(makeNumber(front,end) == 10 || makeNumber(front,end) == 20) return 1;
    if(front == end) {
        if(makeNumber(front,end) == 0) return 0;
        dp[(int)S[front]-48] = 1; return 1; }
    // 숫자 두개일 경우
    if(front+1 == end) {
        // 10~26
        if(inRange(makeNumber(front, end))) {
            dp[makeNumber(front, end)] = 2; return 2;
        }
        // 26~
        else {
            if(makeNumber(front,end) == 0) return 0;
            dp[makeNumber(front, end)] = 1; return 1;
        }
    }
    // 25114
    
    int cnt = 0;
    if(size > 2) {
        cnt = cnt + countSet(front+1,end);
        if(inRange(makeNumber(front,front+1))) {
            cnt = cnt + countSet(front+2,end);
        }
    }
    dp[makeNumber(front,end)] = cnt;
    return cnt;
}

int main() {
    cin >> S;
    // 자릿수 카운트
    while(true) {
        if(strcmp(&S[size],"") == 0) break;
        size++;
    }
    cout << countSet(0, size-1) << endl;
}
