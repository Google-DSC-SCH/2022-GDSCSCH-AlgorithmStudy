#include <iostream>
#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<string> id_list, vector<string> report, int k) {
	vector<int>		answer;
	vector<string>	reporter;
	vector<string>	selector;
	bool			flag = true;

	for (int i = 0; i < report.size(); i++) {
		int blank = report[i].find(' ');
		string first = report[i].substr(0, blank);
		string second = report[i].substr(blank + 1);

		if (flag == true) {
			reporter.push_back(first);
			selector.push_back(second);
			flag = false;
			continue;
		}

		for (int j = 0; j < reporter.size(); j++) {
			if (reporter[j] == first && selector[j] == second) {
				flag = true;
			}
		}

		if (flag == false) {
			reporter.push_back(first);
			selector.push_back(second);
		}
	}

	vector<int> cnt;
	for (int i = 0; i < id_list.size(); i++) {
		int count = 0;
		for (int j = 0; j < selector.size(); j++) {
			if (id_list[i] == selector[j]) {
				count++;
			}
		}

		cnt.push_back(count);
	}

	int arr[4] = { 0 };
	for (int i = 0; i < cnt.size(); i++) {
		if (cnt[i] >= k) {
			for (int j = 0; j < report.size(); j++) {
				if (id_list[i] == selector[j]) {
					for (int x = 0; x < id_list.size(); x++) {
						if (reporter[j] == id_list[x]) {
							arr[x]++;
						}
					}
				}
			}
		}
	}
	for (int i = 0; i < id_list.size(); i++)
		answer.push_back(arr[i]);

	return answer;
}

//int main() {
//	vector<string> ex1;
//	ex1.push_back("muzi");
//	ex1.push_back("frodo");
//	ex1.push_back("apeach");
//	ex1.push_back("neo");
//
//	vector<string> ex1_report;
//	ex1_report.push_back("muzi frodo");
//	ex1_report.push_back("apeach frodo");
//	ex1_report.push_back("frodo neo");
//	ex1_report.push_back("muzi neo");
//	ex1_report.push_back("apeach muzi");
//
//	vector<int> answer;
//	answer = solution(ex1, ex1_report, 2);
//	for (int i = 0; i < answer.size(); i++) {
//		cout << answer[i] << endl;
//	}
//    return 0;
//}
