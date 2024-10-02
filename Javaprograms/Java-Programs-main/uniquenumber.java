import java.util.Scanner;
public class uniquenumber {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("enter the length of the array");
        int n = sc.nextInt();
        int[] arr;
        arr = new int[n];
        for(int i=0;i<arr.length;i++){
            System.out.println("enter the value of the element ");
            arr[i]=sc.nextInt();
        }
        int uniq =0;
        for(int j=0;j<arr.length;j++){
            uniq = uniq^arr[j];
        }
        System.out.println("the unique element is "+uniq);
    }
}
