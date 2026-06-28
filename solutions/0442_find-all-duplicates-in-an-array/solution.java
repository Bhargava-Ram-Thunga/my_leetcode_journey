class Solution {
    public List<Integer> findDuplicates(int[] nums) {
        HashMap <Integer,Boolean> map = new HashMap<>();
        ArrayList <Integer> list = new ArrayList<>();
        for(int num:nums){
            if(map.containsKey(num)){
                list.add(num);
            }
            else{
                map.put(num,true);
            }
        }
        return list;
    }
}