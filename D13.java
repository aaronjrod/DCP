public class D13 {

    private static boolean verify(String str, int k){
        boolean[] bucket = new boolean[26];
        int val = 0;
        for (int i = 0; i < str.length(); i++){
            val = str.charAt(i)-97;
            if (!bucket[val]){
                bucket[val] = true;
                k--;
            }
            if (k<0) return false;
        }
        return (k>=0);
    }

    public static int longestSubstring(String s, int k){
        int max = 0;
        int subLen = 0;
        int start = 0;

        String substr = "";
        int len = s.length();
        for (int i = 0; i <= len; i++){
            substr = s.substring(start, i);
            subLen = substr.length();

            if (verify(substr,k)){
                if (subLen > max)
                    max = subLen;
            }
            else{
                while(!verify(substr,k)){
                    start++;
                    substr = s.substring(start, i);
                }
            }
        }
        return max;
    }

    public static int longestSubstring2(String s, int k){
        int max = 0;
        int subLen = 0;
        int start = 0;

        String substr = "";
        int len = s.length();
        for (int i = 0; i <= len; i++){
            substr = s.substring(start, i);

            while(!verify(substr,k)){
                start++;
                substr = s.substring(start, i);
            }

            subLen = substr.length();
            if (subLen > max)
                max = subLen;

        }
        return max;
    }

    public static void main(String[] args) {
        // System.out.println(verify("hi", 1));
        // System.out.println(verify("hi", 2));
        // System.out.println(verify("hi", 3));
        // System.out.println(verify("abbbbbb", 2));
        // System.out.println(verify("abbbbbcb", 2));
        // System.out.println(verify("abbbbbz", 3));
        // System.out.println(verify("", 0));

        System.out.println(longestSubstring2("abba", 2));
        System.out.println(longestSubstring2("abcba", 2));
        System.out.println(longestSubstring2("abccba", 1));

        System.out.println(longestSubstring2("", 1));


    }
}
