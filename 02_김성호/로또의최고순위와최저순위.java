package level1;

public class 로또의최고순위와최저순위 {
	public static void main(String[] args) {
		
	 public static int[] solution(int[] lottos, int[] win_nums) {
	        int[] answer = {};
	        
	        int zeroCnt = 0;
	        int corrCnt = 0;
	        
	        
	        for(int i = 0; i < win_nums.length; i++){
	            if(lottos[i] == 0){
	                zeroCnt++;
	                continue;
	            } 
	            
	            for(int j = 0; j < win_nums.length; j++){
	                if(lottos[i] == win_nums[j]){
	                    corrCnt++;
	                }
	            }

	        }
	        
	
	        if(zeroCnt == 0){
	            if(corrCnt > 1){
	                answer = new int[]{6 - corrCnt + 1, 6 - corrCnt + 1};    
	            }
	            else{
	                answer = new int[]{6, 6};
	            }
	            
	           
	        }
	        else{
	            if(corrCnt > 1){            
	                
	                answer = new int[]{6 - (corrCnt + zeroCnt) + 1, 6 - corrCnt + 1};
	            }
	            else{

	                answer = new int[]{6 - (corrCnt + zeroCnt) +1, 6};  
	               
	            }
	        }
	        
	        return answer;
	    }
}
