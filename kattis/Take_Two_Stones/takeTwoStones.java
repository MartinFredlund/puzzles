import java.util.Scanner;
public class takeTwoStones {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        double x = scan.nextDouble();
        if(x%2 == 0) {
            System.out.print("Bob");
        }
        else { 
            System.out.print("Alice");
        }
    }
}