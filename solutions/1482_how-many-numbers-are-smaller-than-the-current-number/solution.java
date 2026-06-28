class Solution {
    public int[] smallerNumbersThanCurrent(int[] nums) {
        int count = 0, n = nums.length;
        int[] result = new int[n];

        for(int i = 0; i < n; i++){
            for(int j = 0; j < n; j++){
                if(i != j){
                    if(nums[i] > nums[j]){
                        count++;
                    }
                }
            }
            result[i] = count;
            count = 0;
        }

        return result;
    }
}