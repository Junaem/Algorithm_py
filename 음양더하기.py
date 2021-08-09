def solution(absolutes, signs):
    li = []
    for i in range(len(absolutes)):
        if signs[i]:
            li += [absolutes[i]]
        else :
            li += [-absolutes[i]]
    return sum(li)