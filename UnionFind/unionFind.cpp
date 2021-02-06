#include <stdio.h>

// 부모노드를 찾는 함수
int getParent(int parent[], int x) {
    // 재귀함수의 종료조건
    if(parent[x] == x) return x;

    return parent[x] = getParent(parent, parent[x]);
}

// 두 부모노드를 합치는 함수
void unionParent(int parent[], int a, int b) {
    a = getParent(parent, a);
    b = getParent(parent, b);
    
    // 두 부모를 확인하고 작은쪽으로 합침
    if(a < b) parent[b] = a;
    else parent[a] = b;
}

// 같은 부모를 가지는지 확인
// 같은 그래프에 속하는지 확인하는 것과 같다.
int findParent(int parent[], int a, int b) {
    a = getParent(parent, a);
    b = getParent(parent, b);
    if(a==b) return 1;
    return 0;
}

int main() {
    int parent[11];
    for(int i=1; i<10; i++) {
        parent[i] = i;
    }
    unionParent(parent, 1, 2);
    unionParent(parent, 2, 3);
    unionParent(parent, 3, 4);
    unionParent(parent, 5, 6);
    unionParent(parent, 6, 7);
    unionParent(parent, 7, 8);

    printf("1과 5가 같은 그래프에 속해있나요? %d\n", findParent(parent, 1, 5));

    unionParent(parent, 1, 5);
    printf("1과 5가 같은 그래프에 속해있나요? %d\n", findParent(parent, 1, 5));
    // 1에 속하는 다른 원소 + 5가 속하는 집합의 다른 원소를 연결 처리가 된다.
}