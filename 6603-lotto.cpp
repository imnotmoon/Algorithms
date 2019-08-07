//
//  lotto.cpp
//  
//
//  Created by 문상혁 on 07/08/2019.
//

#include <stdio.h>
#include <iostream>
#include <vector>
#include <string>

using namespace std;

// graph making fuction


void visit(vector<int> arr, int index, int cnt, string result, int size);

void visit(vector<int> arr, int index, int cnt, string result, int size) {
    //cout << "index : " << index << " " << "cnt : " << cnt << endl;
    if(index > size-1) {
        return;
    }
    string sol = result;
    if(cnt == 6) {
        sol = sol.append(to_string(arr[index]));
        sol = sol.append(" ");
        cout << sol << endl;
        return;
    }
    if(arr[index] != 0) {
        sol = sol.append(to_string(arr[index]));
        sol = sol.append(" ");
    }
    //이거 다시보자
    visit(arr, index+1, cnt+1, sol, size);
    //이거
    visit(arr, index+1, cnt, result, size);
}

int main() {
    int K; int a; int iter_series = 0; string s = "";
    cin >> K;
    vector<vector<int> > series;
    int temp[13] = {0};
    while(!(K==0)) {
        vector<int> S; S.push_back(0);
        for(int i=0; i<K; i++) {
            cin >> a;
            S.push_back(a);
            if(i+1==K) {K = 0; series.push_back(S); iter_series++;}
        }
        cin >> K;
        S.clear();
    }
    
    for(int i=0; i<iter_series; i++) {
        visit(series[i], 0, 0, s, series[i].size());
        cout << endl;
    }
    
}


// 8 다음 34로 안감 왜안가냐
