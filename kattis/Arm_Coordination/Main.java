import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int x = input.nextInt();
        int y = input.nextInt();
        int radius = input.nextInt();

        int left = x - radius;
        int right = x + radius;
        int top = y + radius;
        int bottom = y - radius;

        System.out.println(right + " " + top);
        System.out.println(right + " " + bottom);
        System.out.println(left + " " + bottom);
        System.out.println(left + " " + top);
    }
}
