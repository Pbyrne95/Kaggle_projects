public class q_191 {


    public int hammingWeight(String n) {

        int byteCount = 0;
        for(int i = 0; i <= n.length()-1; i++){
            if(n.charAt(i) != '0'){
                byteCount++;
            }
            
        }
        return byteCount;
    }

    public String Stringify(byte n){
        return "str";
    } 
    public static void main(String args[]){
        q_191 placeHolder = new q_191();

        String holdThis = "00000000000000000000000000001011";

        System.out.println(placeHolder.hammingWeight(holdThis));
    }
}
