//
//  atm.cpp
//  
//
//  Created by 문상혁 on 18/08/2019.
//

#include <stdio.h>
#include <iostream>
#include <vector>

using namespace std;

vector<int> v;

void vector_sort(vector<int> v) {
    int temp = v[0];
    for(int i=0; i<v.size(); i++) {
        for(int j=i; j<v.size(); j++) {
            if(v[i] > v[j]) {
                temp = v[i]; v[i] = v[j]; v[j] = temp;
            }
        }
    }
    int sum = 0;
    for(int i=0; i<v.size(); i++) {
        sum += v[i]*(v.size()-i);
    }
    cout << sum << endl;
}


int main() {
    int N; cin >> N;
    int sum = 0;
    for(int i=0; i<N; i++) {
        int t; cin >> t;
        v.push_back(t);
    }
    vector_sort(v);
}
