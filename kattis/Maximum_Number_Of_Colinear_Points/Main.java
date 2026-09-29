import java.util.*;

public class Main {
    record Direction(int x, int y){}
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int amountPoints = input.nextInt();
        List<Map.Entry<Integer, Integer>> points = new ArrayList<>();
        while(amountPoints != 0){
            for(int i = 0; i<amountPoints; i++){
                int x = input.nextInt();
                int y = input.nextInt();
                points.add(Map.entry(x,y));
            }
            int maxAmount = 1;
            for(Map.Entry<Integer, Integer> e: points){
                Map<Direction, Integer> amountOnLine = new HashMap<>();
                for(Map.Entry<Integer, Integer> e2: points){
                    if(!e.equals(e2)){
                        int dx = e2.getKey() - e.getKey();
                        int dy = e2.getValue() - e.getValue();

                        int divisor = gcd(Math.abs(dx), Math.abs(dy));
                        dx /= divisor;
                        dy /= divisor;

                        if (dx < 0 || (dx == 0 && dy <0)){
                            dx = -dx;
                            dy = -dy;
                        }

                        Direction direction = new Direction(dx, dy);
                        amountOnLine.put(direction, amountOnLine.getOrDefault(direction, 0) + 1);

                        }
                    }

                for(int amountFound: amountOnLine.values()){
                    if(amountFound + 1 > maxAmount)
                        maxAmount = amountFound + 1;
                }
            }
            System.out.println(maxAmount);
            amountPoints = input.nextInt();
            points.clear();

        }
    }
    static int gcd(int a, int b) {
        while (b !=0){
            int remainder = a % b;
            a = b;
            b = remainder;
        }
        return a;
    }
}

