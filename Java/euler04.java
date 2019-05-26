import java.util.*;
import java.lang.*;
import java.text.*;


class euler04{
	
	public static boolean checkPalindrome(int n){
		int number=n;
		int reverse_number=0;
		while(n>0){
			int digit = n%10;
			reverse_number=reverse_number*10+digit;
			n=n/10;
		}
		if(number==reverse_number){
			return true;
		}else{
			return false;
		}
	}


	public static void main(String[] args){
		long startTime= System.nanoTime();

		int max=0;

		for(int i=999;i>100;i--){
			for(int j=999;j>100;j--){
				int s=i*j;
				if(checkPalindrome(s)){
					if(s>max)
						max=s;
				}
			}
		}
		System.out.println("Maximum palindrome number : "+max);

		long endTime = System.nanoTime();

		long timeElapsed = endTime - startTime;

		System.out.println("Execution time in nanoseconds: " + timeElapsed);
		System.out.println("Execution time in milliseconds: " + timeElapsed / 1000000);

	}

}

//Maximum palindrome number : 906609
//Execution time in nanoseconds: 126378438
//Execution time in milliseconds: 126