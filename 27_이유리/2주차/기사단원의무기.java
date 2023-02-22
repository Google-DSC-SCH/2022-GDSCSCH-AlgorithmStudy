import java.util.HashMap;
import java.util.Map;

class Solution {
    public int solution(int number, int limit, int power) {
        int answer = 0;
        int[] aliquot_num = new int[number];
        aliquot_num[0] = 1;	// 가장 첫 번째 값인 1은 항상 약수가 1개이기 때문에 값을 초기화
        
        HashMap<Integer, Integer> map; // 소인수분해 결과를 넣을 HashMap. key에는 소인수, value에는 소인수의 거듭제곱 회수
        int prime, N;
        
        /* 가장 먼저 number를 소인수분해하여 약수의 개수를 구하는 공식에 맞춰 약수의 개수를 구한다.
         * 약수의 개수를 순서대로 배열에 넣는다.
         * 약수의 개수가 limit보다 크다면, power값으로 교체한다.
         * 약수의 개수 배열에 있는 수들을 모두 합하여 return한다. */
        
        for(int i = 2; i <= number; i++) {
        	map = new HashMap<>();	// HashMap 초기화
        	N = i;
        	prime = 2;
        	while(prime <= N) {	// 소인수분해
        		if(N%prime == 0) {
        			N /= prime;
        			if(map.get(prime) != null) 	// 현재 나눈 소인수를 key값으로 하는 value가 있다면
        				map.put(prime, map.get(prime) + 1);	// value값을 +1한다.
        			else						// 현재 소인수가 hashmap에 없다면
        				map.put(prime, 1);		// vlaue값을 1로하여 추가한다.
        		}
        		else 
        			prime++;
        	}
        	
        	// 약수의 개수를 구하여 배열에 추가한다.
        	for(Map.Entry<Integer, Integer> entry : map.entrySet()) {
        		if(aliquot_num[i - 1] == 0) {
        			aliquot_num[i - 1] = entry.getValue() + 1;
        		}
        		else {
        			aliquot_num[i - 1] *= (entry.getValue() + 1);
        		}
        	}
        }
        
        // 약수의 개수가 limit을 초과하면 answer에 power값을 추가하고, 그렇지 않으면 약수의 개수를 그대로 answer에 추가한다.
        for(int i = 0; i < number; i++) {
        	if(aliquot_num[i] > limit)
        		answer += power;
        	else 
        		answer += aliquot_num[i];
        }
        
        return answer;
    }
}
