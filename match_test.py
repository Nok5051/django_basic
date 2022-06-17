# match ~ case
# 3.10 버전부터 사용 가능

a = input("1 ~ 3 사이의 숫자 입력 : ")
# 실행창 넘어가는 단축키 alt + 4

match a:
    case "1":
        print('one')
    case "2":
        print("two")
    case "3":
        print("three")


season = 3
match season:
    case 12 | 1 | 2:
        print("겨울")
    case 3 | 4 | 5:
        print("봄")
    case 6 | 7 | 8:
        print("여름")
    case 9 | 10 | 11:
        print("가을")
    case _:
        print("1 ~ 12 사이의 값을 입력해 주세요.")
