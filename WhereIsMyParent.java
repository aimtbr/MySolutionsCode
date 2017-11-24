package com.company;
import java.util.*;
/**
 Mothers arranged dance party for children in school.On that party there are only mothers and their children.
 All are having great fun on dancing floor when suddenly all lights went out.Its dark night and no one can see eachother.
 But you were flying nearby and you can see in the dark and have ability to teleport people anywhere you want.

 Legend:
 -Uppercase letters stands for mothers,lowercase stand for their children. I.E "A" mothers children are "aaaa".
 -Function input:String contain only letters,Uppercase letters are unique.

 Task:
 Place all people in alphabetical order where Mothers are followed by their children.I.E "aAbaBb" => "AaaBbb".
 */
public class WhereIsMyParent {
    static String findChildren(final String text) {
        if(text.length()!=0) {
            String arr_txt[] = new String[text.length()];
            String sorted[] = new String[text.length()];
            String txt_buff = "", txt_buff2 = "", rtrn = "";
            int count = 0;
            for (int i = 0; i < text.length(); i++) {
                arr_txt[i] = String.valueOf(text.charAt(i));
            }
            Arrays.sort(arr_txt);
            for(int j = 0; j < text.length(); j++){
                if(arr_txt[0].equals(arr_txt[0].toUpperCase())){
                    if(arr_txt[j].equals(arr_txt[j].toUpperCase())){
                        txt_buff += arr_txt[j];
                    }else txt_buff2 += arr_txt[j];
                }else txt_buff2 += arr_txt[j];
            }
            if(txt_buff.length() == 0){
                return txt_buff2;
            }else if (txt_buff2.length() == 0){
                return txt_buff;
            }else {
                for (int i = 0; i < txt_buff.length(); i++) {
                    sorted[count] = String.valueOf(txt_buff.charAt(i));
                    count++;
                    for (int j = 0; j < txt_buff2.length(); j++) {
                        if (String.valueOf(txt_buff.charAt(i)).equals(String.valueOf(txt_buff2.charAt(j)).toUpperCase())) {
                            sorted[count] = String.valueOf(txt_buff2.charAt(j));
                            count++;
                        }
                    }
                }
                if (count == txt_buff.length()){
                    for(int i = 0; i < txt_buff2.length(); i++){
                        sorted[count] = String.valueOf(txt_buff2.charAt(i));
                        count++;
                    }
                }
            }
            for(int i = 0; i < text.length(); i++){
                rtrn += sorted[i];
            }
            return rtrn;
        }else return "";
    }

    public static void main(String[] args) {
        System.out.println(findChildren("ZgGgPVvggFvpCDdddXxxxRrrrEee"));
    }
}
