public class D12 {

    //1: 1: 1
    //2: 2: 1,1;2
    //3: 3: 1,1,1;1,2;2,1
    //4: 5: 1,1,1,1; 1,1,2; 1,2,1; 2,1,1; 2,2
    //5: 8: 1,1,1,1,1; 2,2,1; 2,1,2; 1,2,2; 1,1,1,2; 1,1,2,1; 1,2,1,1; 2,1,1,1;
    public static int climbStairs2(int n){
        int total1 = 1;
        int total2 = 1;
        int temp = 0;
        for (int i = 1; i < n; i++){
            temp = total1;
            total1 = total1 + total2;
            total2 = temp;
        }
        return total1;
    }

    public static int climbStairs(int n){
        if (n==0 || n == 1) return 1;
        return climbStairs(n-2) + climbStairs(n-1);
    }

    public static int climbStairs(int n, int[] X){
        if (n==0 || n == 1) return 1;
        else if (n<0) return 0;

        int sum = 0;
        for (int num : X){
            sum += climbStairs(n-num,X);
        }

        return sum;
    }

    public static int climbStairs2(int n, int[] X){
        int total1 = 1;
        int total2 = 1;
        int temp = 0;
        
        if (n==0 || n == 1) return 1;
        else if (n<0) return 0;

        int sum = 0;
        for (int num : X){
            sum += climbStairs(n-num,X);
        }

        return sum;
    }

    public static void main(String[] args) {
        //1: 1: 1
        //2: 1: 1,1
        //3: 2: 1,1,1;3
        //4: 3: 1,1,1,1; 1,3; 3,1
        //5: 5: 1,1,1,1,1; 1,1,3; 1,3,1; 3,1,1; 5
        int[] x = {1,3,5};
        for (int i = 1; i < 8; i++) {
            //System.out.println(i+": " +climbStairs2(i));
            System.out.println(i+": " +climbStairs(i,x));
        }

        
        


    }
}
