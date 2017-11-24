package com.company;
import java.util.*;
import java.io.*;

//Все слова в тексте из файла пишет в предложениях наоборот / буквы в каждом предложении пишутся задом наперёд

/**
 * Created by User on 09.09.2017.
 */
public class Lab1_ASD {
    static String fline, temp = "", chars = "";

    private static void StrRead (String pathIn, String pathOut){
            try {
                File file = new File(pathIn);           //ФАЙЛ С ТЕКСТОМ
                File fileOut = new File(pathOut);       //ФАЙЛ, В КОТОРОМ СЛОВА В ПРЕДЛОЖЕНИЯХ БУДУТ ЗАПИСАНЫ НАОБОРОТ
                if (fileOut.exists()){
                    fileOut.delete();
                    fileOut.createNewFile();
                }
                Stack<String> stack = new Stack<>();
                FileInputStream fis = new FileInputStream(file);    //открываем поток ввода данных с файла
                InputStreamReader isr = new InputStreamReader(fis, "Cp1251"); //обработка байтов и их декодирование в символы
                BufferedReader br = new BufferedReader(isr);     //объект для чтения текста из входящего потока
                BufferedOutputStream bos = new BufferedOutputStream(new FileOutputStream(fileOut)); //открываем потом вывода данных
                OutputStreamWriter osw = new OutputStreamWriter(bos,"Cp1251");  //обработка символов в байты кодировки Cp1251
                BufferedWriter bw = new BufferedWriter(osw);        //объект для записи символов в поток вывода
                while ((fline = br.readLine()) != null) {   //пока конец файла не достигнут перезаписывает строку в переменную
                    for (int i = 0; i < fline.length(); i++){      //цикл работает пока не достигнут конец строки
                        temp = temp + String.valueOf(fline.charAt(i));    //добавляет в строку по символу из строки
                        if(i == fline.length()-1) {      //если цикл дошёл до последнего элемента, то
                            stack.push(temp);           //добавляет в стек строку со словом
                            chars = chars + StChar(temp);//добавляет к строке слово в котором буквы задом наперёд
                            temp = "";                  //очищает строку со словом
                            while (!(stack.isEmpty())) {      //пока стек не пуст..
                                bw.write(stack.peek() + " ");   //записывает в файл слова предложения задом наперёд
                                stack.pop();
                            }
                        }else if(String.valueOf(fline.charAt(i)).equals(" ")){      //если слово закончилось, то
                            if(i != 0){                         //если строка не начинается с пустого элемента, то
                                temp += " ";
                                stack.push(temp);
                                chars = chars + StChar(temp);
                                temp = "";
                            }
                            while (String.valueOf(fline.charAt(i)).equals(" ")) {//пока предложение начинается с пустого элемента, то
                                i++;                                //пропускает этот элемент
                                if(i == fline.length()-1){          //если пустой элемент находится в конце строки, то
                                    break;                          //прекращается пропуск элемента
                                }
                            }
                            i--;
                        } else if(String.valueOf(fline.charAt(i+1)).equals(",") || String.valueOf(fline.charAt(i+1)).equals(".")
                                || String.valueOf(fline.charAt(i+1)).equals("?")) {
                            temp += " ";
                            stack.push(temp);
                            chars = chars + StChar(temp);
                            temp = "";
                        }
                    }
                    chars +="\r\n";
                    bw.write("\r\n");               //переход на новую строку в файле
                }
                InFile(chars,"C:\\Users\\User\\Desktop\\Lab1_ASD\\test2.txt"); //В ЭТОТ ФАЙЛ ЗАПИСЫВАЮТСЯ БУКВЫ ЗАДОМ НАПЕРЁД
                br.close();             //закрывает
                bw.close();             //потоки
            }catch (Exception e) {
                System.out.println("\n ERROR");
            }
    }

    private static String StChar(String temp){
        Stack <String> stck = new Stack<>();
        String ch = "";
        for(int i = 0; i < temp.length(); i++){         //пока не достигнут конец строки
            stck.push(String.valueOf(temp.charAt(i)));      //добавляет в стек по символу из строки
        }
        while(!(stck.isEmpty())){           //пока стек не пуст
            ch = ch + stck.peek();          //к новой строке добавляет по символу из стека
            stck.pop();
        }
        return ch;
    }

    private static void InFile(String str, String path){
        try {
            File file = new File(path);
            if (file.exists()) {
                file.delete();
                file.createNewFile();
            }
            BufferedOutputStream bos = new BufferedOutputStream(new FileOutputStream(file));
            OutputStreamWriter osw = new OutputStreamWriter(bos,"Cp1251");
            BufferedWriter bw = new BufferedWriter(osw);
            bw.write(str);
            bw.close();
        }catch (Exception e){
            System.out.println("\n ERROR");
        }
    }

    public static void main(String[] args) throws IOException {
        StrRead("ПУТЬ К ФАЙЛУ С ИСХОДНЫМ ТЕКСТОМ","ПУТЬ К ФАЙЛУ В КОТОРЫЙ ЗАПИШЕТ");
    }
}
