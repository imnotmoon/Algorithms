// 20.08.01 21:30 정답
// 클래스로 풀기 싫었는데 어찌어찌 풀음

#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int N, M;   // N : 문제 갯수    // M : 응시자 수
vector<int> q;
vector<int> totalOfAll;

class Tester {
public:
    int testNumber;
    vector<char> ox;

    Tester(int testNumber, vector<char> ox) {
        this->testNumber = testNumber;
        this->ox = ox;
    }

    bool operator <(const Tester &tester)const {
        return this->testNumber < tester.testNumber;
    }
};

vector<Tester> v;

int calcScoreAndFindFirst() {
    for(int i=0; i<M; i++) {
        int total = 0;
        for(int j=0; j<N; j++) {
            if(v[i].ox[j] == 'O') total += q[j];
        }
        totalOfAll.push_back(total);
        // cout << v[i].testNumber << " : " << total << endl;
    }
    int max = 0;
    for(int i=0; i<M; i++) {
        if(totalOfAll[i] > totalOfAll[max]) max = i;
    }
    return max;
}

int main() {
    cin >> N >> M;
    for(int i=0; i<N; i++) {
        int t; cin >> t; q.push_back(t);
    }
    for(int i=0; i<M; i++) {
        int number; cin >> number;
        vector<char> ox;
        for(int j=0; j<N; j++) {
            char c; cin >> c; ox.push_back(c);
        }
        v.push_back(Tester(number, ox));
    }
    sort(v.begin(), v.end());

    int max = calcScoreAndFindFirst();

    cout << v[max].testNumber << " " << totalOfAll[max];
}
