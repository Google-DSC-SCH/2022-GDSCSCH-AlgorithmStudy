import java.util.Map;

class Solution {
    public String solution(String[] survey, int[] choices) {
        String answer = "";
        // 설문자의 점수를 담을 정수형 배열 선언, 차례대로 R, C, J, A 형의 점수, 반대 점수는 음수로 더한다.
        int[] scores = new int[4];

        // 설문지 점수표를 담을 정수형 배열 선언, i번째 인덱스의 숫자가 i점의 점수
        int[] scoreTable = {0, 3, 2, 1, 0, 1, 2, 3};

        // 계산할 점수 지표를 담을 캐릭터형 선언
        char indicator;

        // 질문지의 길이만큼 순회하여 choices의 i번째 요소를 꺼낸다.
        for(int i = 0; i < choices.length; i++) {
            int choice = choices[i];
            // 꺼낸 점수가 4일 경우 continue
            if (choice == 4) continue;
            // 꺼낸 점수가 1~3일 경우
            if (choice < 4) {
                // survey[i]의 0번째 캐릭터형이 점수 지표
                indicator = survey[i].charAt(0);
            } else {  // 꺼낸 점수가 5~7일 경우
                // survey[i]의 1번째 캐릭터형이 점수 지표
                indicator = survey[i].charAt(1);
            }
            // indicator 에 따라 점수를 계산
            switch(indicator) {
                case 'R':
                    scores[0] += scoreTable[choice];
                    break;
                case 'T':
                    scores[0] -= scoreTable[choice];
                    break;
                case 'C':
                    scores[1] += scoreTable[choice];
                    break;
                case 'F':
                    scores[1] -= scoreTable[choice];
                    break;
                case 'J':
                    scores[2] += scoreTable[choice];
                    break;
                case 'M':
                    scores[2] -= scoreTable[choice];
                    break;
                case 'A':
                    scores[3] += scoreTable[choice];
                    break;
                case 'N':
                    scores[3] -= scoreTable[choice];
                    break;
                default: break;
            }
        }
        // 점수 배열의 0번째 인덱스가 0이상인 경우 결과 문자열에 R, 음수일경우 T를 붙인다.
        if (scores[0] >= 0) {
            answer += "R";
        } else answer += "T";
        // 점수 배열의 1번째 인덱스가 0이상인 경우 결과 문자열에 C, 음수일경우 F를 붙인다.
        if (scores[1] >= 0) {
            answer += "C";
        } else answer += "F";
        // 점수 배열의 2번째 인덱스가 0이상인 경우 결과 문자열에 J, 음수일 경우 M을 붙인다.
        if (scores[2] >= 0) {
            answer += "J";
        } else answer += "M";
        // 점수 배열의 3번째 인덱스가 0이상인 경우 결과 문자열에 A, 음수일 경우 N을 붙인다.
        if (scores[3] >= 0) {
            answer += "A";
        } else answer += "N";
        return answer;
    }
}
