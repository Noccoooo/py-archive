from collections import Counter

med = [1, 2, 5, 6, 2, 2, 1]

def find_med(lst):
    index = len(lst) // 2
    return lst[index]

def find_mean(lst):
    mean = 0
    for num in lst:
        mean += num
    return mean // len(lst)

def find_mode(lst):
    c =  Counter(lst)
    return c.most_common(1)

        

print(find_mode(med))