#https://school.programmers.co.kr/learn/courses/30/lessons/86051
# 없는 숫자 더하기
def solution(numbers):
    answer = 0
    for i in range(0,10):
        if i not in numbers:
            answer+=i
    return answer