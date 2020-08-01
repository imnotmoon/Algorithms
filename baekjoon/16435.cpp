// 20.08.01. 21:44 정답

#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

vector<int> fruits;
int N, L;

int main() {
    cin >> N >> L;
    for(int i=0; i<N; i++) {    // 과일 위치 입력
        int t; cin >> t; fruits.push_back(t);
    }
    sort(fruits.begin(), fruits.end());
    // 초기 스네이크버드의 길이가 제일 낮은 과일도 못먹는지
    if(fruits[0] > L) {
        cout << L;
        return 0;
    } else {
        for(int i=0; i<N; i++) {
            if(L >= fruits[i]) L++;
            else break;
        }
    }
    cout << L;
}