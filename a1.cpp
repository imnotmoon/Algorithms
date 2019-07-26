//
//  c.cpp
//  
//
//  Created by 문상혁 on 08/06/2019.
//

#include <stdio.h>
#include <iostream>

using namespace std;

int isCorrect(int arr[], int size) {
    for(int i=0; i<size; i++) {
        if(arr[i] == 0) {
            return 0;
        }
    }
    return 1;
}

int main() {
    int s1, s2;
    while(true) {
        cin >> s1 >> s2;
        if(s1+s2 > 0 && s1+s2 < 101) {
            int a, b;
            int ans1[s1], ans2[s2];
            int iter = 0;
            while(iter < s1) {
                cin >> a >> b;
                if(a == b) {
                    ans1[iter] = 1;
                } else {
                    ans1[iter] = 0;
                }
                iter++;
            }
            iter = 0;
            while(iter < s2) {
                cin >> a >> b;
                if(a == b) {
                    ans2[iter] = 1;
                } else {
                    ans2[iter] = 0;
                }
                iter++;
            }
            if(isCorrect(ans1, s1) == 1 && isCorrect(ans2, s2) == 1) {
                cout << "Accepted!" << endl;
            } else if(isCorrect(ans1, s1) == 1 && isCorrect(ans2, s2) == 0) {
                cout << "Why Wrong!!" << endl;
            } else {
                cout << "Wrong Answer!" << endl;
            }
        } else {
            continue;
        }
    }
}
