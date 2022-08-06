import java.util.Arrays;

public class D9 {
    //Is 5 part of the optimal solution?
    // Numbers can be 0 or negative
    // Is the first element of the array part of the optimal solution?
    // DP: ineff, but would work
    // Say we pick 2. Then 4 is not part of curr. sol.; cont. 

    public static<T> int[] subArray(int[] array, int beg, int end) {
        return Arrays.copyOfRange(array, beg, end + 1);
    }
    
    //Dyanmic programming approach (optimal substructure holds)
    //Best solution is probably some iterative version of this
    public static int largestSumDP(int[] arr){
        int largest = 0;
        int total = 0;
        int len = arr.length;

        //Pretty sure this is useless
        if (len == 0)
            return 0;

        for (int i = 0; i < len; i++) {
            //If subarray too small to be considered (ex. {1,2}, i=0, len=2)
            //Will iterate to next one, so we good (both i=0, i=1 considered still, just no recursive cal)
            if (i+2>len-1)
                total = arr[i];
            //Add arr[i] and the optimal substructure solution, compare
            else{
                total = arr[i] + largestSumDP(subArray(arr,i+2,len-1));
            }
            if (total > largest)
                largest = total;
        }
        return largest;
    }

    //If I were to write a better soln....
    //Ignore negs for now, make em 0
    //If 0, then optimal soln. would have either cur index or next index, no need for big cascading (greedy choice)
    //Still recursive? Just || instead of for loop
    public static int largestSumV2(int[] arr){
        //Fix negs
        int len = arr.length;
        if (len == 0) return 0;

        if (arr[0] < 0) arr[0] = 0;
        if (len == 2){
            if (arr[1] < 0) arr[1] = 0;
            return Math.max(arr[0], arr[1]);
        }
        else if (len == 1)
            return arr[0];

        return Math.max(arr[0] + largestSumV2(subArray(arr,2,len-1)), largestSumV2(subArray(arr,1,len-1)));
    }

    public static int largestSumV3(int[] arr){
        return largestSumIndex(arr, 0);
    }

    private static int largestSumIndex(int[] arr, int i){
        //Fix negs
        int len = arr.length;
        if (len == 0) return 0;

        if (arr[i] < 0) arr[i] = 0;
        //End case
        if (len-i == 2){
            if (arr[i+1] < 0) arr[i+1] = 0;
            return Math.max(arr[i], arr[i+1]);
        }
        else if (len-i == 1)
            return arr[i];

        return Math.max(arr[i] + largestSumIndex(arr, i+2), largestSumIndex(arr,i+1));
    }

    // Bottom-up implementation
    // Bottom up: Add either this index to the prev-prev or keep prev (whichever bigger)
    public static int largestSumV4(int[] arr){
        int len = arr.length;
        if (len == 0) return 0;

        //if (arr[0] < 0) arr[0] = 0;
        if (len == 1) return arr[0];
        
        arr[1] = Math.max(arr[0], arr[1]);
        if (len == 2) return arr[1];
        
        for (int i = 2; i < len; i++){
            //if (arr[i] < 0) arr[i] = 0;
            arr[i] = Math.max(arr[i],Math.max(arr[i]+arr[i-2], arr[i-1]));
        }
        return arr[len-1];
    }



    public static void main(String[] args) {
        int[] arr = {-1,-2,-5,-8,5,2,5,7,4,2,42};
        int[] arr2 = {2, 4, 6, 2, 5};
        int[] arr3 = {5,1,1,5};
        int[] arr4 = {-1};
        int[] arr5 = {1,2,5,8};
        int[] arr6 = {1,2};
        int[] arr7 = {-1,2,-3,4,-5,6};
        int[] arr8 = {};

        // System.out.println(largestSumDP(arr));
        // System.out.println(largestSumDP(arr2));
        // System.out.println(largestSumDP(arr3));
        // System.out.println(largestSumDP(arr4));
        // System.out.println(largestSumDP(arr5));
        // System.out.println(largestSumDP(arr6));
        // System.out.println(largestSumDP(arr7));
        // System.out.println(largestSumDP(arr8));
        // System.out.println();
        // System.out.println(largestSumV2(arr));
        // System.out.println(largestSumV2(arr2));
        // System.out.println(largestSumV2(arr3));
        // System.out.println(largestSumV2(arr4));
        // System.out.println(largestSumV2(arr5));
        // System.out.println(largestSumV2(arr6));
        // System.out.println(largestSumV2(arr7));
        // System.out.println(largestSumV2(arr8));
        // System.out.println();
        // System.out.println(largestSumV3(arr));
        // System.out.println(largestSumV3(arr2));
        // System.out.println(largestSumV3(arr3));
        // System.out.println(largestSumV3(arr4));
        // System.out.println(largestSumV3(arr5));
        // System.out.println(largestSumV3(arr6));
        // System.out.println(largestSumV3(arr7));
        // System.out.println(largestSumV3(arr8));
        // System.out.println();
        System.out.println(largestSumV4(arr));
        System.out.println(largestSumV4(arr2));
        System.out.println(largestSumV4(arr3));
        System.out.println(largestSumV4(arr4));
        System.out.println(largestSumV4(arr5));
        System.out.println(largestSumV4(arr6));
        System.out.println(largestSumV4(arr7));
        System.out.println(largestSumV4(arr8));
    }
}
