// Last updated: 6/14/2025, 10:33:42 PM
class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int freq=0,ans=0;
        for(int i=0;i<nums.size();i++){
            if(freq==0){
            ans=nums[i];
            }
            if(ans==nums[i]){
                freq++;
            }
            else{
                freq--;
            }
        }
        return ans;
    }
};