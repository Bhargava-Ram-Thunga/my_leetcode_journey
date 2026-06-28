class Solution {
    public int sumOfUnique(int[] nums) {
        int sum = 0;
        int count =0;
        for(int i=0;i<nums.length;i++){
            for(int num : nums){
                if(num==nums[i]){
                    count++;
                }
                if(count>1){
                    break;
                }
            }
            if(count==1){
                sum+=nums[i];
            }
            count=0;
        }
        return sum;
    }
    // public boolean unique(int[] nums,int num){
    //     int count = 0;
    //     for(int i=0;i<nums.length;i++){
    //         if(nums[i]==num){
    //             count++;
    //         }
    //         if(count>1){
    //             return false;
    //         }
    //     }
    //     return true;
    // }
}