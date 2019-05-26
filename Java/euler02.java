import java.util.*;
import java.lang.*;
import java.text.*;
//import java.util.concurrent.TimeUnit;

class euler02
{
	public static void main(String[] args)
	{
		long startTime = System.nanoTime();

		List<Integer> list=new ArrayList<>();
		int a=0,b=1,c=0,sum=0,counter=0;
		for(int i=0;i<100;i++)
		{
			c=a+b;
			counter+=1;
			if(c>4000000)
				break;
			a=b;
			b=c;
			if(c%2==0)
				list.add(c);
		}

		for(int obj:list)
			sum+=obj;
		System.out.println(sum);

		long endTime = System.nanoTime();

		long timeElapsed = endTime - startTime;

		System.out.println("Execution time in nanoseconds: " + timeElapsed);
		System.out.println("Execution time in milliseconds: " + timeElapsed / 1000000);

	}
}

/*
4613732
Execution time in nanoseconds: 288940
Execution time in milliseconds: 0

*/