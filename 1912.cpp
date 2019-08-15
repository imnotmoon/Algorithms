//
//  1912.cpp
//  
//
//  Created by 문상혁 on 10/08/2019.
//

#include <stdio.h>
#include <iostream>

using namespace std;

int main() {
    int n; cin >> n;
    int arr[n];
    int tmp; int sum = 0;
    for(int i=0; i<n; i++) {
        cin >> arr[i];
    }
    tmp = arr[0] + arr[1];
    for(int i=0; i<n-1; i++) {
        sum = arr[i];
        for(int j=i+1; j<n; j++) {
            cout << sum << " " << arr[j] << endl;
            sum+=arr[j];
            if(sum > tmp) tmp = sum;
        }
    }
    cout << tmp << endl;
}
