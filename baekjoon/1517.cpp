#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int N;
vector<int> v;
vector<int> sorted_v;   // value, idx

int main() {
    cin >> N;
    for(int i=0; i<N; i++) { 
        int t; cin >> t;
        v.push_back(t); 
        sorted_v.push_back(t); 
    }
    sort(sorted_v.begin(), sorted_v.end());
    for(int i=0; i<sorted_v.size(); i++) {
        cout << sorted_v[i] << " ";
    }
    cout << endl;

    cout << cnt;

    4 6 2 1
    1 2 4 6




}

