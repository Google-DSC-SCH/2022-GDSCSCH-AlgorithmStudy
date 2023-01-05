#include <string>
#include <vector>

using namespace std;

int solution(vector<int> ingredient) { 
    int answer = 0;
    int i = 0;
 
   while(1){

        if (i == ingredient.size() - 3 || ingredient.size() < 4) break;

       else if (ingredient[i] == 1 && ingredient[i + 1] == 2 && ingredient[i + 2] == 3 && ingredient[i + 3] == 1) {

           for (int k = 0; k < 4; k++) {
               ingredient.erase(ingredient.begin() + i);
           }
           answer++;
           i = 0;
       }
     
       else i++;
   }

    return answer;
}
