# -*- coding: utf-8 -*-
import os.path
import time


def lensort(strlist):
    sorted_strlist = sorted(strlist, key=lambda length: len(length))
    print(strlist, sorted_strlist)
    return sorted_strlist


def unique(strlist):
    s = set(strlist)
    print(s)
    return list(s)


def my_enumerate(strlist):
    numlist = list(i for i in range(len(strlist)))
    z = zip(numlist, strlist)
    print(z)
    return list(z)


def words_frequency(file_name):
    current_dir = os.getcwd()
    if not os.path.isfile(os.path.join(current_dir, file_name)):
        print("Файл не существует", os.path.join(current_dir, file_name))
        return
    with open(os.path.join(current_dir, file_name), 'r') as f:
        data = f.readlines()
    f_dict = {}
    for d in data:
        for word in d.split():
            if word not in f_dict:
                f_dict[word] = 1
            else:
                f_dict[word] = f_dict[word] + 1
    print(f_dict)
    return f_dict


def time_decorator(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(format(end - start, '.10g'))
        return result
    return wrapper


@time_decorator
def for_list(lst):
    square_list = []
    for i in lst:
        square_list.append(i**2)
    return square_list


@time_decorator
def lc_list(lst):
    return [i**2 for i in lst]


@time_decorator
def map_list(lst):
    return list(map(lambda x: x**2, lst))


if __name__ == "__main__":
    input_arr = ['python', 'perl', 'java', 'c', 'haskell', 'ruby']
    # lensort()
    # unique()
    # my_enumerate()
    words_frequency(".gitignore")
    # lst1 = range(1,9999999  )
    # for_list(lst1)
    # lst2 = range(1,9999999)
    # lc_list(lst2)
    # lst3 = range(1,9999999)
    # map_list(lst3)
