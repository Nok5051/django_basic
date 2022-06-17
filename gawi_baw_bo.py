from random import randint

class GwaiBawiBoException(Exception):
    def __init__(self):
        pass

def game_processs(player_num):
    '''
    <player - computer>
    player              가위1    바위2      보3
    computer     가위1    0        1(승)    2(패)
                 바위2    -1(패)   0        1(승)
                 보3     -2(승)   -1(패)    0
    '''
    computer_num = randint(1, 3)
    prn = {1: '기위', 2: '바위', 3: '보'}
    print(f'player:{prn[player_num]} vs computer:{prn[computer_num]}')

    if (player_num - computer_num) in [1, -2]:
        print('당신이 이겼습니다!')
    elif player_num == computer_num:
        print('비겼습니다.')
    else:
        print('컴퓨터가 이겼습니다!')


def play():
    while True:
        try:
            player_num = int(input('가위:1 / 바위:2 / 보:3 / 게임종료:4\n숫자를 입력하세요:'))
            if player_num not in [1, 2, 3, 4]:
                raise GwaiBawiBoException()
            if player_num == 4:
                print('재밌으였나요?')
                break


        except ValueError:
            print('숫자만 입력해 주세요...')
        except GwaiBawiBoException:
            print('1, 2, 3, 4 중에 하나만 입력해 주세요...')
        except:
            print('관리자에게 문의해 주세요...')
            break
        else:
            game_processs(player_num)

    print('다음에 도 놀러오세요~')

if __name__ == '__main__':
    play()
