import java.util.Scanner;
public class aDifferentProblem {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        while(scan.hasNext()) {
            long nbr1 = scan.nextLong();
            long nbr2 = scan.nextLong();
            System.out.println(Math.abs(nbr1-nbr2));
        }
    }
}