import java.math.BigInteger; 
import java.util.*;

class Euler25{
	public static int fibonacci(){
		int counter=0;
		BigInteger A  = BigInteger.valueOf(0);
		BigInteger B  = BigInteger.valueOf(1);
		BigInteger C;		
		while(A.toString().length()!=1000){
			C = A.add(B);
			A=B;
			B=C;
			counter+=1;
		}
		return counter+1;
	}

	public static void main(String[] args){
		long startTime=System.nanoTime();
		int S=fibonacci();
		System.out.println(S);
		long endTime=System.nanoTime();
		long elapsedTime=endTime-startTime;
		System.out.println("Time Taken in nanoSecond : "+elapsedTime);
		System.out.println("Time Taken in milliSecond : "+elapsedTime/1000000);
	}
}

//4783
//Time Taken in nanoSecond : 702007600
//Time Taken in milliSecond : 702

