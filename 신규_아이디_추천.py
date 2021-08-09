def solution(new_id):
    new_id = new_id.lower()
    ret = ''
    for i in range(len(new_id)):
        if 48 <= ord(new_id[i]) <= 57 or 97 <= ord(new_id[i]) <=122:
            ret += new_id[i]
        elif ord(new_id[i]) == 45 or ord(new_id[i]) == 95:
            ret += new_id[i]
        elif ord(new_id[i]) == 46 and (ret!='' and ret[-1]!='.') and 0<i<len(new_id)-1:
            ret += '.'

    while ret!='' and ret[-1]=='.':
        ret = ret[:-1]

    if ret == '':
        ret = 'a'

    if len(ret) > 15:
        ret = ret[:15]

        while ret[-1]=='.':
            ret = ret[:-1]

    while len(ret) < 3:
        ret += ret[-1]

    return ret
