#1부터 100까지 짝수의 합을 구하는 프로그램을 while문으로 작성하시오
total = 0
i = 1
while i <= 100:
    if i % 2 == 0:
        total += i
    i += 1
print(total)

