//n(n+1)/2 - sum of nonzeroes, count and add
// if output is zero, return count+1
// The array can contain duplicates and negative numbers as well... Bruh!
// Each element, we know its no longer missing
// swap

//so maybe... don't need to swap it to where is has to be, just get rid of repeats and negs

public class D4 {

    static private int missingInt(int[] arr){
        //if (a)
        

        
        int temp = 0;
        for (int i = 0; i < arr.length; i++) {
            //Check if term to swap is valid
            // If value is currently in right place we good, otherwise concerned
            if (arr[i] > 0 && (arr[i] == i+1 || arr[i] != arr[arr[i]-1])){
                //Swap
                temp = arr[i];
                arr[i] = arr[temp-1];
                arr[temp-1] = temp;

                // Removed invalids swapped in
                if (arr[i] <= i)
                    arr[i] = 0;
                // Swap first, then check after swap?
            }
            // Remove repeats/negs
            else {
                arr[i] = 0;
            }
        }
        int count = 1;
        int total = 0;
        for (int num : arr) {
            total += num;
            if(num!=0) count++;
        }
        
        int sumExp = count*(count+1)/2;
        return sumExp - total;
    }

    public static void main(String[] args) {
        int[] arr1 = {1,-3,-10, 2, 4, 1, 3, 3, 3, -5,5};
        int[] arr2 = {};
        int[] arr3 = {1, 2, 0};
        int[] arr4 = {0,1,2,4,3};
        int[] arr5 = {2,4,3};
        //System.out.println(missingInt(arr1)); //6
        //System.out.println(missingInt(arr2)); //1?
        //System.out.println(missingInt(arr3)); //3
        //System.out.println(missingInt(arr4)); //5
        System.out.println(missingInt(arr5)); //1
    }
}

