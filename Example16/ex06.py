'''
파일 삭제
'''
import os

file_path = "C:/upload/test.txt"

try:
    os.remove(file_path)
except:
    print("파일이 존재하지 않습니다")