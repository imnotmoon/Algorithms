//
//  lotto.cpp
//  
//
//  Created by 문상혁 on 08/08/2019.
//

#include <stdio.h>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

vector<vector<int> > S;

void visit(vector<int> arr, int index, string s, int cnt) {
    if(cnt == 6) { cout << s << endl; return; }
    string result = s;
    result = result.append(to_string(arr[index])); result.append(" ");
    //cout << result << " // cnt : " << cnt << endl;
    if(index < arr.size()) {
        visit(arr, index+1, result, cnt+1);
        //cout << " ------------------ " << endl;
        visit(arr, index+1, s, cnt);
    }
}
void visit(int i) {
    visit(S[i],0,"",0);
}

int main() {
    int k; cin >> k;
    int input;
    // input vector
    while(!(k==0)) {
        vector<int> temp;
        for(int i=0; i<k; i++) {
            cin >> input; temp.push_back(input);
        }
        S.push_back(vector<int>(temp));
        temp.clear(); cin >> k;
    }
    
    for(int i=0; i<S.size(); i++) {
        visit(i); cout << endl;
    }
}
