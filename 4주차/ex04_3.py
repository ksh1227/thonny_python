katok = []


def add_data(friend):  # 빈 리스트에 데이터 추가
    katok.append(None)
    klen = len(katok)
    katok[klen - 1] = friend


# 친구 자동 삽입
def find_and_insert_data(friend, k_count):
    findPos = -1
    for i in range(len(katok)):
        pair = katok[i]
        if k_count >= pair[1]:
            findPos = i
            break
        if findPos == -1:
            findPos = len(katok)  # 마지막자리에 추가


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
katok = [("다현", 200), ("정연", 150), ("쯔위", 90), ("사나", 30), ("지효", 15)]

# 메인코드
if __name__ == "__main__":
    while True:
        data = input("추가할 친구 -->")
        count = int(input("카톡 횟수 -->"))
        find_and_insert_data(data, count)
        print(katok)
