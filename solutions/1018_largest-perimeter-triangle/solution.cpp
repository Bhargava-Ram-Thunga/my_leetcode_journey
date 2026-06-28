class Solution {
public:
    int largestPerimeter(vector<int>& nums) {
        sort(nums.begin(),nums.end());
        int i;
        int a,b,c;
        for(int i=nums.size()-1;i>=2;i--){
            a = nums[i-2];
            b = nums[i-1];
            c = nums[i];
            if ((a+b)>c && (b+c)>a && (a+c)>b ){
                return a+b+c;
            }
        }
        return 0;
    }
};