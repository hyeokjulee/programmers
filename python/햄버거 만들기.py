def solution(ingredient):
    answer = 0

    ingredientStr = ''.join(list(map(str, ingredient)))

    idx = ingredientStr.find("1231")
    while idx < len(ingredientStr):
        if ingredientStr[idx:idx+4] == "1231":
            answer += 1
            ingredientStr = ingredientStr[:idx] + ingredientStr[idx+4:]
            idx -= 2
        else:
            idx += 1

    return answer