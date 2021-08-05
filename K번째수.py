def solution(array, commands):
    answer = []
    for tools in commands:
        arr = array[tools[0]-1:tools[1]]
        arr.sort()
        answer.append(arr[tools[2]-1])
    return answer


array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
print(solution(array, commands))