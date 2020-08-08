// 20.08.08 18:51
//

#include <iostream>
#include <map>

using namespace std;

map<string, int> bestSeller;

int main() {
    int N; cin >> N;
    for(int i=0; i<N; i++) {
        string name; cin >> name;
        if(bestSeller.find(name) == bestSeller.end()) {
            // not found
            bestSeller.insert(make_pair(name, 1));
        } else {
            bestSeller.find(name)->second++;
        }
    }
    map<string, int>::iterator max = bestSeller.begin();
    for(map<string, int>::iterator it=bestSeller.begin(); it != bestSeller.end(); it++) {
        // cout << it->first << " : " << it->second << endl;
        if(it->second > max->second) {
            max = it;
        }
    }
    cout << max->first << endl;
}