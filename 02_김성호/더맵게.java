import java.util.*;

class Solution {
    public int solution(int[] scoville, int K) {
		PriorityQueue<Integer> queue = new PriorityQueue<Integer>();
        int answer = 0;
        
		for(int item : scoville) {
			queue.offer(item);
		}
		
		while(!queue.isEmpty()) {
			int newFood = 0;
			
			if(queue.peek() >= K) break;
			
			if(queue.size() == 1 && queue.peek() < K) {
				answer = -1;
				break;
			}
			
			
			
			if(queue.peek() < K) {
				newFood = queue.poll() + (queue.poll() * 2);
				queue.offer(newFood);
				answer++;
			}
			
			
		}
        
        
        return answer;
    }
}
