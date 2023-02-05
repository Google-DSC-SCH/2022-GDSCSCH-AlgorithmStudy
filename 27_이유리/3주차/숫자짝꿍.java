class Solution {
	public String solution(String X, String Y) {
	    StringBuilder answer = new StringBuilder();
	
	    int[] X_num = new int[10];	// X의 임의의 자리 정수 개수를 표시할 배열
    	int[] Y_num = new int[10];	// Y의 임의의 자리 정수 개수를 표시할 배열
    	boolean check = false;		// 1-9까지의 수가 발견되었는지 표시할 부울대수
	
    	// X가 가지고 있는 정수의 개수를 배열에 표시한다.
	    for(int i = 0; i < X.length(); i++) {
	        X_num[X.charAt(i) - '0']++;
		}
		
	    // Y가 가지고 있는 정수의 개수를 배열에 표시한다.
		for(int i = 0; i < Y.length(); i++) {
		    Y_num[Y.charAt(i) - '0']++;
		}
		
		/* X와 Y가 1-9 각 숫자를 몇 개 가지고 있는지 확인한다. 
    	 * 둘 다 1개 이상 가지고 있다면 더 적은 수에 맞춰 answer에 추가한다.*/
		for(int i = 9; i > 0; i--) {
		    if(X_num[i] > 0 && Y_num[i] > 0) {
		        int small = (X_num[i] < Y_num[i]) ? X_num[i] : Y_num[i];
		        for(int j = 0; j < small; j++) {
		            answer.append(i);
		        }
		        check = true;	// answer가 ""이 아님을 표시한다.
		    }
		}
		
		if(check) {	// answer가 ""이 아니라면
		    if(X_num[0] > 0 && Y_num[0] > 0) {
		        int small = (X_num[0] < Y_num[0]) ? X_num[0] : Y_num[0];
		        for(int j = 0; j < small; j++) {
		            answer.append("0");	// answer 뒤에 남아있는 0을 모두 추가한다.
		        }
		    }
		}
		else {		// answer가 ""라면
		    if(X_num[0] > 0 && Y_num[0] > 0)
		        return "0";		// 0이 X, Y에서 공통으로 나타나는 경우 "0" return
			else
			    return "-1";	// 짝꿍이 존재하지 않는 것으로, "-1" return
		}
		
		return answer.toString();
	}
}
