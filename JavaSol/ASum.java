package com.company;
/**
 * Created by User on 29.09.2017.
 */
public class ASum {
    public static long findNb(long m) {
        long i = 0;
        long n;
        for(n = 1; i!=m; n++){
            i += (long)Math.pow(n, 3);
            if (i > m) {
                n = -1;
                break;
            }
        }
        n -= (n!=-1) ? 1 : 0;
        return n;
    }

    public static void main(String[] args) {
        System.out.println(findNb(135440716410000L));
    }
}
