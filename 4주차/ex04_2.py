katok = []


def add_data(friend):  # 빈 리스트에 데이터 추가
    katok.append(None)
    klen = len(katok)
    katok[klen - 1] = friend


def insert_data(ps, friend):  # 중간에 다른 데이터 삽입
    if ps < 0 or ps > len(katok):
        print("데이터 삽입 범위를 벗어났습니다.")
        return

    katok.append(None)
    klen = len(katok)

    for i in range(klen - 1, ps, -1):
        katok[i] = katok[i - 1]
        katok[i - 1] = None

    katok[ps] = friend


def del_data(ps):  # 데이터 삭제
    if ps < 0 or ps >= len(katok):
        print("데이터 삭제 범위를 벗어났습니다.")
        return

    klen = len(katok)
    katok[ps] = None

    for i in range(ps + 1, klen):
        katok[i - 1] = katok[i]
        katok[i] = None

    del katok[klen - 1]


# 전역변수 선언
katok = []
select = -1

# 메인코드
if __name__ == "__main__":
    while select != 4:
        select = int(input("선택하시오(1: 추가, 2:삽입, 3:삭제, 4:종료)-->"))

        if select == 1:
            data = input("추가할데이터 -->")
            add_data(data)
            print(katok)
        elif select == 2:
            pos = int(input("삽입할위치 -->"))
            data = input("추가할데이터-->")
            insert_data(pos, data)
            print(katok)
        elif select == 3:
            pos = int(input("삭제할위치 -->"))
            del_data(pos)
            print(katok)
        elif select == 4:
            print(katok)
        else:
            print("1~4중 하나를 입력하시오")
            continue
