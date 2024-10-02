import java.util.Scanner;
public class NthDigit {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("enter the number");
        int n = sc.nextInt();
        System.out.println("enter the position of bit you want");
        int pos = sc.nextInt();
        int ans = n&(1<<n-1);
        System.out.println("value of bit :"+ans);
    }
}
//this is a program that tells the value of nth bit of a number .