//
//

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int N;
vector<int> numbers;

int main() {
    cin >> N;
    for(int i=0; i<N; i++) {
        int t; cin >> t; numbers.push_back(t);
    }
    sort(numbers.begin(), numbers.end());
    long long total = 0;
    int i = numbers.size()-1; int j = i-1;

    // for(int i=0; i<numbers.size(); i++) {
    //     cout << numbers[i] << " ";
    // }
    // cout << endl;

    while(j>0 && numbers[j] > 0) {
        if(numbers[j] == 1) break;
        total = total + numbers[i]*numbers[j];
        i-=2; j-=2;
        
    }
    int k = 0; int l = 1;
    while(l<i && numbers[l] <= 0) {
        total = total + numbers[k]*numbers[l];
        k+=2; l+=2;
    }
    // cout << "total : " << total << endl;
    // cout << "current : " << k << " // " << i << endl;

    for(int a=k; a<=i; a++) {
        total += numbers[a];
    }
    cout << total << endl;
}