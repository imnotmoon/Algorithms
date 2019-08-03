//
//  tree.cpp
//  
//
//  Created by 문상혁 on 02/08/2019.
//

#include <stdio.h>
#include <iostream>

using namespace std;

int max(int arr[]) {
    int tmp = 0;
    for(int i=0; i<100; i++) {
        if(arr[i] > tmp) {
            tmp = arr[i];
        }
    }
    return tmp;
}

int binarySearch(int arr[], int tree[], int size, int find) {
    int left = 0; int right = size; int mid = (left+right)/2;
    int min;
    while(left<=right) {
        int total = 0;
        cout << "mid : " << mid << endl;
        for(int i=0; i<size; i++) {
            // tree를 돌면서 mid 이상의 값을 더해서 찾으려는 수가 나오는지 확인
            if(tree[i] - mid > 0) {
                total = total + (tree[i]-mid);
            }
        }
        cout << "total : " << total << endl;
        if(total == find) {
            return mid;
        } else if(total > find) {
            left = mid;
            min = mid;
            mid = (left+right)/2;
        } else {
            right = mid;
            mid = (left+right)/2;
        }
        if(left == mid) {
            break;
        } else if(mid == right) {
            break;
        }
    }
    return min;
}

int main() {
    int M, N;
    cin >> N >> M;
    // 배열 생성
    int tree[1000000] = {0};
    for(int i=0; i<N; i++) {
        cin >> tree[i];
    }
    int size = max(tree);
    int arr[size];
    for(int i=0; i<size; i++) {
        arr[i] = i+1;
    }
    cout << binarySearch(arr, tree, size, M) << endl;
}
