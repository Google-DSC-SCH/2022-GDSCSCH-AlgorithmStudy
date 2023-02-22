package com.example.demo.codingTest;

import java.util.Arrays;

public class 체육복 {

    public static void main(String[] args) {
        Solution s = new Solution();

        int n = 3;
//        int[] lost = {2, 4};
        int[] lost = {1, 2};
//        int[] reserve = {1, 3, 5};
        int[] reserve = {2, 3};

        int solution = s.solution(n, lost, reserve);
        System.out.println(solution);


    }
    static class Solution {
        public int solution(int n, int[] lost, int[] reserve) {
            int answer = 0;
            Arrays.sort(lost);
            Arrays.sort(reserve);
            for(int i=0; i < lost.length; i++) {
                for(int j=0; j < reserve.length; j++) {
                    if(lost[i] == reserve[j]) {
                        lost[i] = -1;
                        reserve[j] = -1;
                        answer++;
                        break;
                    }
                }
            }
            for (int i=0; i < lost.length; i++) {
                for (int j=0; j < reserve.length; j++) {
                    if(lost[i] == reserve[j]+1 || lost[i] == reserve[j]-1) {
                        answer++;
                        reserve[j] = -1;
                        break;

                    }
                }
            }
            return answer + (n - lost.length);

        }
    }
}
