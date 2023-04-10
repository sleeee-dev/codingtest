import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        if (n >= 1 && n <= 4000) {
            if ((n % 4) == 0 && (n % 100) != 0 || (n % 400) == 0) {
                System.out.println("1");
            } else {
                System.out.println("0");
            }
        }
    }
}