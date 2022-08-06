public class D18 {

    // Brute first
    public static int[] maxArray(int[] arr, int k){
        int len = arr.length;
        int[] localMaxes = new int[len-k+1];
        int curMax = 0;

        for (int i = 0; i < len - k + 1; i++){
            curMax = 0;

            for (int j = i; j < i + k; j++){
                if (arr[j] > curMax) {
                    curMax = arr[j];
                }
            }

            localMaxes[i] = curMax;
        }
        return localMaxes;
    }
    // Conditions: Is the new entry greater than max? If so, is new max
    // Else if the leaving entry is not max, max same
    // New entry less than max and leaving is max: Compare entry to second best
    // Inelegant, what if k is 1, and have to track, might as well sort
    public static int[] maxArray2(int[] arr, int k){
        int len = arr.length;
        int[] localMaxes = new int[len-k+1];
        int curMax = 0;

        for (int i = 0; i < len - k + 1; i++){
            curMax = 0;

            for (int j = i; j < i + k; j++){
                if (arr[j] > curMax) {
                    curMax = arr[j];
                }
            }

            localMaxes[i] = curMax;
        }
        return localMaxes;
    }


    public static void main(String[] args) {
        int[] input = {10, 5, 2, 7, 8, 7};
        int[] arr = maxArray(input,1);

        for (int x : arr)
            System.out.println(x);
    }
}
