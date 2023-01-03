package level1;

import java.util.Arrays;
import java.util.HashMap;
import java.util.LinkedHashSet;
import java.util.Map;

public class 신고결과받기 {

	public static int[] solution(String[] id_list, String[] report, int k) {
		
		int[] answer = new int[id_list.length];
		
        Map<String, Integer> reported_list = new HashMap<String, Integer>();
        Map<String, Integer> user_list = new HashMap<String, Integer>();
        
        LinkedHashSet<String> hashSet = new LinkedHashSet<String>(Arrays.asList(report));
        String[] new_reported_list = hashSet.toArray(new String[0]);
        
        
        for(int i = 0; i < id_list.length; i++) {
        	reported_list.put(id_list[i], 0);
        	user_list.put(id_list[i], 0);
        }
        

        for(int i = 0; i < new_reported_list.length; i++) {
        	String reported_id = new_reported_list[i].split(" ")[1]; // 신고 당한 애
        	
    		int val = reported_list.get(reported_id);
    		reported_list.replace(reported_id, val+1);
        }
        

        for(int i = 0; i < new_reported_list.length; i++) {
        	String[] temp = new_reported_list[i].split(" ");
        	String user_id = temp[0]; 
        	String reported_id = temp[1];
        	int cnt = reported_list.get(reported_id); 
        	if(cnt >= k) {
        		int val = user_list.get(user_id);
        		user_list.replace(user_id, val+1);
        	}
        }
        for(int i = 0; i < user_list.size(); i++) {
        	answer[i] = user_list.get(id_list[i]);
        }
       
        return answer;
    }
}
