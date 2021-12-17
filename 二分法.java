public class Solution {
    public int search(int[] nums, int target) {
        int left = 0;
        int right = nums.length - 1;
        return search_tar(left,right,nums,target);
    }
    public int search_tar(int left,int right,int[] nums,int target){
        if(left>right) return -1;
        int mid = (left + right)/2;
        if(target>nums[mid]){
            return search_tar(mid+1,right,nums,target);
        }else if(target<nums[mid]){
            return search_tar(left,mid-1,nums,target);
        }else if(target==nums[mid]){
            return mid;
        }
        return -1;
    }
}
