# for문을 이용해서 l변수에 저장된 1 ~ 5까지 출력하기
l=[1,2,3,4,5]
for value in l :
    print(value)
else:
    print('for문 종료')

print("---------------")

l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for value in l:
    print(f"2 x {value} = {2*value}")
else:
    print('for문 종료')
print("-----------------")
# + 연산자 (리스트 결합)
# + 연산자를 이용해서 리스트끼로 더할 수 있다.
# 형식 : 
# 리스트1 + 리스트2
# [1,2,3,4,5] + [10,20,30,40,50]
# [1, 2, 3, 4, 5, 10, 20, 30, 40, 50]
# 임시적으로 + 한 것이고
# 영구적으로 + 하려면 변수에 저장해야 한다.
l = [1,2,3,4,5]
print(l + [10, 20, 30, 40, 50])  # 임시적으로 + 한 것
print(l)  # [1, 2, 3, 4, 5]
l += [10, 20, 30, 40, 50]  # 영구적으로 + 한 것, l = l + [10, 20, 30, 40, 50]
print(l)  # [1, 2, 3, 4, 5, 10, 20, 30, 40, 50]
# * 연산자 (리스트 반복)
# * 연산자를 이용해서 리스트를 반복한다.
# 형식 : 리스트변수명 * 정수값
# [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
# 임시적으로 * 한 것이고
# 영구적으로 * 할려면 변수에 저장해야 한다.
l = [1,2,3,4,5]
print(l * 3)  # 임시적 [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
print(l)  # [1, 2, 3, 4, 5]
l *= 3    # 영구적 l = l * 3
print(l)  # [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]

# += 연산자 (리스트 확장)
# += 연산자를 이용해서 리스트를 확장한다.
# 형식 : 리스트변수명 += 리스트
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list1 += list2
print(list1)  # [1, 2, 3, 4, 5, 6]

# *= 연산자 (리스트 반복 및 할당)
# *= 연산자를 이용해서 리스트를 반복하고 할당한다
list1 = [1, 2, 3]
list1 *= 3
print(list1)  # [1, 2, 3, 1, 2, 3, 1, 2, 3]


# 리스트는 +, * 연산은 가능하지만 -, / 연산은 불가능하다. 
# print(l - [1,2,3])
# print(l / [1,2,3])

# 인덱스 값 변경
# 형식1: 변수명[인덱스번호] = 값
# 형식2: 변수명[인덱스번호] = 변수
# 형식3: 변수명[인덱스번호] = 함수
# 형식4: 변수명[인덱스번호] = 수식
print("--------------")
l = [1,2,3,4,5]
print(l)  # [1, 2, 3, 4, 5]
l[0] = 10
l[4] = 50
print(l)  # [10, 2, 3, 4, 50]
l[1] = 10
print(l)  # [10, 10, 3, 4, 50]