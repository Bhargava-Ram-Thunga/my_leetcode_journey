class Solution {
    public boolean findSubarrays(int[] nums) {
        int n = nums.length;
        HashSet <Integer> set = new HashSet<>();
        for(int i=1;i<n;i++){
            int sum = nums[i-1]+nums[i];
            if(! set.add(sum)){
                return true;
            }
        }
        return false;
    }
}