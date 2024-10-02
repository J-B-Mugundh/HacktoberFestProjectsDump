
public class fibonaccirecursion {
    public int fibo(int n) {
       if(n == 0 || n==1){
           return n;
       }
       return fibo(n-1)+fibo(n-2);
       //much easier code compared to the normal way of doing things
        //thanks to recursion
    }
}
