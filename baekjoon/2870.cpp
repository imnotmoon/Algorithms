// 20.07.25. 04:14 정답

#include <iostream>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;

int n;
vector<string> v;

bool compare(string a, string b) {
    if(a.length() < b.length()) {
        return true;
    } else if(a.length() > b.length()) {
        return false;
    } else {
        for(int i=0; i<a.length(); i++) {
            if(a[i] < b[i]) return true;
            else if(a[i] > b[i]) return false;
        }
    }

}

void extractInteger(string s) {
    string total = "";
    bool isNumber = false;
    // bool isFirstZero = true;
    for(int i=0; i<s.length(); i++) {
        int t = s[i] - '0';
        if(t<10) {
            // if(t == 0 && isFirstZero) continue;
            isNumber = true;
            // isFirstZero = false;
            total = total + to_string(t);
        } else {
            if(isNumber) v.push_back(total);
            isNumber = false;
            total = "";
        }
    }
    if(isNumber) v.push_back(total);
}

int main() {
    string str;
    cin >> n;
    for(int i=0 ;i<n; i++) {
        cin >> str;
        extractInteger(str);
    }

    for(int i=0; i<v.size(); i++) {
        // cout << v[i] << endl;
        if(v[i].length() > 0) {
            // cout << "entered" << endl;
            int deleteTo = 0;
            for(int j=0; j<v[i].length()-1; j++) {
                if(v[i][j] == '0') {
                    deleteTo++;
                } else {
                    break;
                }
            }
            v[i].erase(0, deleteTo);
            // cout << "new : " << v[i] << endl;
        }
    }
    sort(v.begin(), v.end(), compare);
    for(int i=0; i<v.size(); i++) {
        cout << v[i] << endl;
    }
}