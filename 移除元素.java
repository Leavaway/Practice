class Solution {
    public int removeElement(int[] nums, int val) {
        int fast = 0;
        int slow = 0;
        while (fast<nums.length){
            nums[slow] = nums[fast];
            if(nums[slow]==val){
                fast++;
            }else {
                fast++;
                slow++;
            }
        }
        return slow;
    }
}
