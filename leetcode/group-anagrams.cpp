#include <algorithm>

class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        // 리턴값 담을 벡터
        vector<vector<string> > ret;
        // 인자로 받은건 정렬할거고 org를 리턴할때 쓸거임
        vector<string> org = strs;
        
        // 각 스트링을 정렬 -> 같은문자 쓴건 다 똑같이 생기게됨
        for(int i=0; i<strs.size(); i++) {
            sort(strs[i].begin(), strs[i].end());
        }
        
        // 같은건 같은 숫자로 체크할거임
        int comp = 1;
        vector<int> same;
        
        // same벡터 초기화
        for(int i=0; i<strs.size(); i++) {
            same.push_back(0);
        }
        
        // 같은 단어는 같은 숫자로 표기하는 과정
        for(int i=0; i<strs.size(); i++) {
            if(same[i] != 0) continue;
            same[i] = comp;
            for(int j=i; j<strs.size(); j++) {
                if(same[j] != 0) continue;
                if(strs[i] == strs[j]) {
                    same[j] = comp;
                }
            }
            comp++;
        }
        
        // 같은 숫자로 묶인것끼리 결과벡터에 담는 과정
        for(int i=1; i<comp; i++) {
            vector<string> t;
            for(int j=0; j<strs.size(); j++) {
                if(same[j] == i) t.push_back(org[j]);
            }
            ret.push_back(t);
        }
        
        // 이꾸요
        return ret;
    }
};