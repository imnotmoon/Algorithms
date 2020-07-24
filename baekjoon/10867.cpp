// 20.07.25. 02:22 정답

#include <stdio.h>
#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int arr[100000] = {0};
int n;

void quickSort(int start, int end) {
    if(start>=end) return;
    int i = start+1; int j = end; int pivot = start;
    while(i<=j) {
        while(arr[i] <= arr[pivot]) i++;
        while(arr[j] >= arr[pivot] && j>start) j--;
        if(i>j) swap(arr[j], arr[pivot]);
        else swap(arr[i], arr[j]);
    }
    quickSort(start, j-1);
    quickSort(j+1, end);
}

void printArray() {
    int current = arr[0];
    for(int i=0; i<n; i++) {
        if(i != 0) {
            if(current != arr[i]) {
                printf("%d ", arr[i]);
                current = arr[i];
            }
        } else printf("%d ", arr[0]);
    }
}

int main() {
    scanf("%d", &n);
    int t;
    for(int i=0; i<n; i++) {
        cin >> arr[i];
    }
    quickSort(0, n-1);
    printArray();
}