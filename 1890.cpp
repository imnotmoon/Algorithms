//
//  1890.cpp
//  
//
//  Created by 문상혁 on 14/08/2019.
//

#include <stdio.h>
#include <iostream>

using namespace std;
int N;
int arr[100][100]; int visited[100][100];

void searchEnd(int x, int y) {
    for(int i=0; i<N; i++) {
        for(int j=0; j<N; j++) {
            if(i == N-1 && j == N-1) return;
            if(visited[i][j] != 0) {
                for(int a = 0; a<N; a++) {
                    for(int b = 0; b<N; b++) {
                        cout << visited[a][b] << " ";
                    }
                    cout << endl;
                }
                cout << endl;
                if(i+arr[i][j] < N) {
                    visited[i+arr[i][j]][j] += visited[i][j];
                }
                if(y+arr[i][j] < N) {
                    visited[i][j+arr[i][j]] += visited[i][j];
                }
            }
        }
    }
}

int main() {
    cin >> N;
    for(int i=0; i<N; i++) {
        for(int j=0; j<N; j++) {
            cin >> arr[i][j];
            visited[i][j] = 0;
        }
    }   // initialize
    visited[0][0] = 1;
    searchEnd(0,0);
    cout << visited[N-1][N-1] << endl;
}
