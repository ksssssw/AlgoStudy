package study.ifif.example03;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String s = br.readLine();
        int year = Integer.parseInt(s);

        if(year % 4 == 0 && (year % 100 != 0 || year % 400 == 0)){
            System.out.println("1");
        }else{
            System.out.println("0");
        }
    }
}
