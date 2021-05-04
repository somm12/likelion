#실습2 - 유저 db 갱신 프로그램
#유저의 간단한 정보를 딕셔너리에 저장하고 출력하는 프로그램

#dictionary 변수 선언 - {'key' : value}형식
dicUser = {}

#input한 값을 반환하는 함수 userInfo 정의
def userInfo(comment):
  val = input(comment)
  return val

#이름, 나이, 휴대폰 번호 입력
name = userInfo('이름: ')
age = userInfo('나이: ')
phone = userInfo('연락처 : ')

#입력한 값을 dicUser 딕셔너리에 업데이트.
dicUser.update({'name': name})
dicUser.update({'age': age})
dicUser.update({'phone': phone})

print(dicUser)
