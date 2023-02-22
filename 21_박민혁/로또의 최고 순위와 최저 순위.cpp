#include <iostream>
#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> lottos, vector<int> win_nums) {
    vector<int> answer;
    int win_count = 0;
    int zero_count = count(lottos.begin(), lottos.end(), 0);

    for (size_t i = 0; i < lottos.size(); i++) {
        for (size_t j = 0; j < win_nums.size(); j++) {
            if (lottos[i] == win_nums[j]) win_count++;
        }
    }

    win_count += zero_count;
    for (size_t i = 0; i < 2; i++)
    {
        if (win_count == 6) answer.push_back(1);
        else if (win_count == 5) answer.push_back(2);
        else if (win_count == 4) answer.push_back(3);
        else if (win_count == 3) answer.push_back(4);
        else if (win_count == 2) answer.push_back(5);
        else answer.push_back(6);

        win_count -= zero_count;
    }

    return answer;
}

int main() {
    vector<int> test_lottos, test_win_nums;
    test_lottos.push_back(44);
    test_lottos.push_back(1);
    test_lottos.push_back(0);
    test_lottos.push_back(0);
    test_lottos.push_back(31);
    test_lottos.push_back(25);

    test_win_nums.push_back(31);
    test_win_nums.push_back(10);
    test_win_nums.push_back(45);
    test_win_nums.push_back(1);
    test_win_nums.push_back(6);
    test_win_nums.push_back(19);

    //test_lottos.push_back(0);
    //test_lottos.push_back(0);
    //test_lottos.push_back(0);
    //test_lottos.push_back(0);
    //test_lottos.push_back(0);
    //test_lottos.push_back(0);

    //test_win_nums.push_back(38);
    //test_win_nums.push_back(19);
    //test_win_nums.push_back(20);
    //test_win_nums.push_back(40);
    //test_win_nums.push_back(15);
    //test_win_nums.push_back(25);

    //test_lottos.push_back(45);
    //test_lottos.push_back(4);
    //test_lottos.push_back(35);
    //test_lottos.push_back(20);
    //test_lottos.push_back(3);
    //test_lottos.push_back(9);

    //test_win_nums.push_back(20);
    //test_win_nums.push_back(9);
    //test_win_nums.push_back(3);
    //test_win_nums.push_back(45);
    //test_win_nums.push_back(4);
    //test_win_nums.push_back(35);

    vector<int> answer = solution(test_lottos, test_win_nums);
    for (size_t i = 0; i < answer.size(); i++) {
        cout << answer[i] << endl;
    }

    return 0;
}
