class Solution {
    public int missingNumber(int[] nums) {
        // int sum =0;
        // int n = nums.length;
        // for(int i=0;i<n;i++){
        //     sum+=nums[i];
        // }
        // int sumOfN = n*(n+1)/2;
        // int missing = sumOfN - sum;
        // return missing;
        int xor = 0, i = 0;
        for (i = 0; i < nums.length; i++) {
             xor = xor ^ i ^ nums[i];
             }
             return xor ^ i;  
    }
    
}