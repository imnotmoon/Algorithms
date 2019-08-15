//
//  1072.cpp
//  
//
//  Created by 문상혁 on 15/08/2019.
//

#include <stdio.h>
#include <iostream>

using namespace std;

int X, Y;

int binarySearch(int Z) {
    int front = Y; int end = X; int mid = (front + end) / 2;
    while(front+1 != end) {
        if(mid*100/X != Z) return 1;
        front = mid; mid = (front+end)/2;
    }
    return 0;
}

int main() {
    cin >> X >> Y;
    int Z = Y*100/X;
    int ZZ = Z;
    cout << Z << endl;
    // X = 53     Y = 47      Z = 88
    int wins = 0;
    
    
    if(binarySearch(Z) == 0) {
        cout << -1 << endl;
        return 0;
    }

    while(Z == ZZ) {
        wins++;
        Z = (Y+wins)*100/(X+wins);
    }
    cout << wins << endl;
}
