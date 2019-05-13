import java.util.*;
import java.math.*;
import java.text.*;

class euler06{
	public static int sum_of_squares(int n){
		int sum_=0;
		for (int i=1;i<=n;i++){
			int square=(int)Math.pow(i,2);
			sum_+=square;
		}
		return sum_ ;
	}

	public static int sqaure_of_sums(int n){
		int sum_=0;
		for(int i=1;i<=n;i++){
			sum_+=i;
		}
		int square=(int)Math.pow(sum_,2);
		return square;
	}

	public static void main(String[] args) {
		long startTime=System.nanoTime();
		int number=100;
		int difference=sqaure_of_sums(number)-sum_of_squares(number);
		System.out.println(difference);
		long endTime=System.nanoTime();
		long timeTaken=endTime-startTime;
		System.out.println("Total time taken in nano seconds : "+ timeTaken);
		System.out.println("Total time taken in mili seconds : "+ timeTaken/1_000_000);
	}
}

//25164150
//Total time taken in nano seconds : 1751374
//Total time taken in mili seconds : 1