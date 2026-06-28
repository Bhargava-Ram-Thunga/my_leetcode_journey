class Solution {
    public String[] sortPeople(String[] names, int[] heights) {
        int n=names.length;

       HashMap<Integer,String> map=new HashMap<>();
       for(int i=0;i<n;i++){
           map.put(heights[i],names[i]);
       }
       Arrays.sort(heights);
       int k=0;
       for(int i=n-1;i>=0;i--){
           names[k]=map.get(heights[i]);
           k++;
       }
       return names;
    }
}