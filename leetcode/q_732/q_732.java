import java.util.ArrayList;

public class q_732 {
    public boolean isPrime(int number){

        int tracker = 0;
        for(int i = 1; i < number; i++){
            if (number % i ==0){
                tracker++;
            }
            if(tracker > 1){
                return false;}
        }
        return true;
    }
    
    public int toBinary(int currentNumber){
        int toDouble = 1;
        ArrayList<Integer> allInts = new ArrayList<Integer>();
        allInts.add(toDouble);
        while(toDouble < currentNumber){
            toDouble*=2;
            allInts.add(toDouble);
        } 
        boolean check = allInts.get(allInts.size()-1) > currentNumber;
        if(check){
            allInts.remove(allInts.size()-1);
        }     
        
        StringBuilder thisList = new StringBuilder();
        int currentSum = currentNumber;
        for(int nums = allInts.size()-1; nums >= 0; nums--){       
            if (currentSum >= allInts.get(nums)){
                currentSum-= allInts.get(nums);
                thisList.append("1");}}
        
        int returnValue = Integer.valueOf(thisList.length());
        return returnValue;
    }

    public int countPrimeSetBits(int L, int R) {
        int primeTracker = 0;
        for(int i = L; i <= R; i++){            
            if(this.isPrime(this.toBinary(i))==true){
                
                primeTracker++;
            }

        }
        return primeTracker;
    }

    public static void main(String args[]){
        q_732 intstanceNew = new q_732();
        
        System.out.println(intstanceNew.countPrimeSetBits(567,607));        
    }
}
