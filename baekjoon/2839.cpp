
#include <iostream>

using namespace std;

int minPack(int N) {
    int num = N;
    int cnt = 0;
    if(N%5 == 0) {
        return N/5;
    } else {
        while(num%5 != 0) {
            num -= 3; cnt++;
            if(num < 0) return -1;
        }
        return cnt+num/5;
    }
}

int main() {
    int N; cin >> N;
    
    cout << minPack(N) << endl;
}
