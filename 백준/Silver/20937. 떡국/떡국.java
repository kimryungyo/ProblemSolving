import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {

        int N;
        int[] counts = new int[50001];

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());

        String input = br.readLine();
        String[] numbers = input.split(" ");

        for (String number : numbers) {
            counts[Integer.parseInt(number)] += 1;
        }
        
        int max_count = 0;
        for (int i = 0; i < 50001; i++) {
            if (counts[i] > max_count) {
                max_count = counts[i];
            }
        }

        System.out.println(max_count);
    }
}