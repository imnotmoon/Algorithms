#include <iostream>
#include <algorithm>
#include <vector>   // #2

using namespace std;

bool compare2(pair<string, pair<int, int> > a, pair<string, pair<int, int> > b) {
    if(a.second.first == b.second.first) {
        return a.second.second > b.second.second;
    } else {
        return a.second.first > b.second.first;
    }
}
int main() {
    // 클래스 사용하는 방식에서 벡터와 페어를 사용하는 방식으로 변경
    vector<pair<int, string> > v;
    v.push_back(pair<int, string>(0, "우소연"));
    v.push_back(pair<int, string>(54523, "조유빈"));
    v.push_back(pair<int, string>(14234, "킹짱빈"));
    v.push_back(pair<int, string>(78943, "행신사는조유빈"));
    v.push_back(pair<int, string>(10985, "행신사는항공대학교15학번조유빈(경영에서소학으로전과함)"));

    // sort(v.begin(), v.end());

    // for(int i=0; i<v.size(); i++) {
    //     cout << v.at(i).first << ' ' << v.at(i).second << endl;
    // }

    // 이중페어를 사용해서 이름, 성적, 생년월일을 2개의 값으로 정렬
    // 3개 이상이면 너무 복잡해지니 차라리 클래스를 쓰는게 나을수도 있다더라
    vector<pair<string, pair<int, int> > > vv;
    vv.push_back(pair<string, pair<int, int> >("나동빈", pair<int, int>(90, 19961222)));
    vv.push_back(pair<string, pair<int, int> >("우소연", pair<int, int>(50, 19970728)));
    vv.push_back(pair<string, pair<int, int> >("킹짱빈", pair<int, int>(1090, 00001225)));
    vv.push_back(pair<string, pair<int, int> >("조빈빈", pair<int, int>(1090, 10001225)));
    vv.push_back(pair<string, pair<int, int> >("문빈빈", pair<int, int>(212, 19970501)));

    // 성적이 같은데 생일이 느리면 더 늦은 우선순위
    sort(vv.begin(), vv.end(), compare2);

    for(int i=0; i<5; i++) {
        cout << vv[i].first << " " << vv[i].second.first << " " << vv[i].second.second << endl;
    }
}




////////////////// 이하 9강 ///////////////////


void printList(int *a) {
    for(int i=0; i<10; i++) {
        cout << a[i] << " " ;
    }
}

bool compare(int a, int b) {
    // return a < b;   // a가 b보다 작을떼 우선적으로 정렬한다 -> 오름차순
    return a > b;       // 내림차순
}

class Student {
public:
    string name;
    int score;
    Student(string name, int score) {
        this->name = name;
        this->score = score;
    }
    // 정렬 기준 정의 : 점수가 작은 순서
    bool operator <(const Student &student)const {
        return this->score < student.score;  // 오름차순으로 정렬한다
    }

};

void main_2() {
    int a[10] = {9, 3, 5, 4, 2, 20, 8, 6, 8, 7};
    sort(a, a+10); // 인자는 메모리 주소
    //printList(a);

    sort(a, a+10, compare);
    // printList(a);

    // 데이터를 묶어서 정렬하는 방법 -> '특정한 변수를 기준으로 정렬'하는 방법
    // Student 객체를 시험점수 순서로 정렬

    Student students[] = {
        Student("나동빈", 90),
        Student("조유빈", 150),
        Student("우소연", 5),
        Student("킹짱빈", 200),
        Student("문상혁", 80)
    };
    sort(students, students+5);

    for(int i=0; i<5; i++) {
        cout << students[i].name << ' ';
    }
}