import java.util.ArrayList;
import java.util.*;


class Euler24{

    public static int factorial(int num){
        int res=1;
        if(num <= 1)
            return 1;

        while(num > 1){
            res *= num--;   
        }
        return res;
    }

    public static ArrayList<Integer> addValue(int digit, ArrayList<Integer> al) {
        List<Integer> list = new ArrayList<>(Arrays.asList(0, 1, 2, 3, 4, 5, 6, 7, 8, 9));
        list.removeAll(al);
        al.add(list.get(digit));
        return al;
    }

    public static void main(String args[])
    {
        long startTime=System.nanoTime();
        ArrayList<Integer> al = new ArrayList<Integer>();   
        int index = 999999; 
        int numOfDigit = 10;

        int digit, count=1;
        while( index !=0  )
        {
            digit = ( index / factorial( numOfDigit - count ) );
            al = addValue(digit, al);

            index = ( index % factorial( numOfDigit - count ) );

            if(index == 0)
                break;
            count++;
        }
        int temp =0;
        while( al.size() < numOfDigit )
        {

            if(!al.contains(temp))
                al.add(temp);

        temp++;
        }
        for(int obj:al){
            System.out.print(obj);
        }
        System.out.println();
        long endTime=System.nanoTime();
        long timeElapsed=endTime-startTime;
        System.out.println("Time Elapsed in nanoSecond: "+ timeElapsed);
        System.out.println("Time Elapsed in milliSecond: "+ timeElapsed/1000000);
    }
}

//2783915460
//Time Elapsed in nanoSecond: 2637800
//Time Elapsed in milliSecond: 2