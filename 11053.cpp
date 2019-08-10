//
//  dp1.cpp
//  
//
//  Created by 문상혁 on 10/08/2019.
//

#include <stdio.h>
#include <iostream>

using namespace std;

int main() {
    int N; cin >> N;
    int A[N];
    for(int i=0; i<N; i++) {
        cin >> A[i];
    }
    int D[N]; int pos = 0; D[0] = 1;
    for(int i=1; i<N; i++) {
        if(A[pos] < A[i]) {
            D[i] = D[pos]+1; pos = i;
        } else {
            D[i] = 1;
        }
    }
    cout << D[pos] << endl;
}
