#include <iostream>
#include <vector>

using namespace std;

int main() {
    vector<int> v; int len = 0;
    cout << "정렬할 배열의 크기 : " << endl; cin >> len;
    cout << "숫자 입력 : " << endl;
    for(int i=0; i<len; i++) { int t; cin >> t; v.push_back(t); }

    // Selection Sort //
    for(int i=0; i<len; i++) {
        int min = i;
        for(int j=i+1; j<len; j++) {
            if(v[min] > v[j]) { min = j; }
        }
        int tmp = v[i]; v[i] = v[min]; v[min] = tmp; 
    }
    cout << endl;
    for(int i=0; i<len; i++) {
        cout << v[i] << " ";
    }
    cout << endl;
}