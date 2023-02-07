   static class Solution {
        public long solution(int w, int h) {
            long ref = gcd(w, h);

            return ((long) w * h) - (((w / ref) + (h / ref) - 1) * ref); // 그려보니 못쓰는 사각형 -1 해줘야됨, 최대공배수
        }
        private int gcd(int n, int m) {
            while (m != 0) {
                int r = n % m;

                n = m;
                m = r;
            }

            return n;
        }

    }
