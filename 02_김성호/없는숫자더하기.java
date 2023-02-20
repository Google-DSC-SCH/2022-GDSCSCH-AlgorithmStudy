package com.example.demo.codingTest;

import java.util.Arrays;

public class 없는숫자더하기 {
    public static void main(String[] args) {


        int[] numbers = {1,2,3,4,6,7,8,0};

        int solution = solution(numbers);
        System.out.println("solution = " + solution);
    }

    public static int solution(int[] numbers) {
        int answer = 45;

        for (int num : numbers) {
            answer -= num;
        }

        return answer;
    }
}
