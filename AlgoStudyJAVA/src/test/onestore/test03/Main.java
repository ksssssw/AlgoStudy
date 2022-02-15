package test.onestore.test03;

import java.io.*;
import java.util.*;

class Solution {
    int solution(int[] A) {
        int N = A.length;
        ArrayList<Integer> newA = new ArrayList<Integer>();
        Arrays.stream(A).toArray();
        HashMap<Integer, List<Integer>> temp = new HashMap<Integer, List<Integer>>();

        int result = 0;

        for (int i = 0; i < N; i++){
            if (temp.containsKey(A[i])){
                temp.values().add(newA.indexOf(A[i]));
            }
        }

//        for (int i = 0; i < N; i++)
//            for (int j = 0; j < N; j++) {
//                if (A[i] == A[j]) {
//                    result = Math.max(result, Math.abs(i - j));
//                }
//            }
//        return result;
    }
}

class Main {
    public static void main(String[] args) {
        Solution sol = new Solution();
        int[] A = {4, 6, 2, 2, 6, 6, 1};
        System.out.println(sol.solution(A));
    }
}