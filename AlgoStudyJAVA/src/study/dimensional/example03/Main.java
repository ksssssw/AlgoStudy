package study.dimensional.example03;

import java.io.*;
import java.util.*;

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        List<Integer> nums = new ArrayList<Integer>();
        int[] arr = new int[10];

        for (int i = 0; i < 3; i++) {
            nums.add(Integer.parseInt(br.readLine()));
        }

        int n = nums.get(0) * nums.get(1) * nums.get(2);
        String temp = String.valueOf(n);
        for (int i = 0; i < temp.length(); i++) {
            arr[temp.charAt(i) - 48]++;
        }

        for (int i : arr) {
            System.out.println(i);
        }
    }
}
