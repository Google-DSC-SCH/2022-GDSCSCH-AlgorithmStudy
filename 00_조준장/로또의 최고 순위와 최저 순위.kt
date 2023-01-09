class Solution {
    fun solution(lottos: IntArray, win_nums: IntArray): IntArray {
        var answer: IntArray = intArrayOf(lottos.count { it == 0 }, 6)
        val rank = intArrayOf(6, 6, 5, 4, 3, 2, 1)

        win_nums.forEach { winNum ->
            if (winNum in lottos) answer[0] += 1
            else answer[1] -= 1

        }
        answer = intArrayOf(rank[answer[0]], rank[answer[1]])

        return answer
    }
}
