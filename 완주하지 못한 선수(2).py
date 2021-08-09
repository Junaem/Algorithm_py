from collections import Counter

def solution(participant, completion):
    P = dict(Counter(participant))
    C = dict(Counter(completion))

    for key in participant:
        if P.get(key) != C.get(key):
            return key