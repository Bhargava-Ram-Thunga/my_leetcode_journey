class Solution {
    public List<List<Integer>> findDifference(int[] nums1, int[] nums2) {
        List<List<Integer>> Answer = new ArrayList<>();
        ArrayList<Integer> Answer1 = new ArrayList<>();
        ArrayList<Integer> Answer2 = new ArrayList<>();
        HashSet<Integer> Set1 = new HashSet<>();
        HashSet<Integer> Set2 = new HashSet<>();
        Answer.add(Answer1);
        Answer.add(Answer2);
        for(int num:nums1){
            Set1.add(num);
        }
        for(int num:nums2){
            Set2.add(num);
        }
        for(int num:nums1){
            if(!Set2.contains(num) && !Answer1.contains(num)){
                Answer1.add(num);
            }
        }
        for(int num:nums2){
            if(!Set1.contains(num) && !Answer2.contains(num)){
                Answer2.add(num);
            }
        }
        return Answer;
    }
}