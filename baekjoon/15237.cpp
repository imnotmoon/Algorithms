// 20.08.01 23:53 정답
// 계수정렬

#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int N; long long C;

vector<long long> code;
vector<pair<long long, long long> > frequency;  // first : number   // second : frequency

bool compare(pair<long long, long long> a, pair<long long, long long> b) {
    if(a.second > b.second) return true;
    else if(a.second == b.second) {
        // frequency가 같을 경우 먼저 입력한 값에 우선순위를 줌
        if(find(code.begin(), code.end(), a.first) < find(code.begin(), code.end(), b.first)) return true;
    }
    return false;
}

void frequencySorting() {
    sort(frequency.begin(), frequency.end(), compare);
    for(long long i=0; i<frequency.size(); i++) {
        for(long long j=0; j<frequency[i].second; j++) {
            cout << frequency[i].first << " ";
        }
    }
}

int main() {
    // 입력
    cin >> N >> C;
    for(int i=0; i<N; i++) {
        long long t; cin >> t; code.push_back(t);
    }
    // frequency 배열 세팅
    for(int i=0; i<N; i++) {
        int alreadyIn = 0;
        for(long long j=0; j<frequency.size(); j++) {
            if(frequency[j].first == code[i]) {
                frequency[j].second++;
                alreadyIn = 1;
                break;
            }
        }
        if(alreadyIn == 0) {
            pair<long long, long long> p; p.first = code[i]; p.second = 1;
            frequency.push_back(p);
        }
    }
    frequencySorting();
}