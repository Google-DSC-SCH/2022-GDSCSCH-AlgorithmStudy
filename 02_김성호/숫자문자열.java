   static class Solution {
        public int solution(String s) {
            int answer = 0;
            HashMap<String, String> map = new HashMap<>();
            map.put("zero", "0");
            map.put("one", "1");
            map.put("two", "2");
            map.put("three", "3");
            map.put("four", "4");
            map.put("five", "5");
            map.put("six", "6");
            map.put("seven", "7");
            map.put("eight", "8");
            map.put("nine", "9");

            StringBuilder sb1 = new StringBuilder();

            for(int i = 0; i < s.length(); i++){

                if(s.charAt(i) < 'a'){
                    sb1.append(s.charAt(i));
                }
                else{ 
                    for (int j = 2; j <= s.length()-i; j++) {
                        if(map.containsKey(s.substring(i, i+j))){
                            sb1.append(map.get(s.substring(i, i + j)));
                            i = (i + j - 1);
                        }
                    }

                }
            }

            answer = Integer.parseInt(sb1.toString());

            return answer;
        }
    }
