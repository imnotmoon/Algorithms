//
//  blackjack.cpp
//  
//
//  Created by 문상혁 on 20/08/2019.
//

#include <stdio.h>
#include <iostream>
#include <vector>

using namespace std;

int main() {
    int N, M;
    cin >> N >> M;
    int arr[N];
    vector<int> v;
    
    for(int i=0; i<N; i++) {
        cin >> arr[i];
    }
    
    int sum = 0;
    for(int i=0; i<N-2; i++) {
        for(int j=i+1; j<N-1; j++) {
            for(int k=j+1; k<N; k++) {
                sum = arr[i] + arr[j] + arr[k];
                if(sum == M) {
                    cout << sum << endl;
                    return 1;
                } else if(sum < M) {
                    v.push_back(sum);
                }
                sum = 0;
            }
        }
    }
    int max = 0;
    for(int i=0; i<v.size(); i++) {
        if(v[i] > max) max = v[i];
    }
    cout << max << endl;
}
