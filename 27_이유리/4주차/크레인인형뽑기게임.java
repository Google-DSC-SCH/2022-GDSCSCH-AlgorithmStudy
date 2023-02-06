import java.util.Stack;

class Solution {
    public int solution(int[][] board, int[] moves) {
        int answer = 0;
        
        Stack<Integer> basket = new Stack<>();	// 인형을 담을 바구니.
        int doll = 0;
        
        for(int i = 0; i < moves.length; i++) {		// 크레인이 움직인 만큼 반복한다.
        	for(int j = 0; j< board.length; j++) {
        		if(board[j][moves[i] - 1] != 0) {
        			doll = board[j][moves[i] - 1];	// 크레인이 집어든 인형을 변수에 저장.
        			board[j][moves[i] - 1] = 0;		// 인형이 있던 자리를 0으로 변경
        			
        			if(basket.empty())				// 바구니가 비었으면
        				basket.push(doll);			// 인형을 바로 바구니에 넣는다.
        			else {							// 바구니에 인형이 있으면
        				if(basket.peek() == doll) {	// 맨 위에 있는 인형과 크레인이 집어든 인형을 비교하여 둘이 같은 경우
        					basket.pop();			// 바구니에서 인형을 꺼내고
        					answer += 2;			// answer에 사라진 인형의 개수를 더한다.
        				}
        				else {						// 맨 위에 있는 인형과 크레인이 집어든 인형이 다르면
        					basket.push(doll);		// 크레인이 집어든 인형을 바구니에 넣는다.
        				}
        			}
        			break;
        		}
        	}
        }
        
        return answer;
    }
}
