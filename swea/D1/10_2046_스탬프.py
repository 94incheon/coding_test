"""
주어진 숫자만큼 # 을 출력해보세요.
주어질 숫자는 100,000 이하다.

[입력]
3

[출력]
###
"""
T = int(input())

if 0 < T <= 100000:
    for i in range(T):
        print('#'*i, end='')
else:
    print('100,000 이하의 자연수를 입력해주세요.')

