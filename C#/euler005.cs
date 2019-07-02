using System;
using System.Collections.Generic;
class euler005 {
    public static bool checkNumberDivisibility(int obj){
        if(obj%11==0 && obj%12==0 && obj%13==0 && obj%14==0 && obj%15==0 && obj%16==0 &&
        obj%17==0 && obj%18==0 && obj%19==0 && obj%20==0)
            return true;
        return false;
        
    }
    static void Main(string[] args){
        for(int i=10000000;i<50000000000;i+=40){
            if(checkNumberDivisibility(i)){
                Console.WriteLine(i);
                break;
            }    
        }
        
        
    }
  }
