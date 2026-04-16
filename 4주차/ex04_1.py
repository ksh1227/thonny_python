katok = []


def add_data(friend):  # 빈 리스트에 데이터 추가
    katok.append(None)
    klen = len(katok)
    katok[klen - 1] = friend


add_data("다현")
add_data("정연")
add_data("쯔위")
add_data("사나")
add_data("지효")

print(katok)


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


insert_data(2, "솔라")
print(katok)
insert_data(6, "문별")
print(katok)


def del_data(ps):
    if ps < 0 or ps >= len(katok):
        print("데이터 삭제 범위를 벗어났습니다.")
        return

    klen = len(katok)
    katok[ps] = None

    for i in range(ps + 1, klen):
        katok[i - 1] = katok[i]
        katok[i] = None

    del katok[klen - 1]


del_data(1)
print(katok)
del_data(3)
print(katok)
