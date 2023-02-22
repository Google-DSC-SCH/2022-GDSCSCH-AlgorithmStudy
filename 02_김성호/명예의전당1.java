import java.util.*;

class Solution {
		public int[] solution(int k, int[] score) {
			int[] answer = new int[score.length];
			PriorityQueue<Integer> pq = new PriorityQueue<Integer>((a, b) -> a - b > 0 ? 1 : -1); // 내림차순

			
			for(int i = 0; i < score.length; i++) {
				
				if(pq.size() < k) {
					pq.offer(score[i]);
					answer[i] = pq.peek();
				}
				else if(pq.size() == k) {
					if(score[i] > pq.peek()){
						pq.poll();
						pq.offer(score[i]);
					}
					answer[i] = pq.peek();
				}
				
			}
			
			return answer;
		}
}
