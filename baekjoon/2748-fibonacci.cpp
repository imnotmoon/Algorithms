//
//  a.cpp
//  
//
//  Created by 문상혁 on 26/07/2019.
//

#include <stdio.h>
#include <iostream>

using namespace std;

int main() {
    int fib[3];
    fib[0] = 0; fib[1] = 1; fib[2] = 1;
    
    int n;
    cin >> n;
    
    for(int i=0; i<n; i++) {
        fib[i%3] = fib[(i+1)%3] + fib[(i+2)%3];
    }
    
    cout << fib[n%3] << endl;
}

