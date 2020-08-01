// 20.08.01 20:08 정답
// 쉬운데 바보같이 for루프 잘못돌아서 틀림

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> counts;    // love 계산한 결과
vector<string> names;
vector<int> minsik(4, 0);
int n;

void countLetters(string name) {
    int length = name.length();
    vector<int> love(4, 0);
    for(int i=0; i<length; i++) {
        switch(name[i]) {
            case 'L' :
                love[0]++; break;
            case 'O' : 
                love[1]++; break;
            case 'V' :
                love[2]++; break;
            case 'E' :
                love[3]++; break;
        }
    }
    int l = love[0] + minsik[0];
    int o = love[1] + minsik[1];
    int v = love[2] + minsik[2];
    int e = love[3] + minsik[3];

    int ret = ((l+o)*(l+v)*(l+e)*(o+v)*(o+e)*(v+e))%100;
    // cout << name << " " << l << " " << o << " " << v << " " << e << " "<< ret << endl;  
    counts.push_back(ret);
}

int sortByPossibility() {
    int max = 0;    // 최고값이 있는 index
    for(int i=0; i<n; i++) {
        if(counts[i] > counts[max]) max = i;
    }
    return max;
}

int main() {
    string ohminsik; cin >> ohminsik;
    for(int i=0; i<ohminsik.length(); i++) {
        switch(ohminsik[i]) {
            case 'L' :
                minsik[0]++; break;
            case 'O' : 
                minsik[1]++; break;
            case 'V' :
                minsik[2]++; break;
            case 'E' :
                minsik[3]++; break;
        }
    }
    cin >> n;
    for(int i=0; i<n; i++) {
        string name; cin >> name; names.push_back(name);
    }

    sort(names.begin(), names.end());

    for(int i=0; i<n; i++) {
        countLetters(names[i]);
    }

    int max = sortByPossibility();

    cout << names[max];
}