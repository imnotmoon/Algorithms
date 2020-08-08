// 20.08.08 18:44
// long long...

#include <iostream>
#include <map>

using namespace std;

map<long long, long long> hand;

int main() {
    int N;
    cin >> N;
    for(int i=0; i<N; i++) {
        long long card; cin >> card;
        if(hand.find(card) == hand.end()) {
            hand.insert(make_pair(card, 1));
        } else {
            hand.find(card)->second++;
        }
    }

    map<long long, long long>::iterator max = hand.begin();
    for(map<long long, long long>::iterator it=hand.begin(); it != hand.end(); it++) {
        // cout << it->first << "(" << it->second << ")" << "  :  " << max->first << "(" << max->second << ")" <<  endl;
        if(it->second > max->second) {
            max = it;
        }
    }

    cout << max->first;
}