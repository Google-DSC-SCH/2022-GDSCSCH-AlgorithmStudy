class Solution {
    fun solution(new_id: String): String {
        return new_id
                .toLowerCase() // 소문자로 변환
                .filter { it.isLowerCase() || it.isDigit() || it == '-' || it == '_' || it == '.' } // filter 키워드를 통해 소문자이거나 숫자이거나 "-", "_", "."인 문자만을 반환
                .replace("[.]*[.]".toRegex(), ".") // 정규 표현식을 통해 "."의 개수가 2개 이상일 경우 "."으로 변환
                .removePrefix(".").removeSuffix(".") // 첫 번째와 마지막 문자가 "."일 경우 제거
                .let { it.ifEmpty { "a" } } // 문자열이 비어있다면 "a"를 반환
                .let {// 문자열의 길이가 16보다 크다면 15까지 잘라서 반환
                    if (it.length >= 16) it.substring(0, 16).removeSuffix(".") else it
                }
                .let {// 문자열의 길이가 2이하라면 3이 될 때까지 마지막 문자를 더해준다.
                    if (it.length <= 2) {
                        val sb = StringBuilder(it)
                        while (sb.length != 3)
                            sb.append(it.last())
                        sb.toString()
                    } else it
                }
    }
}
