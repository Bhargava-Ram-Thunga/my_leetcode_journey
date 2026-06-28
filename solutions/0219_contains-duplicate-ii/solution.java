class Solution {
    public boolean containsNearbyDuplicate(int[] nums, int k) {
    //     for(int i=0;i<nums.length;i++){
    //         for(int j=0;j<nums.length;j++){
    //             if(i!=j && nums[i]==nums[j]){
    //                 if(Math.abs(i-j)<=k){
    //                     return true;
    //                 }
    //             }
    //         }
    //     }
    //     return false;
        HashMap<Integer,Integer> map=new HashMap<>();
    for(int i=0;i<nums.length;i++){
        if(map.containsKey(nums[i]) && Math.abs(i-map.get(nums[i]))<=k){
            return true;
        }else{
            map.put(nums[i],i);
        }
    }
    return false;

    }
}