#include <iostream>
#include <vector>

using namespace std;

int main() {
    vector<int> v; int len = 0;
    cout << "정렬할 배열의 크기 : " << endl; cin >> len;
    cout << "숫자 입력 : " << endl;
    for(int i=0; i<len; i++) { int t; cin >> t; v.push_back(t); }

    // Insertion Sort //
    for(int i=1; i<len; i++) {
        cout << i << "th" << endl;
        int j=i;
        while(j-1>=0) {
            if(v[j] < v[j-1]) { int t=v[j]; v[j] = v[j-1]; v[j-1] = t; j--; }
            else { j--; break; }
        }
    }

    cout << endl;
    for(int i=0; i<len; i++) {
        cout << v[i] << " ";
    }
    cout << endl;
}