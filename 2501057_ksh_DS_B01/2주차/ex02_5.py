#1부터 100까지 짝수의 합을 구하는 함수 getTotal()을 만들고 반환 후 결과 출력
def getTotal():
    total = 0
    for i in range(1, 101):    
        if i % 2 == 0:
            total += i
    return total

result = getTotal()
print(result)

