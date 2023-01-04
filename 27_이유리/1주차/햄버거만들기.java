import java.util.Stack;

class Solution {
    public int solution(int[] ingredient) {
        int answer = 0;
        Stack stack = new Stack();
        int sSize;
        
        for(int i : ingredient) {
        	stack.push(i);
        	sSize = stack.size();
        	
        	// 재료들이 쌓인 상태가 햄버거를 포장할 수 있는지 확인
        	if(sSize >= 4 && 
        			stack.elementAt(sSize-4).equals(1) && 
        			stack.elementAt(sSize - 3).equals(2) &&
        			stack.elementAt(sSize - 2).equals(3) && 
        			stack.elementAt(sSize - 1).equals(1)) {
        		answer++;					// 햄버거 포장이 가능하면 answer++
        		for(int j = 0; j < 4; j++)	// 햄버거를 포장하고 나면 pop으로 사용한 재료 삭제
        			stack.pop();
        	}
        }
        
        return answer;
    }
}
