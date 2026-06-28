class Solution {
public:
    vector<int> nextGreaterElement(vector<int>& nums1, vector<int>& nums2) {
        stack <int> s;
        map <int,int> m;
        vector <int> res ;
        for(int i = 0;i<nums2.size();i++){
            int num = nums2[i];
            m[num] = i;
        }
        for(int i=nums2.size()-1;i>=0;i--){
            int num = nums2[i];
            while(!s.empty()){
                if(s.top() < num){
                    s.pop();
                }else{
                    break;
                }
            }
            if(s.empty()){
                s.push(num);
                nums2[i] = -1;
            }else{
                nums2[i] = s.top();
                s.push(num);
            }
        }
        for(int num:nums1){
            res.push_back(nums2[m[num]]);
        }
        return res;
    }
};