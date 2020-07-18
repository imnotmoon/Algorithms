//
//  a.cpp
//  
//
//  Created by 문상혁 on 24/08/2019.
//

#include <stdio.h>
#include <iostream>
#include <vector>

using namespace std;

int main() {
    int N; cin >> N;
    vector<int> sub;
    float t = 0;
    int max = t;
    for(int i=0; i<N; i++) {
        cin >> t; sub.push_back(t);
        if(max < t) max = t;
    }
    float total = 0;
    for(int i=0; i<N; i++) {
        float t = ((float)sub[i]/(float)max)*100;
        total += t;
`       }
    double avg = total / N;
    printf("%lf\n", avg);
}
