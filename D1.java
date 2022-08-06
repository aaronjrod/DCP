import java.io.*;
import java.util.*;

class D1{
    
    private static boolean addUp(int k, int[] list){
        for (int i = 0; i < list.length; i++){
            for (int j = i+1; j < list.length; j++) {
                if (list[i]+list[j] == k) return true;
            }
        }
        return false;
    }

    private static boolean addUp2(int k, int[] list){
        int length = list.length;
        HashSet<Integer> hashset = new HashSet<Integer>();

        for (int i = 0; i < length; i++){
            if (hashset.contains(list[i]))
                return true;
            hashset.add(k-list[i]);
        }
        return false;
    }
    
    public static void main(String[] args) {
        int[] list = {10, 15, 3, 7};
        int k = 30;

        // System.out.println(addUp2(10,list));
        // System.out.println(addUp2(17,list));
        // System.out.println(addUp2(18,list));
        // System.out.println(addUp2(13,list));
        // System.out.println(addUp2(25,list));
        // System.out.println();
        // System.out.println(addUp2(20,list));
        // System.out.println(addUp2(30,list));
        for (int i = 0; i < 26; i++)
            System.out.println(i+": "+addUp2(i,list));
        //System.out.println(list[0]);


    
    }
}
