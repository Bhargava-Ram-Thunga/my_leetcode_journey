class Solution {
    public int search(int[] nums, int key) {
        int low=0,high=nums.length-1;
        while(low<=high) {
            int mid=(low+high)/2;
            if(nums[mid]==key) {
                return mid;
                }else if(nums[mid]<key) {
                    low=mid+1;
                    }
                    else {
                        high=mid-1;
                        }
                        }
                        return -1;
                        }

    }
