using System;
using System.Collections.Generic;
class euler004 {
    public static int reverse(int number){
        int n=number,reverse=0;
        while(n>0){
            int d=n%10;
            reverse=(reverse*10)+d;
            n=n/10;
        }
        return reverse;
    }
    public static bool isPalindrome(int number){
        if(reverse(number)==number){
            return true;
        }
        else{
            return false;
        }
    }
    public static int checkLargestPalindrome(){
        int s;
        int maximum=0;
        for(int i=999;i>100;i--){
            for(int j=999;j>100;j--){
              s=i*j;
              if(isPalindrome(s) && s>maximum){
                  maximum=s;
              }
            }
        }
        return maximum;
    }
    public static void Main() {
      int maximum=checkLargestPalindrome();
      Console.WriteLine(maximum);
  }
}
