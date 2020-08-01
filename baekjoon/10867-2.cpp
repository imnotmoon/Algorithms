// 20.08.01 22:00 정답
// 계수정렬(CountingSort)로 품

#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int N;
vector<int> v;
int countPositive[1001] = {0};
int countNegative[1001] = {0};

void countingSort() {
    for(int i=0; i<N; i++) {
        if(v[i] < 0) countNegative[abs(v[i])]++;
        else countPositive[v[i]]++;
    }
    for(int i=1000; i>=0; i--) {
        if(countNegative[i] != 0) {
            cout << -i << " ";
        }
    }
    for(int i=0; i<1001; i++) {
        if(countPositive[i] != 0) {
            cout << i << " ";
        }
    }
}

int main() {
    cin >> N;
    for(int i=0; i<N; i++) {
        int t; cin >> t; v.push_back(t);
    }
    countingSort();
}