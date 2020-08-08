// 20.08.08 18:13
// result 계산할때 한번에 곱하기까지 하니까 이상한답 나왔었음

#include <iostream>
#include <map>

using namespace std;

// STL map ref :  https://twpower.github.io/91-how-to-use-map-in-cpp

map<string, pair<int, int> > resistance;

int main() {
    resistance.insert(make_pair("black", make_pair(0, 1)));
    resistance.insert(make_pair("brown", make_pair(1, 10)));
    resistance.insert(make_pair("red", make_pair(2, 100)));
    resistance.insert(make_pair("orange", make_pair(3, 1000)));
    resistance.insert(make_pair("yellow", make_pair(4, 10000)));
    resistance.insert(make_pair("green", make_pair(5, 100000)));
    resistance.insert(make_pair("blue", make_pair(6, 1000000)));
    resistance.insert(make_pair("violet", make_pair(7, 10000000)));
    resistance.insert(make_pair("grey", make_pair(8, 100000000)));
    resistance.insert(make_pair("white", make_pair(9, 1000000000)));

    string a, b, c;
    cin >> a >> b >> c;

    long long result = (resistance.find(a)->second.first*10 + resistance.find(b)->second.first);
    result *= resistance.find(c)->second.second;
    cout << result;

    // cout << resistance.find("black")->second.second;
}