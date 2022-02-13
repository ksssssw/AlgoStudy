package study.dimensional.example02;

import java.io.*;
import java.util.*;

// 최댓값 - 2562
class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        StringBuilder sb = new StringBuilder();

        List<Integer> nums = new ArrayList<Integer>();

        for (int i = 0; i < 9; i++) {
            nums.add(Integer.parseInt(br.readLine()));
        }
        int result = Collections.max(nums);
        sb.append(result).append('\n');
        result = nums.indexOf(result);
        sb.append(result + 1);

        System.out.println(sb);
    }
}
