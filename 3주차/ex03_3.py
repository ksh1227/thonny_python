import random

#전역변수
ttL = []
lt = []
pN = 0
count = 0

#메인 코드 부분
print("로또 번호 생성")
count =int(input('몇번을 뽑을까?'))

for _ in range(count):
    lt = []
    while True:
        pN = random.randint(1, 45)
        if pN not in lt:
            lt.append(pN)
        if len(lt) >= 6:
            break
    ttL.append(lt)
    
for lt in ttL:
    lt.sort()
    print('자동번호', end=' ')
    for i in range(0,6):
        print("%2d"%lt[i],end=' ')
    print()