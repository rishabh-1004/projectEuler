import java.util.*;

class Euler09{
	
	public static long pythagorean_Triplets(int limit){
		int c=0,m = 2;
		int a=0,b=0,d=0;
    	while(c<limit){
    		for(int n=1;n<m;n++){
    			a = m * m - n * n; 
	            b = 2 * m * n ;
	            c = m * m + n * n; 
    			if (a+b+c==1000)
        			return (a*b*c);
    		}
    		if (c > limit) 
                break;
            
            m=m+1;
    	}
    	return 0;
	}
	public static void main(String[] args){
		long startTime= System.nanoTime();
		long i=pythagorean_Triplets(1000);
		System.out.println(i);
		long endTime=System.nanoTime();
		long timeElapsed=endTime-startTime;
		System.out.println("The time taken in nanoSeconds: "+ timeElapsed);

		System.out.println("The time taken in milliSeconds: "+ timeElapsed/1000000);
		
		
	}
}

//31875000
//The time taken in nanoSeconds: 557800
//The time taken in milliSeconds: 0