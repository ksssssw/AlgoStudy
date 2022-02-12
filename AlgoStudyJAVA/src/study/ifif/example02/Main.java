package study.ifif.example02;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String s = br.readLine();
        int score = Integer.parseInt(s);

        switch (score / 10){
            case 6:
                System.out.println("D");
                break;
            case 7:
                System.out.println("C");
                break;
            case 8:
                System.out.println("B");
                break;
            case 9:
                System.out.println("A");
                break;
            case 10:
                System.out.println("A");
                break;
            default:
                System.out.println("F");
                break;
        }
    }
}
