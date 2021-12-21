class Solution {
    public int minSubArrayLen(int target, int[] nums) {
        int top = 0;
        int down = 0;
        int total = nums[0];
        int res = 0;
        while(top< nums.length -1){
            if(total<target){
                top++;
                total+=nums[top];
            }else {
                if(res==0) res = top - down + 1;
                else res = Math.min(top-down+1,res);
                total-=nums[down];
                down++;
            }
        }
        while(total>=target){
            if(res==0) res = top - down + 1;
            else res = Math.min(top-down+1,res);
            total-=nums[down];
            down++;
        }
        return res;
    }
}
