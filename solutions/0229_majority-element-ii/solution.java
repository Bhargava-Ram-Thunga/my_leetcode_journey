class Solution {
    public List<Integer> majorityElement(int[] nums) {
        int n= nums.length;
        ArrayList <Integer> list = new ArrayList<>();
        HashMap <Integer,Integer> map = new HashMap <>();
        for(int i=0;i<n;i++){
            map.put(nums[i],map.getOrDefault(nums[i],0)+1);
            if(map.get(nums[i])>n/3){
                if(!list.contains(nums[i])){
                    list.add(nums[i]);
                }
            }
        }
        return list;
    }
}