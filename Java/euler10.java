import java.util.*;

class Euler10{
     public static long sieveOfEratosthenes(int n) 
    { 
        boolean prime[] = new boolean[n+1];
        long sum=0; 
        for(int i=0;i<n;i++) 
            prime[i] = true; 
          
        for(int p = 2; p*p <=n; p++) 
        { 
            if(prime[p] == true) 
            { 
                for(int i = p*2; i <= n; i += p) 
                    prime[i] = false; 
            } 
        } 
          
        for(int i = 2; i <= n; i++) 
        { 
            if(prime[i] == true) 
                sum=sum+i; 
        } 
        return sum;
    } 


    public static void main(String[] args){
        long startTime=System.nanoTime();
        long sum=sieveOfEratosthenes(2000001);
        System.out.println(sum);
        long endTime=System.nanoTime();
        long timeElapsed=endTime-startTime;
        System.out.println("Time taken in nanoSeconds: "+timeElapsed);

        System.out.println("Time taken in milliSeconds: "+timeElapsed/1000000);
    }
}

//142913828922
//Time taken in nanoSeconds: 30356000
//Time taken in milliSeconds: 30