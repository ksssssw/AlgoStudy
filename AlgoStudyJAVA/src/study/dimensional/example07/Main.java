package study.dimensional.example07;

import java.io.*;
import java.util.*;

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        StringBuilder sb = new StringBuilder();

        int C = Integer.parseInt(br.readLine());
        for (int i = 0; i < C; i++) {
            st = new StringTokenizer(br.readLine());
            int N = Integer.parseInt(st.nextToken());

            int sum = 0;
            double average = 0;
            int[] scores = new int[N];
            for (int j = 0; j < N; j++) {
                scores[j] = Integer.parseInt(st.nextToken());
                sum += scores[j];
            }
            average = (double) sum / N;

            int cnt = 0;
            for (int k = 0; k < N; k++) {
                if (scores[k] > average) {
                    cnt++;
                }
            }
            sb.append(String.format("%.3f", ((double) cnt / N) * 100)).append("%\n");
        }
        System.out.println(sb);
    }
}
