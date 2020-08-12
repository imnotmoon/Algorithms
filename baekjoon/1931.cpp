// 20.08.09 22:05
// 1순위 : 종료시간 / 2순위 : 시작시간

#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int N;
vector<pair<long long, long long> > schedules;

bool compare(pair<long long,long long> a, pair<long long, long long> b) {
    if(a.second < b.second) return true;
    else if(a.second == b.second) {
        if(a.first < b.first) return true;
        else return false;
    }
    return false;
}

int main() {
    cin >> N;
    for(int i=0; i<N; i++) {
        int s, e; cin >> s >> e;
        schedules.push_back(make_pair(s,e));
    }
    sort(schedules.begin(), schedules.end(), compare);

    int ret = 0;
    long long quit = 0;
    // cout << " ------------------- " << endl;
    for(int i=0; i<schedules.size(); i++) {
        if(quit <= schedules[i].first) {
            // cout << schedules[i].first << " : " << schedules[i].second << endl;
            quit = schedules[i].second;
            ret++;
        }
    }
    cout << ret;
}