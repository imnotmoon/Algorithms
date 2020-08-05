
#include <stdio.h>
#include <iostream>
#include <math.h>

using namespace std;

long long X, Y;

int getZ(long long x, long long y) {
    return floor((double)y/(double)x*100);
}

int binarySearch(int target, long long start, long long end) {
    // cout << start <<  "   " << end << endl;
    if(end - start <= 1) return -1;
    long long middle = (start+end)/2;
    int Z = getZ(X+middle, Y+middle);
    // cout << "middle : " << middle << "   binarySearch Z : " << Z << endl;
    if(Z > target) return middle;
    else if(Z == target) {
        return binarySearch(target, middle, end);
    } else {
        return binarySearch(target, start, middle);
    }
}

int main() {
    cin >> X >> Y;
    int currentZ = getZ(X,Y);
    
    long long ret = binarySearch(currentZ, 0, 1000000000-X);
    // cout << ret << endl;
    if(ret == -1) {
        cout << -1; return 0;
    }
    long long limit = 1;
    for(long long i = ret; i>=0; i--) {
        if(getZ(X+i, Y+i) == currentZ) {
            limit = i; break;
        }
    }
    cout << limit + 1;
}