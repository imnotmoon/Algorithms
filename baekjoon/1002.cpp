//
//  1002.cpp
//  
//
//  Created by 문상혁 on 19/01/2020.
//

#include <stdio.h>
#include <iostream>
#include <stdlib.h>
#include <vector>
#include <cmath>

using namespace std;

int countPointsWhereRyuCanBe(vector<int> turret) {
    double distance = sqrt(pow(double(turret[0]-turret[3]),2.0) + pow(double(turret[1]-turret[4]),2.0));
    double r1 = turret[2], r2 = turret[5];
    if(distance == 0) {
        if(r1 == r2) return -1;
        else return 0;
    } else {
        if(r1+r2 > distance) {
            if(max(r1,r2)-min(r1,r2) == distance) return 1;
            else if(max(r1,r2)-min(r1,r2) > distance) return 0;
            else return 2;
        }
        else if(r1+r2 == distance) return 1;
        else return 0;
    }
}

int main() {
    int n; cin >> n;
    vector<vector<int> > turretAndDistances;
    for(int i=0; i<n; i++) {
        vector<int> temp; int varForInput;
        for(int j=0; j<6; j++) {
            cin >> varForInput; temp.push_back(varForInput);
        }
        turretAndDistances.push_back(temp);
    }
    
    for(int i=0; i<n; i++) {
        cout << countPointsWhereRyuCanBe(turretAndDistances[i]) << endl;
    }
}
