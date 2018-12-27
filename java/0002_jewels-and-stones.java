class Solution {
    public int numJewelsInStones(String J, String S) {
        int len_S = S.length();
        
        int count = 0;
        
        String arr[] = S.split("");
        for(int i=0; i<len_S; i++){
            
            if(J.indexOf(arr[i])!=-1){
                count += 1;
            }
            
        }
        
        return count;
    }
}
