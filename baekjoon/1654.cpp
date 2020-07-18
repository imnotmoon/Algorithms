//
//  wire.cpp
//  
//
//  Created by 문상혁 on 19/08/2019.
//

#include <stdio.h>
#include <iostream>
#include <vector>

using namespace std;

vector<int> range;
int N, K;

int findProperNumber(int *arr, int front, int end) {
    int mid = (front+end)/2;
    int total = 0;
    for(int i=0; i<N; i++) {
        total += arr[i]/range[mid];
    }
    if(total == K) return mid;
    if(total > K) {
        return findProperNumber(arr, mid, end);
    } else if(total < K) {
        return findProperNumber(arr, front, mid);
    }
    return -1;
}

int main() {
    cin >> N >> K;
    int arr[N];
    int sum = 0;
    int total = 0;
    for(int i=0; i<N; i++) {
        cin >> arr[i];
        sum += arr[i];
    }
    sum = sum/K;
    for(int i=0; i<sum; i++) {
        range.push_back(i);
    }
    int tmp = findProperNumber(arr,0,sum);
    while(true) {
        for(int i=0; i<N; i++) {
            total += arr[i]/tmp;
        }
        if(total < K) break;
        total = 0;
        tmp++;
    }
    cout << tmp-1 << endl;
}
