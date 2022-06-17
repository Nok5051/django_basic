def coffee(quantity, price):
    change = price - (200 * quantity)
    if change >= 0:
        prn(quantity, change)
    else:
        prn()

def prn(quantity=0, change=0):
    if quantity == 0 & change == 0:
        print("돈이 부족합니다...")
    else:
        print(f"커피 {quantity} 잔이 나왔습니다. \n잔돈 {change} 원이 나왔습니다.")

def start():
    q = input("커피 몇 잔이 필요하신가요 ? ")
    p = input("돈을 넣어 주세요 (1잔당 200원)")
    coffee(int(q), int(p))


# __name__ : 해당 파일이 실행 됐을때 이름 저장
# 외부에서 import 해서 실행되는 경우 : 파일 이름
# 파일이 직접 실행되는 경우 : "__main__"

if __name__ == '__main__':
    # 프로그램의 주 진입점
    start()

