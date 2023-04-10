import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args)  throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int a = Integer.parseInt(st.nextToken());
        st = new StringTokenizer(br.readLine()); //new line 입력을 위해 한번 더 선언
        int b = Integer.parseInt(st.nextToken());
        if(0<a && b<10) {
            System.out.println(a + b);
        }
    }
}