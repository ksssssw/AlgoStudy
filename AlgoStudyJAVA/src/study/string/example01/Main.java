package study.string.example01;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

// 아스키코드 - 11654
class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int A = br.read();
        System.out.println(A);
    }
}