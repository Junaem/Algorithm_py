def solution(answers):
    answer = []
    aPoint = 0
    bPoint = 0
    cPoint = 0
    def ansA(num):
        a_ans = num % 5 +1
        if a_ans == answers[num]:
            return 1
        else:
            return 0

    b_cases = [1, 3, 4, 5]
    def ansB(num):
        b_ans = 2
        if num%2 :
            b_ans = b_cases[(num // 2) % 4]
        if b_ans == answers[num]:
            return 1
        else:
            return 0
    
    c_cases = [3, 1, 2, 4, 5]
    def ansC(num):
        c_ans = c_cases[(num//2) % 5]
        if c_ans == answers[num]:
            return 1
        else:
            return 0

    for i in range(len(answers)):
        aPoint += ansA(i)
        bPoint += ansB(i)
        cPoint += ansC(i)
    
    max_pnt = max([aPoint, bPoint, cPoint])
    if aPoint == max_pnt:
        answer.append(1)
    if bPoint == max_pnt:
        answer.append(2)
    if cPoint == max_pnt:
        answer.append(3)

    return answer

a = [1]
a.append(3)
print(a)