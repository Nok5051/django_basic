# 1
print('\n'.join([''.join(['*' for i in range(i + 1)]) for i in range(5)]))
print()

# 2
print('\n'.join([''.join(['*' for i in range(i)]) for i in range(5, 0, -1)]))
print()

# 3
print('\n'.join([''.join([' ' for i in range(4 - i)] + ['*' for i in range(i + 1)]) for i in range(5)]))
print()

# 4
print('\n'.join([''.join([' ' for i in range(i)] + ['*' for i in range(5 - i)]) for i in range(5)]))
print()

# 5
'''
위와 같은 형식으로
    *
   ***
  *****
 *******
*********
를 출력
'''

