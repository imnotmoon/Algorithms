// 20.08.08 19:09
// 김진영이 듣도 못한 사람의 명단과, 보도 못한 사람의 명단이 주어질 때, 듣도 보도 못한 사람의 명단을 구하는 프로그램을 작성하시오.

#include <iostream>
#include <map>
#include <vector>

using namespace std;

map<string, bool> db;

int main() {
    // scenario 1. get names not ever heared
    int N, M; cin >> N >> M;
    for(int i=0; i<N; i++) {
        string name; cin >> name;
        db.insert(make_pair(name, false));
    }
    for(int i=0; i<M; i++) {
        string name; cin >> name;
        if(db.find(name)->second == false) {
            db.find(name)->second = true;
        } else {
            db.insert(make_pair(name, false));
        }
    }
    vector<string> names;

    for(map<string, bool>::iterator it=db.begin(); it != db.end(); it++) {
        if(it->second == true) names.push_back(it->first);
    }
    cout << names.size() << endl;
    for(int i=0; i<names.size(); i++) {
        cout << names[i] << endl;
    }
}