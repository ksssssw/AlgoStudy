package study.dimensional.example05;

import kotlin.reflect.jvm.internal.impl.util.collectionUtils.ScopeUtilsKt;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;
import static java.util.Collections.max;

// 평균 - 1546
class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        StringBuilder sb = new StringBuilder();

        int N = Integer.parseInt(br.readLine());
        st = new StringTokenizer(br.readLine(), " ");

        ArrayList<Integer> original = new ArrayList<Integer>();
        for (int i = 0; i < N; i++) {
            original.add(Integer.parseInt(st.nextToken()));
        }

        int M = max(original);
        double result = 0;
        for (int i = 0; i < N; i++) {
            result += (((double)original.get(i) / M) * 100);
        }
        System.out.println(result / N);
    }
}
