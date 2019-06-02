import java.util.*;

public class euler26{
	public static void main(String[] args){
		long startTime=System.nanoTime();
		int sequence_Length=0,number=0;
		for(int i=1000;i>1;i--){
			if(sequence_Length>=i)
				break;
			int[] foundRemainders=new int[i];
			int value=1,position=0;
			while(foundRemainders[value]==0 && value!=0){
				foundRemainders[value]=position;
				value*=10;
				value%=i;
				position+=1;
			}
			if(position-foundRemainders[value]>sequence_Length){
				number=i;
				sequence_Length=position-foundRemainders[value];
			}
		}
		System.out.println(number);
		long endTime=System.nanoTime();
		long timeElapsed=endTime-startTime;
		System.out.println("Time Taken in nanoSecond: "+ timeElapsed);
		System.out.println("Time Taken in milliSecond: "+ timeElapsed/1000000);
	}
}

//983
//Time Taken in nanoSecond: 1332000
//Time Taken in milliSecond: 1