// 무지의 먹방 라이브

#include <iostream>
#include <string>
#include <algorithm>
#include <vector>

using namespace std;

int solution(vector<int> food_times, long long k) {
    int answer = 0;
    long long menu = food_times.size();        
    // [946, 314, 757, 322, 559, 647, 983, 482, 145]	1833	1
    // 901 169 612, 175 414 502 838 337 // 528
    while(k>0) {
        long long size = food_times.size();
        int min = *min_element(food_times.begin(), food_times.end());
        // cout << "min : " << min << "   size : " << size << endl;
        if(min*size < k) {
            for(int i=0; i<size; i++) {
                food_times[i] -= min;
                // cout << food_times[i] << endl;
                if(food_times[i] == 0) food_times.erase(food_times.begin()+i);
            }
            
            k -= size*min;
            // cout << "k : " << k << endl;
        } else if(k < min*size) {
            // cout << "----------" << endl;
            // cout << "k : " << k << endl;
            answer = k%size+1; break;
        } else {
            answer = 1; return answer;
        }
    }
    
    return answer;
}

int main() {
    long long number, k;
    vector<int> v;
    cin >> number >> k;
    for(int i=0; i<number; i++) {
        int t; cin >> t; v.push_back(t);
    }
    cout << solution(v, k);
}