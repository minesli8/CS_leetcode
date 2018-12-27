class Solution {
    public int[] twoSum(int[] nums, int target) {
        int n = nums.length;
        int[] output = new int[2];
        for(int i=0; i<n; i++){
            int a=nums[i];
            for(int j=i+1; j<n; j++){
                int b=nums[j];
                if(a+b==target){
                    output[0]=i;
                    output[1]=j;
                    
                }
                else{
                    continue;
                }
            }
        }
        return output;
    }
}
