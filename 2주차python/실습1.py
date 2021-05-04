#실습1 - 시험점수 자동 채점 프로그램
# 모두 65점이 넘어야 합격
#변수 초기화 - 최소 합격점수, 최대, 최소 점수
cut= 65
maximum = 100
minimum = 0

#과목 점수 입력
num1 = int(input('창사코 점수: '))
num2 = int(input('선형대수 점수: '))
num3 = int(input('컴퓨터 공학: '))

#0-100점 사이 숫자를 입력했는지 확인
if (num1 > maximum or num2> maximum or num3 > maximum):
  print('잘못된 점수가 입력되었습니다.')
elif (num1 < minimum or num2 < minimum or num3 < minimum):
  print('잘못된 점수가 입력되었습니다')

#65점이상시 합격
elif (num1 > 65 and num2 > 65 and num3 >65):
  print('합격입니다!')
else:
  print('불합격입니다')