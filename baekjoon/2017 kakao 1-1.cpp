//  카카오 2017 신입 공채 1차 1번
//  1.cpp
//  
//
//  Created by 문상혁 on 28/08/2019.
//

#include <stdio.h>
#include <iostream>

using namespace std;
int n;

void makeMap(int num1, int num2) {
    char c[n];
    int a = num1; int b = num2;
    // 마지막 자릿수부터 계산
    for(int i=0; i<n; i++) {
        int a_i = a%2; int b_i = b%2;
        if(a_i == 0 && b_i == 0) {
            c[n-i-1] = ' ';
        } else {
            c[n-i-1] = '#';
        }
        // 다음 자릿수 계산
        if(a != 0) {
            a /= 2;
        } else {
            a = 0;
        }
        if(b != 0) {
            b /= 2;
        } else {
            b = 0;
        }
    }
    for(int i=0; i<n; i++) {
        cout << c[i];
    }
}

int main() {
    cin >> n;
    int arr1[n], arr2[n];
    for(int i=0; i<n; i++) {
        cin >> arr1[i];
    }
    for(int i=0; i<n; i++) {
        cin >> arr2[i];
    }
    cout << "[";
    for(int i=0; i<n; i++) {
        cout << '"';
        makeMap(arr1[i], arr2[i]);
        if(i != n-1) cout << '"' << ", ";
        else cout << '"' << "]" << endl;
    }
}
