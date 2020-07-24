#include <iostream>
#include <stdio.h>
#include <vector>
#include <algorithm>

using namespace std;

int v[1000000];
int n;

void printVector() {
    for(int it=0; it<n; it++) {
        printf("%d\n", v[it]);
    }
}

void quickSort(int start, int end) {
    if(start >= end) return;
    int i=start+1; int j=end; int pivot = start;
    while(i <= j) {
        while(v[i] <= v[pivot] && i < n) i++;
        while(v[j] >= v[pivot] && j>start) j--;
        if(j<i) {       // 엇갈린 경우
            swap(v[j], v[pivot]);
        } else {
            swap(v[i], v[j]);
        }
    }
    quickSort(start, j-1);
    quickSort(j+1, end);
}


int main() {
    scanf("%d", &n);
    for(int i=0; i<n; i++) { scanf("%d", &v[i]);}

    quickSort(0, n-1);
    printVector();
}