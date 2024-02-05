'''
파일 읽기

readline()
- 한 번에 한 라인만 읽을 수 있다
'''
file = open("C:/upload/test.txt", 'r')
while True:
    read_line = file.readline()
    if not read_line :
        break
    print(read_line)

# file.read() 이거 쓰면 다 읽기는 함