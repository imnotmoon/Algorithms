//
//  coin2.cpp
//  
//
//  Created by 문상혁 on 10/08/2019.
//

#include <stdio.h>
#include <iostream>

using namespace std;

int memoirize[101];
int n;

int dp(int *arr, int k) {
    for(int i=0; i<n; i++) {
        /*
        for(int j=1; j<=15; j++) {
            cout << memoirize[j] << " ";
        }
         */
        if(k>=arr[i]) {  // dynamic programming
            if(memoirize[k-arr[i]] == 10000) {
                memoirize[k-arr[i]] = dp(arr,k-arr[i]);
                memoirize[k] = memoirize[k-arr[i]]+1;
            } else if(memoirize[k] > memoirize[k-arr[i]]+1) {
                memoirize[k] = memoirize[k-arr[i]]+1;
            }
        }
    }
    return memoirize[k];
}

int main() {
    int k;
    cin >> n >> k;
    int arr[n];
    for(int i=0; i<n; i++) {
        cin >> arr[i];
    }
    for(int i=1; i<=k; i++) {
        memoirize[i] = 10000;
    }
    for(int i=0; i<n; i++) {
        memoirize[arr[i]] = 1;
    }
    cout << dp(arr, k) << endl;
}
