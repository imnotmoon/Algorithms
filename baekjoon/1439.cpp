// 20.08.09 20:58

#include <iostream>
#include <algorithm>
#include <vector>
#include <string>

using namespace std;

string s;
vector<pair<int, int> > zeros;
vector<pair<int, int> > ones;

int flip() {
    // flip 0 to 1
    for(int i=0; i<s.size(); i++) {
        // save pos of zeros in vector zeros
        if(s[i] == '0') {
            int j = i;
            while(j<s.size()) {
                j++;
                if(s[j] == '1') break;
            }
            zeros.push_back(make_pair(i,j-1));
            i = j;
        }
    }
    // flip 1 to 0
    for(int i=0; i<s.size(); i++) {
        if(s[i] == '1') {
            int j = i;
            while(j<s.size()) {
                j++;
                if(s[j] == '0') break;
            }
            ones.push_back(make_pair(i,j-1));
            i = j;
        }
    }
    return min(ones.size(), zeros.size());
}

int main() {
    cin >> s;
    cout << flip();
}