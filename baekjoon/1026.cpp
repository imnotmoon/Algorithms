// 20.07.25. 04:25 정답

#include <iostream>
#include <algorithm>

using namespace std;

int A[100] = {0};
int B[100] = {0};

bool compare(int a, int b) {
    if(a>b) return true;
    else return false;
}

int main() {
    // B가 클수록 A가 작게
    // 1 2 3 7 8 // B
    // 6 1 1 1 0 // A   // 6+2+3+7 = 18

    int n; cin >> n;
    for(int i=0; i<n; i++) {
        cin >> A[i];
    }
    for(int i=0; i<n; i++) {
        cin >> B[i];
    }

    sort(A, A+n);
    sort(B, B+n, compare);

    long long total = 0;
    for(int i=0; i<n; i++) {
        total = total + A[i]*B[i];
    }
    cout << total;
}