import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int blocks = input.nextInt();
        int rowLength = 1;
        int height = 0;
        while(true){
            if(blocks >=  rowLength * rowLength){
                blocks -= rowLength * rowLength;
                height++;
                rowLength += 2;
            }else {
                System.out.println(height);
                return;
            }
        }
    }
}