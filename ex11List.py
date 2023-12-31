# 메서드(메소드, method)란 객체에 들어있는 함수를 의미한다.

# 함수 vs 메소드
# 함수 형식 : 함수명()
# 메소드 형식 : 객체변수.메소드명()

# 메소드란 객체에 들어있는 함수를 의미한다.
#
# 함수 vs 메소드
# 함수 형식 : 함수명()
# 메소드 형식 : 객체변수.메소드명()
#
# 데이터를 추가하는 형식 : 리스트변수명.append(값)
# 데이터를 추가하는 형식 : 리스트변수명.append(변수명) / 맨 끝에 붙음
# 데이터를 삽입하는 형식 : 리스트변수명.insert(인덱스, 값) / 중간에 값 들어떄
# 데이터를 삭제하는 형식 : 리스트변수명.pop(), 리스트변수명.remove()
# 데이터를 수정하는 형식 : 리스트변수명[인덱스] = 값
# 데이터를 수정하는 형식 : 리스트변수명[인덱스] = 변수명

a= [] #뒤쪽에서 무언가를 추가하려는 작업 시 빈 리스트 삽입!!
a.append(1)
a.append(2)
a.append(3)
a.append(4)
a.append(5)
print(a)

print("----------")

a[1]=20
print(a)
a[4] = a[2]
print(a)
print("-----------")

# 리스트에 자료 삭제하기
# pop() : 끝에 있는 자료를 삭제한다.
# pop(인덱스) : 인덱스에 있는 자료를 삭제한다.
# remove(데이터) : 데이터를 지정해서 삭제한다.
# clear(): 데이터를 전체 삭제한다.

a.pop()
a.pop(1) #해당 인덱스 번호에 있는 값이 날아감
a.remove(1) # 데이터가 날아감 즉,1이 없어짐
#a.clear()
print(a)
print("프로그램 종료")


