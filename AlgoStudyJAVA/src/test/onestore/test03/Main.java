package test.onestore.test03;

import java.io.*;
import java.util.*;

class Solution {
    int solution(int[] A) {
        int N = A.length;
        int result = 0;
        for (int i = 0; i < N; i++)
            for (int j = 0; j < N; j++){
                if (A[i] == A[j]) {
                    System.out.println(Math.abs(i - j) + " " + result);
                    result = Math.max(result, Math.abs(i - j));
                }
                System.out.println("-----");
            }
        return result;
    }
}

class Main {
    public static void main(String[] args) {
        Solution sol = new Solution();
        int[] A = {4, 6, 2, 2, 6, 6, 1};
        System.out.println(sol.solution(A));
    }
}



