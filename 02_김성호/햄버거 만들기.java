import java.util.*;

class Solution {
    public int solution(int[] ingredient) {
        ArrayList<Integer> temp = new ArrayList();
        int result = 0;

        for (int i=0; i<ingredient.length; i++) {
            temp.add(ingredient[i]);
            if (temp.size()>=4){
                if(temp.get(temp.size()-4)==1 && temp.get(temp.size()-3)==2 && temp.get(temp.size()-2)==3 && temp.get(temp.size()-1)==1) {

                    result++;

                    for(int j=0; j<4; j++) {
                        temp.remove(temp.size()-1);
                    }
                }

            }
        }
        
        return result;
    }
}
