#include <iostream>
#include <stdio.h>

using namespace std;

int number = 10;
int data[10] = {1, 20, 5, 8, 7, 6, 4, 3, 2, 9};

void quickSort(int *data, int start, int end) {
    if(start >= end) {
        // 원소가 1개인 경우
        return;
    }
    int pivot = start;  // pivot : 첫번째 원소
    int i = start + 1;      // ->
    int j = end;            // <-
    int temp;               // for swap

    while(i <= j) {     // 엇갈릴 때까지 반복
        while(data[i] <= data[pivot]) i++;
        while(data[j] >= data[pivot] && j > start) j--;   // j 바운더리만 설정해줘도 됨
        if(i>j) {
            // 엇갈린 경우 : 왼쪽값(엇갈려서 j가 현재 왼쪽임)와 pivot을 교체
            temp = data[j]; data[j] = data[pivot]; data[pivot] = temp;
        } else {
            // 엇갈리지 않은 경우 : 둘이 교체
            temp = data[j]; data[j] = data[i]; data[i] = temp;
        }
    }
    quickSort(data, start, j-1);
    quickSort(data, j+1, end);
}

int main() {
    ios::sync_with_stdio(0);
    quickSort(data, 0, number-1);
    for(int i=0; i<number; i++) {
        printf("%d ", data[i]);
    }
}