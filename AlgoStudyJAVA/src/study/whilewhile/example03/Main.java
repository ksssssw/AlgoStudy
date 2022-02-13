package study.whilewhile.example03;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

// 더하기 사이클 - 1110
class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int cnt = 0;
        int N = Integer.parseInt(br.readLine());
        int temp = N;

        do {
            temp = ((temp % 10) * 10) + (((temp / 10) + (temp % 10)) % 10);
            cnt++;
        } while (N != temp);
        System.out.println(cnt);
    }
}
