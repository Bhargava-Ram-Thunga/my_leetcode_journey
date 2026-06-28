class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int n = nums.size();
        unordered_map <int,int> man;
        for (int num : nums){
            man[num]++;
            if (man[num] > n/2){
                return num;
            }
        }
        return -1;
    }
};