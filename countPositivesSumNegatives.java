package com.company;
import java.util.Arrays;

public class countPositivesSumNegatives {
    public static int[] countPositivesSumNegatives(int[] input)
    {
        int[] count = new int[2];
        if(input != null) {
            if(input.length != 0) {
                for (int i = 0; i < input.length; i++) {
                    count[0] += (input[i] > 0) ? 1 : 0;
                    count[1] += (input[i] < 0) ? input[i] : 0;
                }
            }else count = new int[]{};
        }else count = new int[]{};
        return count;
    }

    public static void main(String[] args) {
        int[] input = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15};
        System.out.println(Arrays.toString(countPositivesSumNegatives(input)));
    }
}
