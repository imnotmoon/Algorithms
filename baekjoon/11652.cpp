//
//  card.cpp
//  
//
//  Created by 문상혁 on 19/08/2019.
//

#include <stdio.h>
#include <iostream>

using namespace std;

int main() {
    int range[1000000] = {0};

    int N; cin >> N;
    int max = 0;
    for(int i=0; i<N; i++) {
        int t; cin >> t;
        range[t]++;
        if(max < t) max = t;    // 입력한 수 중 최댓값을 저장
    }
    int biggest = 0;
    int i = 0;
    while(i <= max) {
        if(range[i] != 0) {
            if(range[i] > range[biggest]) {
                biggest = i;
            }
        }
        i = i + 1;
    }
    cout << biggest << endl;
}
