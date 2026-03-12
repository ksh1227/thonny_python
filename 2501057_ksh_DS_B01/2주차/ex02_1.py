a = int(input("a값을 입력하시오 "))
b = int(input("b값을 입력하시오 "))

print("a변수의 값은 %d입니다" %a)
print(f"a변수의 값은 {a}입니다")
print("a변수의 값은", a,"입니다")

print(f"{a} + {b} = {a+b}")
print("%d + %d = %d" %(a, b, a+b))
print(a, "+", b, "=", a+b)