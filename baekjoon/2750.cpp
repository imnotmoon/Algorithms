#include <iostream>
#include <vector>

using namespace std;

int main() {
    int n; vector<int> v; cin >> n;
    for(int i=0; i<n; i++) { int t; cin >> t; v.push_back(t); }

    // Bubble Sort
    for(int i=0; i<n; i++) {
        for(int j=0; j<n-i-1; j++) {
            if(v[j] > v[j+1]) { int t = v[j]; v[j] = v[j+1]; v[j+1] = t; }
        }
    }
    for(int i=0; i<n; i++) { cout << v[i] << endl; }
}