import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashSet;
import java.util.List;

class Solution {
    public int[] solution(String[] id_list, String[] report, int k) {
        int[] answer = new int[id_list.length];
        int i = 0;
        
        List<String> id_list_cp = Arrays.asList(id_list);					// indexOf를 사용하기 위해 id_list를 asList사용하여 변환
        HashSet<String> hs = new HashSet<>(Arrays.asList(report));			// 중복 신고 제거
        ArrayList<String>[] report_list = new ArrayList[id_list.length];	// id별 신고한 이용자 목록
        int[] report_count = new int[id_list.length];						// id별 신고당한 횟수
        ArrayList<String> report_result = new ArrayList<>();				// 신고 당한 횟수가 k번 이상인 이용자 목록
        
        for (int j = 0; j < id_list.length; j++) {	// ArrayList 할당
        	report_list[j] = new ArrayList<String>();
        }
  
        
        for(String s : hs) {
        	String[] tmp = s.split(" ");
        	
        	report_list[id_list_cp.indexOf(tmp[0])].add(tmp[1]);	// 신고한 이용자 index위치에 신고당한 이용자의 id를 추가
        	report_count[id_list_cp.indexOf(tmp[1])]++;				// 신고당한 이용자 index위치에 ++하여 횟수 표시
        }
        
        for(int j = 0; j < report_count.length; j++) {
        	if(report_count[j] >= k) 								// 신고당한 횟수가 k번 이상이면
        		report_result.add(id_list[j]);						// stack에 push
        }
        
        for(int j = 0; j < id_list.length; j++) {
        	for(int n = 0; n < report_result.size(); n++) {
        		if(report_list[j].contains(report_result.get(n)))
        			answer[j]++;	// 신고당한 횟수가 k번 이상인 이용자를 신고한 이용자의 index위치 값을 ++하여 메일을 보냈음을 표시
        	}
        }
        
        return answer;
    }
}
