package com.company;

//Заменяет повторяющиеся хотя бы 1 раз элементы в строке на скобку ')', а неповторяющиеся '('

/**
 * Created by User on 23.09.2017.
 */
public class DuplicateEncoder {
    static String encode(String word) {
        String words = "";
        word = word.toLowerCase();
        for (int i = 0; i < word.length(); i++) {
            int count = 0;
            for(int j = 0; j < word.length(); j++) {
                if(String.valueOf(word.charAt(j)).equals(String.valueOf(word.charAt(i)))){
                    count++;
                }
            }
            words += (count > 1) ? ")" : "(";
        }
        word = words;
        return word;
    }

    public static void main(String[] args) {
        System.out.println(encode("hih"));
    }
}
