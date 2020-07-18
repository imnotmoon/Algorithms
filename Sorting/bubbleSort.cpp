#include <iostream>
#include <vector>

using namespace std;

int main() {
    vector<int> v; int len = 0;
    cout << "정렬할 배열의 크기 : " << endl; cin >> len;
    cout << "숫자 입력 : " << endl;
    for(int i=0; i<len; i++) { int t; cin >> t; v.push_back(t); }

    // Bubble Sort //
    for(int i=len-1; i>=0; i--) {
        for(int j=0; j<i; j++) {
            if(v[j] > v[j+1]) { int t = v[j]; v[j] = v[j+1]; v[j+1] = t; } // swap
        }
    }

    cout << endl;
    for(int i=0; i<len; i++) {
        cout << v[i] << " ";
    }
    cout << endl;
}