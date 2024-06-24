def solution(a):
    lengthOfA = len(a)

    if lengthOfA == 1:
        return 1
    if lengthOfA == 2:
        return 2

    answer = 2

    leftMinNum = [0] * lengthOfA
    rightMinNum = [0] * lengthOfA

    leftMinNum[1] = a[0]
    for i in range(2, lengthOfA, 1):
        if a[i-1] < leftMinNum[i-1]:
            leftMinNum[i] = a[i-1]
        else:
            leftMinNum[i] = leftMinNum[i-1]

    rightMinNum[lengthOfA-2] = a[lengthOfA-1]
    for i in range(lengthOfA-3, 0, -1):
        if a[i+1] < rightMinNum[i+1]:
            rightMinNum[i] = a[i+1]
        else:
            rightMinNum[i] = rightMinNum[i+1]

    for i in range(1,lengthOfA-1):
        if leftMinNum[i] > a[i] or rightMinNum[i] > a[i]:
            answer += 1;

    return answer