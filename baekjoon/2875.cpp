// 20.08.09 20:29


#include <iostream>
#include <algorithm>

using namespace std;

int N, M, K;

int makeTeam() {
    while(K > 0) {
        int threshold = N-(M*2);
        // cout << "threshold : " << threshold << endl;
        if(threshold == 0) {
            N -= 1; K -= 1;
        } else if(threshold > 0) {
            N -= 1; K -= 1;
        } else {
            M -= 1; K -= 1;
        }
        // cout << N << " " << M << " " << K << endl;
    }
    if(N > M*2) return M;
    return N/2;
}

int main() {
    cin >> N >> M >> K;
    int ret = makeTeam();
    cout << ret;
}