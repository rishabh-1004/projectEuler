using System;
using System.Collections.Generic;
class euler002 {
  static void Main() {
      List<long> even_fibonacci=new List<long>();
      int a=0,b=1,sum=0,total=0;
      for(int i=0;i<100;i++){
          sum=a+b;
          if(sum>4000000)
            break;
            a=b;
            b=sum;
            if (sum%2==0)
                even_fibonacci.Add(sum);
         
      }
      foreach(int obj in even_fibonacci){
          total+=obj;
      }
      Console.WriteLine(total);
  }
}