import java.util.*;
import java.lang.*;
import java.text.*;

class euler01{
	public static void main(String[] args)
	{

		long startTime = System.nanoTime();

		List<Integer> list = new ArrayList<>();
		int sum=0;
		int i;
		for( i=0;i<1000;i++){
			if(i%3==0 || i%5==0){
				list.add(5);
			}
		}
		for(int obj:list)  
 		   sum+= obj;  
  

        System.out.println(sum); 
        long endTime = System.nanoTime();

		long timeElapsed = endTime - startTime;

		System.out.println("Execution time in nanoseconds: " + timeElapsed);
		System.out.println("Execution time in milliseconds: " + timeElapsed / 1000000);
	}
}

/*
2335
Execution time in nanoseconds: 742727
Execution time in milliseconds: 0
*/