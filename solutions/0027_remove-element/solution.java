class Solution {
    public int removeElement(int[] nums, int val) {
        int count =0;
        for(int k=0;k<nums.length;k++){
            if(nums[k]!=val)
            {
                nums[count++]=nums[k];
            }
        } 
        return count;
    }
}