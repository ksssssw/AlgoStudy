package test.onestore.test01;

import java.io.*;
import java.util.*;
import static java.util.Collections.sort;

class Solution {
    public static ArrayList<String> result = new ArrayList<String>();

    public String solution(String S) {
        String text[] = S.split("");
        int n = text.length;
        boolean[] visited = new boolean[n];

        combination(text, visited, 0, n, n - 1);
        sort(result);
        return result.get(0);
    }

    public static void combination(String[] text, boolean[] visited, int depth, int n, int r) {
        if (r == 0) {
            print(text, visited, n);
            return;
        }
        if (depth == n) {
            return;
        }
        visited[depth] = true;
        combination(text, visited, depth + 1, n, r - 1);

        visited[depth] = false;
        combination(text, visited, depth + 1, n, r);
    }

    private static void print(String[] text, boolean[] visited, int n) {
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < n; i++) {
            if (visited[i]) {
                sb.append(text[i]);
            }
        }
        result.add(String.valueOf(sb));
    }
}

class Main {
    public static void main(String[] args) {
        Solution sol = new Solution();
        String S = "codility";
        System.out.println(sol.solution(S));
    }
}


