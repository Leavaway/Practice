class Solution {
    public int[] sortedSquares(int[] nums) {
        int left = 0;
        int right = nums.length -1;
        int[] res = new int[nums.length];
        int point = nums.length -1;
        while (left <= right){
            if(Math.abs(nums[right])>=Math.abs(nums[left])){
                res[point] = (int) Math.pow(nums[right], 2);
                right--;
                point--;
            }else {
                res[point] = (int) Math.pow(nums[left], 2);
                left++;
                point--;
            }
        }
        return res;
    }
}
