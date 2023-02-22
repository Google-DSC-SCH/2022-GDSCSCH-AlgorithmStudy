#include <iostream>
#include <string>
#include <vector>

using namespace std;

int solution(vector<int> ingredient) {
    int answer = 0;

    for (int i = 0; i < ingredient.size() - 3; i++) {
        if (ingredient[i] == 1) {
            if (ingredient[i + 1] == 2) {
                if (ingredient[i + 2] == 3) {
                    if (ingredient[i + 3] == 1) {
                        ingredient.erase(ingredient.begin() + i);
                        ingredient.erase(ingredient.begin() + i);
                        ingredient.erase(ingredient.begin() + i);
                        ingredient.erase(ingredient.begin() + i);

                        i = 0;
                        answer++;
                        //for (int j = 0; j < ingredient.size(); j++) {
                        //    cout << ingredient[j];
                        //}
                        //cout << endl;
                    }
                }
            }
        }
    }
    return answer;
}

int main() {
    vector<int> ingredient; //[2, 1, 1, 2, 3, 1, 2, 3, 1], [1, 3, 2, 1, 2, 1, 3, 1, 2]
    ingredient.push_back(1);
    ingredient.push_back(3);
    ingredient.push_back(2);
    ingredient.push_back(1);
    ingredient.push_back(2);
    ingredient.push_back(1);
    ingredient.push_back(3);
    ingredient.push_back(1);
    ingredient.push_back(2);
    int burger = solution(ingredient);
    cout << burger << endl;

    ingredient.push_back(2);
    ingredient.push_back(1);
    ingredient.push_back(1);
    ingredient.push_back(2);
    ingredient.push_back(3);
    ingredient.push_back(1);
    ingredient.push_back(2);
    ingredient.push_back(3);
    ingredient.push_back(1);
    burger = solution(ingredient);
    cout << burger << endl;

    return 0;
}
