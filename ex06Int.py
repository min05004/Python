#16진수 표현  (접두사 0x or 0X) 0 ~ 9 a b c d e f 10
 # . e.g.) binaryData = 0b1010, octalData = 0o12, hexaData = 0x1a
i = 10
j = 20

#변수 i에 10 /j에 20

print(i,j)
print('%d %d' %(i,j))
print('{} {}'.format(i,j))


#16진수  // 계산기 활용(프로그래머 모드)
a = 0x7 
b = 0xf
c = 0x10

print(a,b,c)


#8진수
d= 0x7
f= 0x10

print(d,f)
print(0X10) #10진수 16


# 실수를 변수에 저장하는 형식
# 변수명 = 실수

i = 1.5  # i 변수에 1.5를 저장한다.
j = 2.3  # j 변수에 2.3을 저장한다.
k = 3.141592  # k 변수에 3.141592를 저장한다.

# 변수 출력 형식
print(i, j, k)  # 1.5 2.3 3.141592
print('%d %d %d' %(i,j,k))  # 1 2 3  %d : 정수로 출력하라고 명령

# % 출력 형식
# 실수를 출력하는 서식 문자열(문자열 포맷팅) %f를 사용한다.
# % 출력 형식으로 출력하면 소수점 여섯째 자리까지 출력된다.
# 소수점 자리수 제어하는 방법
# 형식 : %.자릿수f
print('%f %f %f' %(i, j, k))  # 1.500000 2.300000 3.141592
print("%.2f %.3f %.4f" %(i, j, k))  # 1.50 2.300 3.1416 

# format() 메소드 출력 형식
# format() 메소드를 이용하면 원래값 그대로 출력된다.
# 소수점 자릿수 제어하는 방법
# 형식 : {인덱스번호:.자릿수f}
# 인덱스 번호가 생략되면 인덱스 번호 순서대로 출력된다.  0부터 시작*

print("{} {} {}".format(i,j,k))  # 1.5 2.3 3.141592
print('{0} {1} {2}'.format(i,j,k))  # 1.5 2.3 3.141592
print('{1} {2} {0}'.format(i,j,k))  # 2.3 3.141592 1.5  / 해당 인덱스값에 숫자가 들어감.
print("{:.2f} {:.3f} {:.2f}".format(i,j,k))  # 1.50 2.300 3.14


# 소수점 전체 자릿수 제어하는 방법
# 형식 : {인덱스번호:전체자릿수.자릿수f}
# 정렬 방법
# 형식 : {인덱스번호:정렬방식|전체자릿수.자릿수f}
# < : 왼쪽 정렬
# >, 생략 : 오른쪽 정렬 (기본값)
# ^ : 가운데 정렬
print('|{}|{}|{}|'.format(i,j,k))  # |1.5|2.3|3.141592|
print('|{:5}|{:5}|{:10}|'.format(i,j,k))  # |  1.5|  2.3|  3.141592|
print('|{:<5}|{:5}|{:^10.4f}|'.format(i,j,k))  # |1.5  |  2.3|  3.1416  |

# * | 구분하려고 작성 구분자.

# f-string 출력 형식
# f"{변수명}"
# f'{변수명}'
# 소수점 자릿수 제어하는 방법
# 형식 : f'{변수명:.자릿수f}'
# 소수점 전체 자릿수 제어하는 방법
# 형식 : f'{변수명:전체자릿수.자릿수f}'
# 정렬 방법
# 형식 : f'{변수명:정렬방식|전체자릿수.소수점자릿수f}'
# < : 왼쪽 정렬
# >, 생략 : 오른쪽 정렬 (기본값)
# ^ : 가운데 정렬
print(f'{i} {j} {k}')  # 1.5 2.3 3.141592
print(f'{i:.2f} {j:.3f} {k:.2f}')  # 1.50 2.300 3.14
print(f'|{i:<5}|{j:5}|{k:^10.4f}|')  # |1.5  |  2.3|  3.1416  |


