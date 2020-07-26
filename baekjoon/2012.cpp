#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int n; cin >> n;
    vector<int> v;
    int vv[500000] = {0};
    for(int i=0; i<n; i++) {
        int t; cin >> t; v.push_back(t);
    }
    sort(v.begin(), v.end());
    // scenario 1. greedy match
    int i=1; int j=0;   // i : 실제등수 // j : 예상등수
    while(i < n) {
        while(j < n) {
            if(i == v[j]) {
                vv[i] = v[j]; v[j] = -1;
                i++; j++;
            } else if(i>v[j]) {
                j++;
            } else if(i<v[j]) {
                i++;
            }
        }
    }

    i=1; j=0;
    while(i<n+1) {
        if(vv[i] == 0) {
            while(j<n) {
                if(v[j]>0) {
                    vv[i] = v[j]; i++; j++;
                } else {
                    j++;
                }
            }
        } else {
            i++;
        }
    }
    int total = 0;
    for(int i=1; i<n+1; i++) {
        total = total + abs(vv[i]-i);
    }
    cout << total;
}
