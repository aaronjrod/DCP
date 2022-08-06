public class D16 {

    private static class CyclicArray{
        int endPoint;
        int N;
        int[] orderIDs;

        public CyclicArray(int N){
            this.N = N;
            orderIDs = new int[N];
            endPoint=0;
        }

        public void record(int order_id){
            if (endPoint == N)
                endPoint = 0;
            orderIDs[endPoint] = order_id;
            endPoint++;
        }

        public int get_last(int i){
            if (endPoint - i < 0)
                return orderIDs[N + endPoint - i];
            return orderIDs[endPoint - i];
        }

    }

    public static void main(String[] args) {
        int N = 10;
        CyclicArray orderList = new CyclicArray(N);
        for (int i = 0; i < N+2; i++)
            orderList.record(i);
        for (int i = 1; i <= N; i++)
            System.out.println(orderList.get_last(i));

    }
}
