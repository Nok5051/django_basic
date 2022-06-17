# fibonacci
# 0 1 1 2 3 5 8 13 21 34 ...

# 입력한 숫자 만큼의 피보나치 수업 갯수 출력
n = int(input('출력할 피보나치 수열의 갯수는 : '))

a, b = 0, 1

i = 0
while i < n:
    print(a, end=' ')
    a, b = b, a + b
    i += 1



