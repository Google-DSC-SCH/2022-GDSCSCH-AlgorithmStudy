#include <iostream>
#include <string>
#include <vector>

using namespace std;

int solution(string s) {
    int answer = 0;
    char first_char = s[0];
    int first_char_cnt = 1, another_char_cnt = 0;

    for (int i = 1; i < s.size(); i++) {
        if (first_char == s[i]) first_char_cnt++;
        else if (first_char != s[i])    another_char_cnt++;

        if (first_char_cnt == another_char_cnt){
            answer++;
            s.erase(0, i + 1);

            if (s.size() > 1)   first_char = s[0];
            else if(s.size() == 1){
                answer++;
                break;
            }
            else    break;

            first_char_cnt = 1;
            another_char_cnt = 0;
            i = 0;
        }
    }

    return answer;
}

int main() {
    string test_input = "banana";
    //string test_input = "abracadabra";
    //string test_input = "aaabbaccccabba";
    int value = solution(test_input);
    cout << value << endl;

    return 0;
}
