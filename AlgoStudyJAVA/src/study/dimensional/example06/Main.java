package study.dimensional.example06;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

// OX 퀴즈 - 8958
class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int N = Integer.parseInt(br.readLine());
        String[] scores = new String[N];
        for (int i = 0; i < N; i++) {
            scores[i] = br.readLine();
        }

        for (int i = 0; i < N; i++) {
            String[] temp = scores[i].split("X");
            int result = 0;
            for (String j : temp) {
                for (int k = 1; k < j.length() + 1; k++) {
                    result += k;
                }
            }
            sb.append(result).append('\n');
        }
        System.out.println(sb);
    }
}
