#1부터 100까지 짝수의 합을 구하는 프로그램을 for문으로 작성하시오
n = 0

# for i in range(1, 101):
#     if i % 2 == 0:
#         n += i
# print(n)


for i in range(2, 101, 2):
    n += i
print(n)