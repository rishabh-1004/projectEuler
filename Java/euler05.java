import java.util.*;
import java.math.*;
import java.text.*;

class euler05{
	public static boolean checkDivisibility(int number){
		for(int i=1;i<20;i++){
			if(number%i==0)
				continue;
			else
				return false;
		}
		return true;
	}

	public static void main(String[] args){
		long startTime=System.nanoTime();

		int n=20;
		while(true){
			if(checkDivisibility(n)){
				System.out.println(n);
				break;
				}
			n+=20;
			}

		long endTime=System.nanoTime();
		long timeTaken=endTime-startTime;
		System.out.println("Time Taken in nano second: "+ timeTaken);
		System.out.println("Time Taken in mili second: "+ timeTaken/1_000_000);
			
	}
}


//232792560
//Time Taken in nano second: 47512455
//Time Taken in mili second: 47