#실습3 - 과일채소 프로그램
#과일 채소 카테고리 리스트에 새로운 상품을 등록하는 프로그램
#이미 등록되었는지 확인하고 없으면 리스트에 추가

#과일, 채소 리스트 선언
fruit = ['사과','오렌지','포도','파인애플']
vegetable = ['당근', '호박','양상추','오이']
# 카테고리와 상품명 입력받기
category = input('등록할 카테고리를 입력해주세요. (과일, 채소 ,,등): ')
name = input('등록할 상품명을 입력하세요. : ')

#이미 등록되었는지 확인
if (category == '채소'):
  if name in vegetable:
    print('이미 등록된 채소입니다')
  else:
    vegetable.append(name)
    
elif (category == '과일'):
  if (name in fruit):
    print('이미 등록된 과일입니다')
  else:
    fruit.append(name)
#없는 카테고리 입력시 예외처리
else:
  print('존재하지 않는 카테고리입니다')

print(fruit, vegetable)

