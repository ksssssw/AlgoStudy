package study.ifif.example05;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] s = br.readLine().split(" ");
        int hour = Integer.parseInt(s[0]);
        int minute = Integer.parseInt(s[1]);
        int temp = minute - 45;

        if(temp < 0){
            if(hour == 0){
                System.out.println(23 + " " + (60 + temp));
            }else{
                System.out.println((hour - 1) + " " + (60 + temp));
            }
        }else{
            System.out.println(hour + " " + (temp));
        }
    }
}
