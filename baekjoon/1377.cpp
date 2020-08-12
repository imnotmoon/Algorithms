#include <iostream>
#include <algorithm>
#include <vector> 

using namespace std;

vector<pair<int, int> > sorted;

int main() {
    int n; cin >> n;
    for(int i=0; i<n; i++) {
        int t; cin >> t; sorted.push_back(make_pair(t, i)); // val, idx
    }
    sort(sorted.begin(), sorted.end());
    
    int ret = 0;
    for(int i=0; i<sorted.size(); i++) {
        ret = max(ret, sorted[i].second - i);
    }
    cout << ret+1; return 0;
}