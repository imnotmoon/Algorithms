//
//  11729-hanoi.cpp
//  
//
//  Created by 문상혁 on 28/07/2019.
//

#include <stdio.h>
#include <iostream>

using namespace std;

void hanoi(int n, int A, int B, int C) {
    if(n==1) {
        cout << A << " -> " << C << endl;
    } else {
        hanoi(n-1, A, C, B);    // n-1개의 탑을 B로 옮김
        cout << A << " -> " << C << endl;   // n-1개 밑의 층을 C로 옮김
        hanoi(n-1, B, A, C);       //   B에 있는 n-1개의 탑을 C로 옮김
    }
}

int main() {
    int n;
    cin >> n;
    hanoi(n,1,2,3);
    cout << "done" << endl;
}

