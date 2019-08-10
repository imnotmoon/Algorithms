//
//  4673.cpp
//  
//
//  Created by 문상혁 on 11/08/2019.
//

#include <stdio.h>
#include <iostream>

using namespace std;

int numbers[10001];

int selfNumbers(int num) {
    int a = num;
    int arr[4] = {0,0,0,0};
    for(int i=3; i>=0; i--) {
        arr[i] = a%10;
        a = (a-a%10)/10;
    }
    return num + arr[3] + arr[2] + arr[1] + arr[0];
}

int main() {
    for(int i=1; i<10001; i++) {
        numbers[selfNumbers(i)] = -1;
    }
    for(int i=1; i<10001; i++) {
        if(numbers[i] != -1) {
            cout << i << endl;
        }
    }
}
