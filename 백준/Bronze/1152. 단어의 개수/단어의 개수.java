import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args)  throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in)); //입력받기

        //String str = br.readLine(); //입력받은거 str로 저장
        //입력받은 문자열을 아래처럼 그냥 바로 넣어서 쓸 수도 있음
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        //StringTokenizer(String str, String delim); 문자열 분리
        //str을 delim(기준)에 따라 분리함
        System.out.println(st.countTokens()); //위에서 분리한 갯수 카운트
    }
}