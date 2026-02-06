import java.util.Scanner;
public class Tarifa {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int x = scan.nextInt();
        int amount = scan.nextInt();
        int p = 0;
        for(int i = 0; i < amount; i++)
        {
            p += x - scan.nextInt();
        }
        
        System.out.print(p + x);
    }
}
