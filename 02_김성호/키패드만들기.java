    static class Solution {
        public String solution(int[] numbers, String hand) {
            String answer = "";
            StringBuilder sb = new StringBuilder();

            HashMap<Integer, Integer[]> keypad = new HashMap<>();
            int k = 1;
            for(int i = 0; i < 3; i++){
                for(int j = 0; j < 3; j++){
                    keypad.put(k, new Integer[]{i, j});
                    k++;
                }
            }
            keypad.put(0, new Integer[]{3, 1});
            keypad.put(-1, new Integer[]{3, 0});
            keypad.put(-2, new Integer[]{3, 2});

            int currR = -1;
            int currL = -2;

            for (int num : numbers) {
                if(num == 1 || num == 4 || num == 7){ // left
                    currL = num;
                    sb.append("L");

                }
                else if (num == 3 || num == 6 || num == 9) { // right
                    currR = num;
                    sb.append("R");

                }
                else{
                    // middle
                    Integer[] next = keypad.get(num);

                    int left = Math.abs(next[0] - keypad.get(currL)[0]) + Math.abs(next[1]  - keypad.get(currL)[1]);
                    int right= Math.abs(next[0] - keypad.get(currR)[0]) + Math.abs(next[1]  - keypad.get(currR)[1]);

                    if(left > right){
                        currR = num;
                        sb.append("R");
                    }
                    else if(right > left){
                        currL = num;
                        sb.append("L");
                    }
                    else{
                        if(hand.equals("right")){
                            currR = num;
                            sb.append("R");

                        }
                        else{
                            currL = num;
                            sb.append("L");
                        }
                    }
                }
            }

            return sb.toString();
        }
    }
