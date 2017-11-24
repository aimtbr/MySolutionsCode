package com.company;

public class Line {
    public static String Tickets(int[] peopleInLine)
    {
        String answer;
        int twfi = 0, fif = 0;
        for(int i = 0; i < peopleInLine.length; i++){
            switch(peopleInLine[i]){
                case 25: {
                    twfi++;
                    break;
                }
                case 50: {
                    if(twfi > 0){
                        twfi--;
                        fif++;
                    }else return answer = "NO";
                    break;
                }
                case 100: {
                    if(twfi >= 1 && fif >= 1){
                        twfi--;
                        fif--;
                    }else if(twfi >= 3){
                        twfi = twfi - 3;
                    }else return answer = "NO";
                    break;
                }
                default: return answer = "NO";
            }
        }
        return answer = "YES";
    }

    public static void main(String[] args) {
        int[] peopleInLine = {25,50,100};
        System.out.println(Tickets(peopleInLine));
    }
}
