def solution(numbers):
    return str(int(''.join(sorted([str(number) for number in numbers], reverse=True, key=lambda x:x*3))))