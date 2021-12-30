class Solution {
    public int[][] generateMatrix(int n) {
        int recur_depth = 0;
        int ini_num = 1;
        int dec_depth = 0;
        int[][] ans = new int[n][n];
        for (int i = n; i >= 0 ; i-=2) {
            dec_depth = 0;
            for (int j = recur_depth; j < i+recur_depth; j++) {
                if(j==recur_depth){
                    for (int k = recur_depth; k < i+recur_depth; k++) {
                        ans[j][k]=ini_num+k-recur_depth;
                    }
                }else if (j==n-recur_depth-1){
                    int kk = 0;
                    for (int k = recur_depth; k < i+recur_depth; k++) {
                        ans[j][k]=3*i-3+ini_num-kk;
                        kk++;
                    }
                }else {
                    ans[j][recur_depth]=4*i-5+ini_num-dec_depth;
                    ans[j][n-recur_depth-1]=ini_num+i+j-1-recur_depth;
                    dec_depth++;
                }
            }
            ini_num=4*i-4+ini_num;
            recur_depth++;
        }
        return ans;
    }
}
