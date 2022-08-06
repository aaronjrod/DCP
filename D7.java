public class D7 {
    //Idea: Legal message, break off
    // Meybe somethine like mergesort?
    // Recursive implementation: Is legal? Add +1 if encoding is legal
    //Ex. 11: (1,1), (11)                                                                       //2
    //Ex. 111: (1,11), (1,1,1), (11,1), (111)X                                                  //3
    //Ex. 1111: (1,111)X, (1,1,11), (1,1,1,1), (1,11,1), (11,11), (11,1,1)          //5
    // 1*2 + 1
    // Fibonacci?
    // What about 101? (10,1) but not (1,0,1)
    // Can remove only 2 digits per check
    //int, 
    static int recurDecode(int n){
        //int length = (n+"").length();

        // If 
        if (n < 9){
            //System.out.print(n+", ");
            return 1;
        } 
        // If n = 10 or 20
        int x = removeFirstDigit(n);
        if (x == 0) return 1;

        if (getFirstTwoDigits(n) > 10 && getFirstTwoDigits(n) <= 26 && getFirstTwoDigits(n) != 20) {
            return recurDecode(x) + recurDecode(removeFirstDigit(x));
        }
        return recurDecode(x);
    }

    static int removeFirstDigit(int n){
        return n % (int) Math.pow(10, (int) Math.log10(n));
    }

    static int getFirstTwoDigits(int n){
        while (n > 99) {
            n /= 10;
        }
        return n;
    }

    public static void main(String[] args) {
        //System.out.println("\n"+recurDecode(101));
        
        int[] list = {1,11,111,1111,10,101,202,201,1259,39,2020,123426,30};
        int ans;
        for (int num : list){
            ans = recurDecode(num);
            System.out.println(num + ": "+ ans);
        }
        //1,2,3,4,2,6
        //1,2,3,4,26
        //1,23,4,2,6
        //1,23,4,26
        //12,3,4,2,6
        //12,3,4,26


    }
}
