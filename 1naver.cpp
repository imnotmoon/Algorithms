//
//  1naver.cpp
//  
//
//  Created by 문상혁 on 07/01/2020.
//

#include <stdio.h>
#include <iostream>

using namespace std;

int main() {
    int size; cin >> size;
    int A[100000];
    int on[100000] = {0};
    int lastBulbTurnedOn = 0;
    int timesWhenEveryBulbTurnedOn = 0;
    
    for(int i=0; i<size; i++) { cin >> A[i]; }
    
    cout << endl;
    
    for(int i=0; i<size; i++) {
        on[A[i]-1] = 1;    // 전구 켬
        for(int k=0; k<size; k++) {
            cout << on[k] << " ";
        }
        cout << endl;
        // 켜진 전구 갯수 카운트
        for(int j=lastBulbTurnedOn; j<size; j++) {
            if(on[j] == 1) lastBulbTurnedOn++;
            else break;
        }
        //cout << "moment : " << i << "   bulbs on : " << lastBulbTurnedOn << endl;
        if(lastBulbTurnedOn == i+1) timesWhenEveryBulbTurnedOn++;
        lastBulbTurnedOn = 0;
    }
    
    cout << timesWhenEveryBulbTurnedOn << endl;
}
