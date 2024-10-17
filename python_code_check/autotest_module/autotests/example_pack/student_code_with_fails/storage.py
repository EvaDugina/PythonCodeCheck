# -*- coding: utf-8 -*-

# Написать key-value хранилище. Данные будут сохраняться в файле storage.data.
# Добавление новых данных в хранилище и получение текущих значений осуществляется с помощью утилиты командной строки storage.py.
# Пример работы утилиты:
# Сохранение значения value по ключу key_name:
# $ storage.py --key key_name --val value
#
# Получение значения по ключу key_name:
# $ storage.py --key key_name
# Утилита может вызваться со следующими параметрами:
# --key <имя ключа>, где <имя ключа> - ключ по которому сохраняются/получаются значения
# --val <значение>, где <значение> - сохраняемое значение.
# Если при запуске утилиты переданы оба ключа,
# происходит добавление переданного значения по ключу и сохранение данных в файле.
# Если передано только имя ключа, происходит чтение файла хранилища и вывод на печать значений,
# которые были сохранены по данному ключу.
# Обратите внимание, что значения по одному ключу не перезаписываются, а добавляются к уже сохраненным.
# Другими словами - по одному ключу могут храниться несколько значений.
# При выводе на печать, значения выводятся в порядке их добавления в хранилище.
# Формат вывода на печать для нескольких значений:
# value_1, value_2
#
# Обратите внимание на пробел после запятой. Если значений по ключу не было найдено, выведите пустую строку или None.
# Подсказки:
# •	Для работы с аргументами командной строки используйте модуль argparse.
# •	Хранить данные в файле можно в формате JSON с помощью модуля стандартной библиотеки  json.
# •	Файл следует можно с помощью модуля tempfile.

import argparse
import os.path
import json
import tempfile

filename = "storage.data"


def get_json_dict():
    a = dict()
    if not (os.path.exists(filename)):
        return a
    fp = open(filename, mode="r")
    content = fp.read()
    if content:
        a = dict(json.loads(content))
    fp.close()
    return a


def save_json_dict(dct):
    fp = open(filename, mode="w")
    json.dump(dct, fp)
    fp.close()


def store_value(key, value):
    dct = get_json_dict()

    if dct.get(key):
        dct[key].append(value)
    else:
        dct[key] = [value]
    save_json_dict(dct)


def get_value(key):
    dct = get_json_dict()

    if dct.get(key):
        print(*dct[key], sep=', ')
    else:
        print(None)


parser = argparse.ArgumentParser(description='Store some data.')
parser.add_argument('--key', type=str)
parser.add_argument('--value', type=str)
args = parser.parse_args()

if args.key and args.value:
    store_value(args.key, args.value)
elif args.key and not args.value:
    get_value(args.key)
else:
    print("Enter key or key & value. For help use -h.")
