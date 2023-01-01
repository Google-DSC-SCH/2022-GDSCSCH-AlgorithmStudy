#include <iostream>
#include <string>
#include <set>
#include <vector>
#include <map>
using namespace std;

map<string, int> usrCnt;			 // 유저별 신고 당한 횟수를 담는 배열
map<string, set<string>> usrReport;	 // 유저별 신고한 다른 유저들의 목록을 담는 배열


vector<int> solution(vector<string> id_list, vector<string> report, int k) {
	vector<int> answer;

	// 신고 내역 받기
	for (string s : report) {
		int blank = s.find(' ');
		string first = s.substr(0, blank);
		string second = s.substr(blank);

		if (usrReport[first].find(second) == usrReport[first].end()) {
			usrReport[first].insert(second);
			usrCnt[second]++;
		}
	}

	// 신고 내역 정산하기 _ ( k번 이상 신고 누적 시 신고자에 메일 발송 )
	for (string usr_id : id_list) {
		int count = 0;  // 받게 될 메일의 수
		for (string s : usrReport[usr_id]) {	//usr_id가 신고한 이력을 순회하며,
			if (usrCnt[s] >= k)	// 해당(신고 당한) 유저의 신고 누적 횟수가 k번 이상이라면 발송해야한다.
				count++;
		}
		answer.push_back(count);
	}

	return answer;
}

// 확인해보기
int main() {
	vector<string> ex1;
	ex1.push_back("muzi");
	ex1.push_back("frodo");
	ex1.push_back("apeach");
	ex1.push_back("neo");

	vector<string> ex1_report;
	ex1_report.push_back("muzi frodo");
	ex1_report.push_back("apeach frodo");
	ex1_report.push_back("frodo neo");
	ex1_report.push_back("muzi neo");
	ex1_report.push_back("apeach muzi");

	vector<int> answer;
	answer = solution(ex1, ex1_report, 2);

	cout << '[' << ' ';
	for (int i = 0; i < answer.size(); i++) {
		cout << answer[i] << ' ';
	}
	cout << ']';
}