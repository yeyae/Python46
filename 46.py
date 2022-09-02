#파일생성하는 방법
f = open("새파일.txt",'w')
f.close()
    
#만약 새 파일.txt 파일을 C:/doit 디렉터리에 생성하고 싶을 때
f = open("C:/doit/새파일.txt",'w')
f.close()

#파일을 쓰기 모드로 열어 출력값 적기
#writedata.py
f = open("C:/doit/새파일.txt",'w')
for i in range(1,11):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close()

for i in range(1,11):
    data = "%d번째 줄입니다.\n" % i
    print(data)
