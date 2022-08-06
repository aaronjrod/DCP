import java.util.Random;

public class D14 {
    //Plan: Make a rectangle, make a circle
    //Ratio of points in rect to points in circle is pi
    public static double monteCarloPi(){
        Random rand = new Random();
        double r,x,y;
        int numIter = 10000000;
        int numCir=0;

        for (int i = 0; i < numIter; i++){
            x = rand.nextDouble();
            y = rand.nextDouble();
            r = Math.sqrt(Math.pow(x, 2) + Math.pow(y, 2));
            if (r <= 1)
                numCir++;
        }
        //Three decimal places
        double pi = (double) 4 * numCir / numIter;
        return Math.floor(pi * 1000) / 1000;
    }
    public static void main(String[] args) {
        Random rand = new Random();
        double r,x,y;

        // for (int i = 0; i < 10; i++){
        //     //System.out.println(rand.nextDouble());
        //     x = rand.nextDouble();
        //     y = rand.nextDouble();
        //     r = Math.sqrt(Math.pow(x, 2) + Math.pow(y, 2));
        //     System.out.println(r);
        // }
        for (int i = 0; i < 100; i++)
            System.out.println(monteCarloPi());


    }
}
