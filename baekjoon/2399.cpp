#include <iostream>

using namespace std;

long long v[10000] = {0};
int n = 0;

// Bubble Sort
void sort_list() {
    for(int i=0; i<n; i++) {
        for(int j=0; j<n-i-1; j++) {
            if(v[j] > v[j+1]) { int t = v[j]; v[j] = v[j+1]; v[j+1] = t; }
        }
    }
}

int main() {
    cin >> n;
    for(int i=0; i<n; i++) { cin >> v[i]; }

    sort_list();

    // count dist
    long long total = 0;
    for(int i=0; i<n; i++) { 
        for(int j=i+1; j<n; j++) {
            total += v[j]-v[i];
        }
    }
    cout << total*2;
}