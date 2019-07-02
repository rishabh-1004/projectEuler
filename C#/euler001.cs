using System;
using System.Collections.Generic;
class euler001 {
  static void Main() {
      int total=0;
      List<int> digits=new List<int>();
      for(int i=1;i<1000;i++){
          if(i%3==0 && i%5==0){
              digits.Add(i);
          }
      }
      foreach(int obj in digits){
          total+=obj;
      }
      
      Console.Write(total);
  }
}