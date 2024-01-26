'''
서식 문자
- 반드시 따옴표 안에서 작성한다

%d : 정수(int) 10진수
%o : 8진수
%x : 16진수
%f : 실수
%c : 문자
%s : 문자열
'''

print("%d" %10)
print("%f" %1.22)
print("%f" %3.141592)
print("%.2f" %3.141592)
print("%s" %"문자열")
print("%d %d" %(10,20))
print("%s %s %s" %("문", "자", "열"))

varValue = 500
print("%d" %varValue)
str1 = "Python"
str2 = "Java"
print("%s %s" %(str1, str2))

print("==============================================")

print("%d" %123)
print("%5d" %123)
print("%10d" %123)
print("%30d" %123)