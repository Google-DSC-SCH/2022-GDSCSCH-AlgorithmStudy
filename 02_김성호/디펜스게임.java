    static class Solution {
        public int solution(int n, int k, int[] enemy) {
          
            PriorityQueue<Integer> queue = new PriorityQueue<>();
          
            for (int round = 0; round < enemy.length; round++) {
              
                queue.add(enemy[round]);
              
                if (queue.size() > k){
                    n -= queue.poll();
                }
              
                if (n < 0){
                    return round;
                }
            }
            return enemy.length;
        }
    }
