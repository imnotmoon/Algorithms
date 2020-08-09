// 20.08.09 17:04
// 숫자를 전부 써야하는건데 부분만 써도 되는줄
// 런타임에러 -> 메인함수가 0을 리턴하지 않거나 /0의 경우를 의심

#include <iostream>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;

vector<int> numbers;

int main() {
    string N; cin >> N;
    int zeros = 0;
    for(int i=0; i<N.size(); i++) {
        if(N[i] == '0') zeros++;
    }
    if(zeros == 0) { cout << -1; return 0; }

    // 숫자 하나씩 분할
    for(int i=0; i<N.size(); i++) {
        numbers.push_back(int(N[i]-'0'));
    }
    sort(numbers.begin(), numbers.end());

    int total = 0;
    for(int i=0; i<numbers.size(); i++) {
        total += numbers[i];
    }
    if(total == 0 || total%3 != 0) {
        cout << -1; return 0;
    }

    string result = "";
    for(int i=numbers.size()-1; i>=0; i--) {
        result += to_string(numbers[i]);
    }
    cout << result;
}