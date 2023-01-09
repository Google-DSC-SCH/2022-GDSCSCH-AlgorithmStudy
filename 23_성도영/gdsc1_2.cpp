#include <iostream>
#include <string>
#include <vector>
#include <stack>
using namespace std;

int solution(vector<int> ingredient) {
	int answer = 0;

	string str = "";
	for (int i = 0; i < ingredient.size(); i++) {
		str += to_string(ingredient[i]);

		int length = str.length();

		if (ingredient[i] == 1 && length >= 4) {
			int len = length - 4;
			if (str.substr(len) == "1231") {
				answer++;
				str.erase(len, 4);
			}
		}
	}

	return answer;
}

int main() {
	vector<int> ingredient1;

	// [ 2, 1, 1, 2, 3, 1, 2, 3, 1 ] 의 형태
	ingredient1.push_back(2);
	ingredient1.push_back(1);
	ingredient1.push_back(1);
	ingredient1.push_back(2);
	ingredient1.push_back(3);
	ingredient1.push_back(1);
	ingredient1.push_back(2);
	ingredient1.push_back(3);
	ingredient1.push_back(1);


	vector<int> ingredient2;

	// [1, 3, 2, 1, 2, 1, 3, 1, 2 ] 의 형태
	ingredient2.push_back(1);
	ingredient2.push_back(3);
	ingredient2.push_back(2);
	ingredient2.push_back(1);
	ingredient2.push_back(2);
	ingredient2.push_back(1);
	ingredient2.push_back(3);
	ingredient2.push_back(1);
	ingredient2.push_back(2);


	int result = solution(ingredient2);
	cout << result << '\n';
}