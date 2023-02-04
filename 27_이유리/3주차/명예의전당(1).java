import java.util.PriorityQueue;

class Solution {
    public int[] solution(int k, int[] score) {
    	int[] answer = new int[score.length];
        PriorityQueue<Integer> pqueue = new PriorityQueue();	// 우선순위 큐를 이용하여 가장 작은 값을 쉽게 꺼내도록 한다.
        int score_num = k;
        
        // k보다 score의 길이가 작은 경우 고려
        if(k > score.length)
        	score_num = score.length;
        
        // k번까지는 명예의 전당에서 내려가는 순위가 없으므로 매 일차 가장 낮은 점수를 모두 answer에 추가한다.
        for(int i = 0; i < score_num; i++) {
        	pqueue.add(score[i]);
        	answer[i] = pqueue.peek();
        }
        
        // k < score.length 인 경우 poll로 일차별 가장 낮은 점수를 명예의 전당에서 내리고 그 다음 낮은 점수를 answer에 추가한다.
        for(int i = score_num; i < score.length; i++) {
        	pqueue.add(score[i]);
        	pqueue.poll();
        	answer[i] = pqueue.peek();
        }
        	
        return answer;
    }
}
