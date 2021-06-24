from itertools import permutations

A = (1, 2, 4, 4)

def solution(A):
    perm = permutations(A)
    valid_times = 0
    for item in set(perm):

        hour1 = item[0]
        hour2 = item[1]
        minute1 = item[2]
        #minute2 = item[3]

        if (hour1 <= 1) and (minute1 <= 5):
            valid_times += 1
            print(item)
        if (hour1 == 2) and (hour2 <= 3) and (minute1 <= 5):
            valid_times += 1
            print(item)
    return valid_times

