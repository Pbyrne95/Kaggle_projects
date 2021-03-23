import java.util.List;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.*;

public class q_90 {
    public Set<Integer> subWithDub(List<Integer> nums){
        int outputListSize = 0;
        Set<Integer> outputList = new HashSet<Integer>();
        List<Integer> holder = new ArrayList<Integer>();
        
        for(Integer i = 0; i < nums.size(); i ++){
            
            for( Integer j = nums.size(); j > i  ; j--)
            {
                holder = nums.subList(0,j);
                // System.out.println(holder + " " + outputListSize);  
                outputList.addAll(holder);
                
                
                outputListSize++;
            }
        
        }
        return outputList;
    }
    static void printSubArrays(int []arr, int start, int end)
    {     
    // Stop if we have reached the end of the array     
        if (end == arr.length) 
            return;
      
    // Increment the end point and start from 0 
        else if (start > end) 
            printSubArrays(arr, 0, end + 1);
          
    // Print the subarray and increment the starting point 
        else
        {
            System.out.print("[");
            for (int i = start; i < end; i++){
                System.out.print(arr[i]+", ");
            }
            
            System.out.println(arr[end]+"]");
            printSubArrays(arr, start + 1, end);
        }
        
        return;
    }
    List<List<Integer>> res = new ArrayList<>();
    public List<List<Integer>> subsetsWithDupOne(int[] nums) {
        if(nums==null || nums.length==0) return res;
        List<Integer> sub =  new ArrayList<>();
        getAllPerm(nums,0, sub);
        
        return res;
    }
    
    private void getAllPerm(int[] nums, int index, List<Integer> sub){
        if(index < nums.length){
            getAllPerm(nums, index+1, sub);
            List<Integer> temp = new ArrayList<>();
            temp.addAll(sub);
            temp.add(nums[index]);
            getAllPerm(nums, index+1, temp);
        }else if(index== nums.length){
            Collections.sort(sub);
            if(!res.contains(sub)){
                res.add(sub);
            }
        }
    }

    public static void main(String args[]){
        q_90 test = new q_90();
        List<Integer> tester = new ArrayList<Integer>();
        tester.add(1);
        tester.add(2);
        tester.add(3);

        System.out.println(test.subWithDub(tester));

        int [] arr = {1, 2, 2};
        System.out.println(test.subsetsWithDupOne(arr));
    }
}
