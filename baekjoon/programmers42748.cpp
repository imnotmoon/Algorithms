// 20.08.02 00:07 정답

#include <string>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> array, vector<vector<int>> commands) {
    vector<int> answer;
    for(int i=0; i<commands.size(); i++) {
        int start = commands[i][0];
        int end = commands[i][1];
        int idx = commands[i][2];
        
        vector<int> newArray;
        for(int j=start-1; j<end; j++) {
            newArray.push_back(array[j]);
        }
        // for(int j=0; j<newArray.size(); j++) {
        //     cout << newArray[j] << " " ;
        // }
        sort(newArray.begin(), newArray.end());
        // cout << "ans : " << newArray[idx-1] << endl;
        answer.push_back(newArray[idx-1]);
    }
    return answer;
}
