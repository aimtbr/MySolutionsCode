package com.company;
import java.util.*;
/**
 * Created by User on 11.10.2017.
 */
public class HanTo {

    private static void Hanto(int m, Stack ori, Stack fin, Stack addi, int a, int b, int c){
        if(m>0) {
            Hanto(m - 1, ori, addi, fin,a,c,b);
            fin.push(ori.peek());
            ori.pop();
            System.out.println("-------------------\nПереносим с " + a + "-го стержня на " + b);
            Print(ori,addi,fin,a,c,b);
            Hanto(m - 1, addi,fin,ori,c,b,a);
        }
    }

    private static void Print(Stack s1, Stack s2, Stack s3, int a, int b, int c){
        int arr[] = new int[3];
        arr[0] = a;
        arr[1] = b;
        arr[2] = c;                                     //ФУНКЦИЯ ДЛЯ КОРРЕКТНОГО ВЫВОДА СОСТОЯНИЯ СТЕРЖНЕЙ
        Arrays.sort(arr);
        for(int i = 0; i < 3; i++){
            if(arr[i] == a){
                System.out.println(arr[i] + "-й стержень" + s1);
            }else if(arr[i] == b){
                System.out.println(arr[i] + "-й стержень" + s2);
            }else if(arr[i] == c){
                System.out.println(arr[i] + "-й стержень" + s3);
            }
        }
    }

    public static void main(String[] args) {
        int k = 3;
        Stack<String> t1 = new Stack<>();
        Stack<String> t2 = new Stack<>();
        Stack<String> t3 = new Stack<>();
        for(int c = 0; c < k; c++){
            t1.push(String.valueOf(k-c));
        }
        Hanto(k, t1, t2, t3, 1, 2, 3);

        //СНИЗУ РАСКОММЕНТИРОВАТЬ ДЛЯ СЧЁТА ВРЕМЕНИ ВЫПОЛНЕНИЯ ПРОГРАММЫ,А СВЕРХУ ЗАКОММЕНТИРОВАТЬ СТРОКИ 38-44

        /*long buff[] = new long[10];
        for(int i = 1; i < 11; i++) {
        Stack<String> t1 = new Stack<>();
        Stack<String> t2 = new Stack<>();
        Stack<String> t3 = new Stack<>();
        for(int c = 0; c < k; c++){
            t1.push(String.valueOf(k-c));
        }
            long start = System.nanoTime();
            Hanto(i, t1, t2, t3, 1, 2, 3);
            long fin = System.nanoTime();
            buff[i-1] = fin-start;
        }
        for(int i = 1; i < 11; i++){
            System.out.println("При N = " + i + ", время выполнения программы составляло " + buff[i-1] + "нс.");
        }*/
    }
}
