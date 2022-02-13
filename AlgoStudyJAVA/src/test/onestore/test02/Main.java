package test.onestore.test02;

import java.io.*;
import java.util.*;

class Solution {
    public int[] solution(String[] cars) {
        int n = cars.length;
        int[] result = new int[n];

        for (int i = 0; i < n; i++) {
            int score = 0;
            for (int j = 0; j < n; j++) {
                if (i == j) continue;

                String a = cars[i];
                String[] tempA = a.split("");
                String b = cars[j];
                String[] tempB = b.split("");

                int cnt = 0;
                for (int k = 0; k < tempA.length; k++) {
                    if (tempA[k].equals(tempB[k])) {
                        cnt++;
                    }
                }
                if (cnt == a.length() - 1 || cnt == a.length() + 1 || cnt == a.length()) {
                    score++;
                }
                result[i] = score;
            }

        }
        return result;
    }
}

class Main {
    public static void main(String[] args) {
        Solution sol = new Solution();
        String[] cars = {"100", "110", "010", "011", "100"};
        int[] result = new int[5];
        result = sol.solution(cars);
        System.out.println(result[4]);
    }
}


