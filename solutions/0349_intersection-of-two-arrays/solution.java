class Solution {
    public int[] intersection(int[] nums1, int[] nums2) {
        HashMap <Integer,Boolean> map = new HashMap<>();
        for(int i=0;i<nums1.length;i++){
            map.put(nums1[i],true);
        }
        ArrayList <Integer> list = new ArrayList<>();
        for(int i=0;i<nums2.length;i++){
            if(map.containsKey (nums2[i])){
                if(map.get(nums2[i]))
                if(!list.contains (nums2[i])){
                    list.add(nums2[i]);
                }
            }
        }
        int [] result = new int[list.size()];
        for(int i=0;i<list.size();i++){
            result[i]=list.get(i);
        }
        return result;
    }
}