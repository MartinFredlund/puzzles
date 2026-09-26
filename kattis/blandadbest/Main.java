import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        input.next();
        String meatType = null;
        while (input.hasNext()){
            if(meatType == null)
                meatType = input.next();
            else if (!meatType.equals(input.next())) {
                System.out.println("blandad best");
                return;
            }
        }
        System.out.println(meatType);
    }
}