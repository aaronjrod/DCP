import java.io.*;
import java.util.*;

class D2{
    
    private static int[] sol1(int[] input){
        int product = 1;
        int length = input.length;
        int[] output = new int[length];
        for (int i : input)
            product *= i;
        for (int i = 0; i < input.length; i++)
            output[i] = product/input[i];
        return output;
    }

    private static int[] sol2(int[] input){
        int length = input.length;
        int[] output = new int[length];
        for (int i = 0; i < length; i++)
            output[i] = 1;

        for (int i = 0; i < length; i++){
            for (int j = 0; j < length; j++) {
                if (j!=i)
                    output[i] *= input[j];
            }
        }
        return output;
    }

    // No way to DP? 
    
    private static String toString(int[] input){
        String str = "";
        for (int i : input)
            str += i + " ";
        return str;
    }

    public static void main(String[] args) {
        int[] input = {1, 2, 3, 4, 5};
        int[] input2 = {3,2,1};
        System.out.println(toString(sol1(input)));
        System.out.println(toString(sol1(input2)));

        System.out.println(toString(sol2(input)));
        System.out.println(toString(sol2(input2)));
        // System.out.println(addUp2(10,list));
        // System.out.println(addUp2(17,list));
        // System.out.println(addUp2(18,list));
        // System.out.println(addUp2(13,list));
        // System.out.println(addUp2(25,list));
        // System.out.println();
        // System.out.println(addUp2(20,list));
        // System.out.println(addUp2(30,list));
        
        //System.out.println(list[0]);


    
    }
}
