    class Solution {
        public int solution(int number, int limit, int power) {
            int answer = 0;

            for (int i = 1; i <= number; i++) {
                int num = 0;

                for (int j = 1; j <= Math.sqrt(i); j++) {
                    if(j * j == i){
                        num++;
                    }              
                    else if(i % j == 0){
                        num+= 2;
                    }
                }

                if(num > limit){
                    num = power;
                }
                //System.out.println(i + "번째 : " +num);
                answer += num;
            }
            return answer;
        }
    }
