package study.dimensional.example04;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.HashSet;

// 나머지 - 3052
class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        ArrayList<Integer> less = new ArrayList<Integer>();
        for (int i = 0; i < 10; i++) {
            less.add(Integer.parseInt(br.readLine()) % 42);
        }

        HashSet<Integer> result = new HashSet<Integer>(less);

        System.out.println(result.size());
    }
}
