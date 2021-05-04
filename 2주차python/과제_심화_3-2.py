#과제(3-2 심화) - 비디오 대여점 프로그램 개발

#변수 선언
movies= {'MOV001': ['인셉션', 2012, '미국'],'MOV002': ['어벤져스4', 2019, '미국'],'MOV003': ['기생충', 2019, '한국']}
directors= {'DIR001': ['MOV001', '크리스토퍼놀란'],'DIR002': ['MOV002', '조루소'],'DIR003': ['MOV002', '앤서니루소'],'DIR004': ['MOV003', '봉준호']}
actors= {'ACT001': ['MOV001', '레오나르도디카프리오', 46],'ACT002': ['MOV002', '로버트다우니주니어', 54],'ACT003': ['MOV002', '스칼렛요한슨', 36],
         'ACT004': ['MOV002', '베네딕트컴버배치', 47], 'ACT005': ['MOV002', '피터파커', 22],'ACT006': ['MOV002', '브루스배너', 51],
         'ACT007': ['MOV002', '토르오딘손', 40],'ACT008': ['MOV002', '제임스로즈', 52],'ACT009': ['MOV002', '비전', 49],'ACT010': ['MOV003', '송강호', 54]}

#영화 데이터 입력함수

def writeMovie():
  info = []
  #자동고유번호 추가하기
  movNum = len(movies)
  movNum = movNum + 1
  
  name = input('영화이름 입력: ')
  info.append(name)
  year = input('개봉년도 입력: ')
  info.append(year)
  country = input('나라 입력: ')
  info.append(country)

  movNum  = "%03d"% movNum
  movNum = str(movNum)
  movies.update({'MOV'+ movNum:info})


def writeDirector():
  #입력하기전 목록조회(고유번호 입력 위함)
  print(movies)
  info = []
  #자동고유번호 추가하기
  directorNum = len(directors)
  directorNum = directorNum + 1
  
  movNum = input('영화 고유번호 입력 (MOV001..): ')
  info.append(movNum)
  directorName = input('감독이름 입력: ')
  info.append(directorName)

  directorNum  = "%03d"% directorNum
  directorNum = str(directorNum)
  directors.update({'DIR'+ directorNum:info})

def writeActor():
  #입력하기전 목록조회(고유번호 입력 위함)
  print(movies)
  info = []
  #자동고유번호 추가하기
  actorNum = len(actors)
  actorNum = actorNum + 1
  
  movNum = input('영화 고유번호 입력 (MOV001..): ')
  info.append(movNum)
  actorName = input('배우이름 입력: ')
  info.append(actorName)
  age = input('배우나이 입력: ')
  info.append(age)

  actorNum  = "%03d"% actorNum
  actorNum = str(actorNum)
  movies.update({'ACT'+ actorNum:info})

#데이터 조회 함수정의
def showData(lookup):
  if (lookup == '영화'):
    print(movies)
  elif (lookup == '감독'):
    print(directors)
  elif (lookup == '배우'):
    print(actors)

#데이터 삭제 함수정의
def deleteDirector(name):
   #반복문에서 딕셔너리 값 삭제 -> size 건들면 오류 생성 -> 새로 다시 딕셔너리에 추가하는 방식
  new = {}
  global directors #전역변수 접근을 위함

  check = []# 없는 데이터를 삭제하려고 할시 종료되는 예외처리
  for key, value in directors.items():
    for values in value:
      check.append(values)
  if name not in check:
    print('해당 데이터는 없습니다')
    return

  for key, value in directors.items():
    info = []
    count = 0
    #value리스트 하나 하나 값을 체크, 모든 값이 삭제하려는 값(개수를 count로 둠)이 아니어야함 => length == count
    for values in value:
      if values != name:
        count += 1
        info.append(values)
    if (count == len(value)):
      new[key] = info
  directors = new
  print(directors)

def deleteActor(name):
   #반복문에서 딕셔너리 값 삭제 -> size 건들면 오류 생성 -> 새로 다시 딕셔너리에 추가하는 방식
  new = {}
  global actors

  check = []# 없는 데이터를 삭제하려고 할시 종료되는 예외처리
  for key, value in actors.items():
    for values in value:
      check.append(values)
  if name not in check:
    print('해당 데이터는 없습니다')
    return


  for key, value in actors.items():
    info = []
    count = 0
    #value리스트 하나 하나 값을 체크, 모든 값이 삭제하려는 값(개수를 count로 둠)이 아니어야함 => length == count
    for values in value:
      if values != name:
        count += 1
        info.append(values)
    if (count == len(value)):
      new[key] = info
  actors = new
  print(actors)

def dataInput():
  #어떤 데이터를 추가하고 싶은지 입력받기
  select = input("영화, 감독, 배우 중 어떤 데이터를 입력하시겠습니까? : ")
  print('\n')
  if (select == '영화'):
    writeMovie()
  elif (select == '감독'):
    writeDirector()
  else:
    writeActor()
def lookupData():
  #조회하고 싶은 데이터 입력받아서 전체 조회
  select = input("영화, 감독, 배우 중 어떤 데이터를 조회하시겠습니까? : ")
  print('\n')
  showData(select)

def deleteData():
  #데이터를 삭제하고 싶은지 입력받기
  select = input("데이터를 삭제하고 싶으신가요? (yes or no) ")
  print('\n')
  if (select == 'yes'):
    which = input("감독과 배우 중 어떤 걸 삭제할까요? ")
    print('\n')
    if (which == '감독'):
      name = input('삭제하고 싶은 감독 이름 데이터를 입력해주세요: ')
      print('\n')
      deleteDirector(name)
    else:
      name = input('삭제하고 싶은 배우 이름 데이터를 입력해주세요: ')
      deleteActor(name)
  else:
    print('종료!')

dataInput()
lookupData()
deleteData()