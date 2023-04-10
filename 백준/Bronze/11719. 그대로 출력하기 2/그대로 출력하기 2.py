while True:
  try:
    print(input())
  except EOFError:
    break

# 문제 분석
# EOFError : 파일의 끝(End Or File)이 올것을 예상하지 못할때 발생하는 에러.
# 즉 더이상 읽어들일 것이 없을때 발생
# 예외처리는 try/except 사용하기