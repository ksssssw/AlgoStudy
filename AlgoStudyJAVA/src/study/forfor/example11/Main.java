package study.forfor.example11;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] s = br.readLine().split(" ");
        int N = Integer.parseInt(s[0]);
        int X = Integer.parseInt(s[1]);

        String[] nums = br.readLine().split(" ");
        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < N; i++){
            if(Integer.parseInt(nums[i])<X){
                sb.append(Integer.parseInt(nums[i])).append(" ");
            }
        }
        System.out.println(sb);
    }
}
