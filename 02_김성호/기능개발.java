import java.util.*;

class Solution {
	static public int[] solution(int[] progresses, int[] speeds) {
	        Queue<Integer> queue = new LinkedList<Integer>();
	        ArrayList<Integer> list = new ArrayList<Integer>();
	        
	        for(int i = 0; i < speeds.length; i++){
	            int rest = 100 - progresses[i];
	
	            
	            if(rest % speeds[i] == 0) {
	            	queue.offer(rest / speeds[i]);
	            }
	            else {
	            	queue.offer((rest / speeds[i]) + 1);
	            }
	            
	        }
	        
	        while(!queue.isEmpty()){
	            int cnt = 0;
	        
	            int curr = queue.poll();
	            cnt++;
	            
	            while(!queue.isEmpty()){
	                if(queue.peek() <= curr){
	                    queue.poll();
                        cnt++;
	                    
	                }
	                else{
	                    break;
	                }
	            }
	            
	            list.add(cnt);
	        }
	       
	         
	        
	        int[] answer = list.stream().mapToInt(Integer::intValue).toArray();
	        return answer;
	    }
}
