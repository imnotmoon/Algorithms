// 20.07.25 13:24 정답

#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int main() {
    int n; cin >> n;
    vector<string> v;
    vector<long long> vv;

    for(int i=0; i<n; i++) {
        string t; cin >> t; v.push_back(t);
    }
    for(int i=0; i<n; i++) {
        // cout << "------------" << endl;
        // cout << v[i] << endl;
        string number = v[i];
        long long total = 0;
        for(int j=number.length()-1; j>=0; j--) {
            total = total*10 + (int)(number[j]-'0');
            // cout << total << endl;
        }
        vv.push_back(total);
    }

    sort(vv.begin(), vv.end());
    for(int i=0; i<n; i++) {
        cout << vv.at(i) << endl;
    }
}