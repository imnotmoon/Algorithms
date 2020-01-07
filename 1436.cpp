//
//  1436.cpp
//  
//
//  Created by 문상혁 on 07/01/2020.
//

#include <stdio.h>
#include <iostream>
#include <math.h>

using namespace std;

int main() {
    int N; cin >> N;
    int count = 0;
    for(int i=666; i<100000000; i++) {
        int now = i;
        while(now >= 666) {
            if(now % (int)pow(10.0, 3.0) == 666) {
                count++; now = 0;
            } else {
                now = now/10;
            }
        }
        if(count == N) {
            cout << i << endl; break;
        }
    }
}
