import java.util.*;
import java.lang.*;
import java.text.*;

class Main{
	
	public static boolean isPrime(long num){
        if(num==1)
            return false;
        if(num==4)
            return false;
        for (long i=2;i< num/2;i++ ){
            if(num%i==0)
                return false;
        }

        return true;
    }

	public static void main(String[] args){
		
		long startTime = System.nanoTime();

		for (long i=2;i<=500000000;i++){
            if( isPrime(i) ){
                counter++;
                if(counter==10001){
                    System.out.println("6th Prime Number is : "+i);
                    break;
                }
            }
        }

        long endTime = System.nanoTime();

		long timeElapsed = endTime - startTime;

		System.out.println("Execution time in nanoseconds: " + timeElapsed);
		System.out.println("Execution time in milliseconds: " + timeElapsed / 1000000);

	}
}