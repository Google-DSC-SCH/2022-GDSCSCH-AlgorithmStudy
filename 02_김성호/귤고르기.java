package com.example.demo.codingTest;

import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.stream.Collectors;

public class 귤고르기 {

    public static void main(String[] args) {
        int k = 6;
        int[] tangerine = {1, 3, 2, 5, 4, 5, 2, 3};

        int solution = solution(k, tangerine);
        System.out.println("solution = " + solution);


    }
    public static int solution(int k, int[] tangerine) {
        int answer = 0;
        HashMap<Integer, Integer> map = new HashMap<>();

        for (int size: tangerine) {
            map.put(size, map.getOrDefault(size, 0)+1);
        }

        List<Integer> values = map.values().stream().collect(Collectors.toList());
        Collections.sort(values, ((o1, o2) -> o2-o1));

        int cnt = 0;
        for (int i : values){
            cnt += i;
            answer++;
            if(cnt >= k) break;

        }

        return answer;
    }


}
