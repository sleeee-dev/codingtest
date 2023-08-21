import java.util.HashMap;
import java.util.Map;

class Solution {
    public String solution(String[] id_pw, String[][] db) {
        Map<String, String> dbMap = new HashMap<String, String>();

        for (String[] strings : db) {
            dbMap.put(strings[0], strings[1]);
        }//put으로 넣어서 db 갯수만큼 들어감

        //아이디,비밀번호 일치하는지 equals로 확인
        if (dbMap.containsKey(id_pw[0])) {
            if (dbMap.get(id_pw[0]).equals(id_pw[1])) {
                return "login";
            } else {
                return "wrong pw";
            }
        } else {
            return "fail";
        }
    }
}