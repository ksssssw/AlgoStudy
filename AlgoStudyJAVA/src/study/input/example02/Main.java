package study.input.example02;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] s = br.readLine().split(" ");
        int result = Integer.parseInt(s[0]) + Integer.parseInt(s[1]);
        System.out.println(result);
    }
}
