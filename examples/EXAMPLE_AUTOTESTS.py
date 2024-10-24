# -*- coding: utf-8 -*-
""" тесты для лабораторной №1 """
import importlib

import pytest
import copy
import ast
import re

from student_code.main import *

# @pytest.fixture(scope="session")
# def path(request) -> str:
#     return request.config.getoption("--path")
#
#
# lensort = unique = my_enumerate = words_frequency = for_list = lc_list = map_list = None
#
#
# def test_path(path):
#     global lensort, unique, my_enumerate, words_frequency, for_list, lc_list, map_list
#     if path is None:
#         print("No path!")
#         pytest.exit('No argument --path!', returncode=4)
#     path = ".".join(path.split("/"))
#
#     try:
#         student_module = importlib.import_module(path)
#         try:
#             lensort = getattr(student_module, "lensort")
#             unique = getattr(student_module, "unique")
#             my_enumerate = getattr(student_module, "my_enumerate")
#             words_frequency = getattr(student_module, "words_frequency")
#             for_list = getattr(student_module, "for_list")
#             lc_list = getattr(student_module, "lc_list")
#             map_list = getattr(student_module, "map_list")
#         except AttributeError as e:
#             # pytest.exit(e, returncode=4)
#             print(e)
#     except ModuleNotFoundError:
#         pytest.exit(f'Module "{path}" not found!', returncode=4)
#
#     assert True

# @pytest.mark.xfail() пригодится
# TODO проверить на наличие функции с именем
# TODO переделать unique_listay и т.д. в fixture

unique_list = [
    ["python", "python", "ruby", "java", "c", "c++", "ruby", "ruby"],
    ["1", "1", 1, "c", 1, "aaaaaa"],
    ["", 3.15, "", "c", 3.16, "ruby"],
    [1, 11, 3, 1, 2, "python"],
    ["python", " ", " ", "c", 0, "0000"],
]

string_list = [
    ["python", "perl", "java", "c", "haskell", "ruby"],
    ["perl", "python", "java", "c", "haskell", "ruby"],
    ["", "perl", "java", "c", "haskell", "ruby"],
    ["1", "11", "3", "01", "2", "python"],
    ["python", "perl", "java", "c", "haskell", "ruby"],
]

right_words_frequency = [
    (
        ".gitignore",
        {
            "log.txt": 1,
            "*/__pycache__": 1,
            "__pycache__": 1,
            ".idea": 2,
            ".pytest_cache": 2,
            "#": 8,
            "Automatically": 1,
            "generated": 3,
            "by": 3,
            "`hgimportsvn`": 1,
            ".svn": 1,
            ".hgsvn": 1,
            "Ignore": 1,
            "local": 1,
            "virtualenvs": 1,
            "lib/": 1,
            "bin/": 1,
            "include/": 1,
            ".Python/": 1,
            "These": 1,
            "lines": 1,
            "are": 1,
            "suggested": 1,
            "according": 1,
            "to": 2,
            "the": 1,
            "svn:ignore": 1,
            "property": 1,
            "Feel": 1,
            "free": 1,
            "enable": 1,
            "them": 2,
            "uncommenting": 1,
            "*.pyc": 1,
            "*.pyo": 1,
            "*.swp": 1,
            "*.class": 1,
            "*.orig": 1,
            "*~": 1,
            ".hypothesis/": 1,
            "autogenerated": 1,
            "src/_pytest/_version.py": 1,
            "setuptools": 1,
            ".eggs/": 1,
            "doc/*/_build": 1,
            "doc/*/.doctrees": 1,
            "build/": 1,
            "dist/": 1,
            "*.egg-info": 1,
            "htmlcov/": 1,
            "issue/": 1,
            "env/": 1,
            ".env/": 1,
            ".venv/": 1,
            "/pythonenv*/": 1,
            "3rdparty/": 1,
            ".tox": 1,
            ".cache": 1,
            ".mypy_cache": 1,
            ".coverage": 1,
            ".coverage.*": 1,
            "coverage.xml": 1,
            ".ropeproject": 1,
            ".hypothesis": 1,
            ".pydevproject": 1,
            ".project": 1,
            ".settings": 1,
            ".vscode": 1,
            "__pycache__/": 1,
            ".python-version": 1,
            "pip": 1,
            "pip-wheel-metadata/": 1,
            "pytest": 1,
            "debug": 1,
            "logs": 1,
            "via": 1,
            "--debug": 1,
            "pytestdebug.log": 1,
            "storage.data": 1,
            "src/*": 1,
            "!src/labs/": 1,
            "src/labs/*": 1,
            "!src/labs/lab_1": 1,
            "src/labs/lab_1/*": 1,
            "!src/labs/lab_1/test_file.txt": 1,
        },
    ),
    (
        "setup.py",
        {
            '"""Minimal': 1,
            "setup": 1,
            "file": 1,
            "for": 1,
            "tasks": 1,
            'project."""': 1,
            "from": 1,
            "setuptools": 1,
            "import": 1,
            "setup,": 1,
            "find_packages": 1,
            "setup(": 1,
            "name='labs',": 1,
            "packages=find_packages('src',": 1,
            "include=[": 1,
            "'labs*'": 1,
            "]),": 1,
            "package_dir={'':": 1,
            "'src'},": 1,
            ")": 1,
        },
    ),
    (
        "src\\labs\\lab_1\\test_file.txt",
        {
            "PvcStatus": 1,
            "pvcAdd_16s_Sfs(const": 1,
            "Pvc16s*": 3,
            "pSrc1,": 1,
            "const": 2,
            "pSrc2,": 1,
            "pDst,": 1,
            "int": 4,
            "len,": 1,
            "scaleFactor)": 1,
            "{": 14,
            "if": 9,
            "(!pSrc1": 1,
            "||": 2,
            "!pSrc2": 1,
            "!pDst)": 1,
            "return": 3,
            "pvcStsNullPtrErr;": 1,
            "(len": 1,
            "<": 6,
            "1)": 1,
            "pvcStsSizeErr;": 1,
            "decr": 1,
            "=": 64,
            "len": 1,
            "&": 5,
            "~0x07,": 1,
            "i": 7,
            "0;": 1,
            "//const": 1,
            "float": 2,
            "scaler": 2,
            "1.0f/powf(2,": 1,
            "scaleFactor);": 5,
            "powf(2,": 1,
            "(scaleFactor": 1,
            ">": 4,
            "0)": 3,
            "__m128i": 5,
            "one,": 1,
            "two,": 1,
            "div_num,": 1,
            "incr,": 1,
            "eq1,": 1,
            "eq2,": 1,
            "_ost,": 1,
            "even;": 1,
            "mask,": 1,
            "sum,": 1,
            "sign,": 1,
            "minus_ch1,": 1,
            "minus_ch2;": 1,
            "//": 1,
            "lt,": 1,
            "only_eq,": 1,
            "odd;": 1,
            "num,": 1,
            "ch1,": 1,
            "ch2,": 1,
            "ost;": 1,
            "round_num": 1,
            "_mm_set1_epi16(scaler": 1,
            "/": 2,
            "2),": 1,
            "minus_scaler": 1,
            "_mm_mullo_epi16(round_num,": 2,
            "_mm_set1_epi16(-1)),": 1,
            "triple_scale_num": 1,
            "_mm_set1_epi16(3));": 1,
            "for": 4,
            "(i;": 3,
            "decr;": 2,
            "+=": 2,
            "8)": 2,
            "ch1": 1,
            "_mm_loadu_si128((__m128i*)": 2,
            "pSrc1[i]);": 1,
            "ch2": 1,
            "pSrc2[i]);": 1,
            "//div_num": 1,
            "_mm_srai_epi16(ch,": 1,
            "//sum": 3,
            "_mm_add_epi16(div_num,": 1,
            "div_const);": 1,
            "minus_ch1": 3,
            "_mm_srai_epi16(ch1,": 1,
            "minus_ch2": 2,
            "_mm_srai_epi16(ch2,": 1,
            "sum": 3,
            "_mm_add_epi16(minus_ch1,": 4,
            "minus_ch2);": 3,
            "eq1": 3,
            "_mm_mullo_epi16(_mm_set1_epi16(scaler),": 3,
            "minus_ch1);": 2,
            "eq2": 3,
            "_mm_cmpgt_epi16(_mm_set1_epi16(0),": 3,
            "_mm_cmpeq_epi16(eq1,": 1,
            "ch1);": 1,
            "_mm_cmpeq_epi16(eq2,": 1,
            "ch2);": 1,
            "_mm_mullo_epi16(eq1,": 1,
            "minus_ch1));": 1,
            "_mm_add_epi16(minus_ch2,": 1,
            "_mm_mullo_epi16(eq2,": 1,
            "minus_ch2));": 1,
            "_mm_sub_epi16(sum,": 2,
            "_mm_add_epi16(eq1,": 1,
            "eq2));": 1,
            "//eq": 5,
            "sum);": 4,
            "_mm_cmpeq_epi16(eq,": 1,
            "ch);": 1,
            "_mm_add_epi16(minus,": 3,
            "_mm_mullo_epi16(eq,": 1,
            "minus)": 1,
            "eq);": 2,
            "//one": 2,
            "_mm_add_epi16(ch,": 1,
            "intrin_value);": 1,
            "//two": 1,
            "_mm_mullo_epi16(sum,": 2,
            "_mm_set1_epi16(scaler));": 1,
            "//ost": 2,
            "_mm_sub_epi16(one,": 1,
            "two);": 1,
            "ost": 2,
            "_mm_sub_epi16(_mm_add_epi16(ch1,": 1,
            "ch2),": 1,
            "_mm_set1_epi16(scaler)));": 1,
            "ost);": 3,
            "//sign": 2,
            "_mm_set1_epi16(1);": 1,
            "sign));": 1,
            "_mm_abs_epi16(ost);": 2,
            "sign": 1,
            "_mm_set1_epi16(1)));": 1,
            "//minus": 1,
            "_mm_cmpgt_epi16(ost,": 1,
            "round_num);": 2,
            "_mm_cmpeq_epi16(ost,": 2,
            "//odd": 1,
            "_mm_and_si128(sum,": 1,
            "_mm_set1_epi16(1));": 2,
            "//only_eq": 2,
            "_mm_mullo_epi16(odd,": 1,
            "//mask": 3,
            "_mm_abs_epi16(_mm_add_epi16(minus,": 1,
            "only_eq));": 1,
            "mask": 2,
            "_mm_abs_epi16(_mm_add_epi16(_mm_cmpgt_epi16(ost,": 1,
            "round_num),": 1,
            "_mm_mullo_epi16(_mm_and_si128(sum,": 1,
            "_mm_set1_epi16(1)),": 2,
            "round_num))));": 1,
            "//lt": 1,
            "_mm_cmplt_epi16(triple_scale_num,": 2,
            "_mm_cmpeq_epi16(triple_scale_num,": 1,
            "//even": 1,
            "_mm_andnot_si128(sum,": 1,
            "_mm_mullo_epi16(even,": 1,
            "_mm_abs_epi16(eq));": 1,
            "_mm_sub_epi16(only_eq,": 1,
            "lt);": 1,
            "_mm_add_epi16(mask,": 4,
            "one);": 1,
            "_mm_mullo_epi16(sign,": 2,
            "mask);": 1,
            "_mm_sub_epi16(_mm_mullo_epi16(_mm_andnot_si128(sum,": 1,
            "_mm_abs_epi16(_mm_cmpeq_epi16(triple_scale_num,": 1,
            "ost))),": 1,
            "ost))));": 1,
            "_mm_storeu_si128((__m128i*)": 2,
            "pDst[i],": 2,
            "/*": 1,
            "(int": 1,
            "k": 2,
            "i;": 1,
            "+": 18,
            "8;": 1,
            "k++)": 1,
            'printf("el[%d]': 1,
            '%d\\n",': 1,
            "k,": 1,
            "pDst[k]);": 1,
            "}*/": 1,
            "}": 13,
            "else": 4,
            "_mm_add_epi16(": 1,
            "_mm_set_epi16(pSrc1[i": 1,
            "7],": 2,
            "pSrc1[i": 6,
            "6],": 2,
            "5],": 2,
            "4],": 2,
            "3],": 2,
            "2],": 2,
            "1],": 2,
            "pSrc1[i]),": 1,
            "_mm_set_epi16(pSrc2[i": 1,
            "pSrc2[i": 6,
            "pSrc2[i])));": 1,
            "buf;": 1,
            "len;": 1,
            "++i)": 1,
            "buf": 3,
            "(pSrc1[i]": 1,
            "pSrc2[i])": 1,
            "(float)scaler;": 1,
            "(buf": 4,
            "32766)": 1,
            "pDst[i]": 6,
            "32767;": 1,
            "continue;": 4,
            "-1.0*32767)": 1,
            "-32768;": 1,
            "-": 3,
            "floor(buf)": 1,
            "==": 2,
            "0.5)": 1,
            "short": 1,
            "beb": 3,
            "(short)floor(buf);": 1,
            "%": 3,
            "2;": 1,
            "((short)floor(buf)": 1,
            "2": 2,
            "1;": 2,
            "((short)ceilf(buf)": 1,
            "-1)": 1,
            "std::ceilf(buf": 1,
            "0.5);": 2,
            "std::floor(buf": 1,
            "pvcStsNoErr;": 1,
        },
    ),
]

num_list = [[1, 2, 3, 4, 5, 6], [i for i in range(1000)], [i for i in range(100000)]]

existing_single_params = [
    ("single", 2222),
    ("single_key", "one_key_only"),
    ("key_22", 47),
]

existing_multiple_params = [
    ("key", "value, value"),
    ("key_222", "2, 47"),
    ("param", "key, key_aaaa"),
]

not_existing_params = ["key1", "singgle", 1, 2, "key_223"]


@pytest.mark.parametrize("input_list", string_list)
class TestLensort:
    """тесты для lensort"""

    def test_lensort_sorting(self, input_list):
        """сортировка списка строк по длине"""
        input_copy = copy.deepcopy(input_list)
        assert lensort(input_list) == sorted(input_copy, key=lambda length: len(length))

    def test_lensort_nochange(self, input_list):
        """проверка на не изменность изначального списка"""
        input_copy = copy.deepcopy(input_list)
        assert input_copy != lensort(input_list)


@pytest.mark.parametrize("input_list", unique_list)
class TestUnique:
    """тесты для unique"""
    
    def test_unique_sorting(self, input_list):
        """должен получать список уникальных элементов"""
        input_copy = copy.deepcopy(input_list)
        assert unique(input_list) == list(set(input_copy))

    def test_unique_nochange(self, input_list):
        """проверка на не изменность изначального списка"""
        input_copy = copy.deepcopy(input_list)
        assert input_copy != list(unique(input_list))


@pytest.mark.parametrize("input_list", string_list)
class TestMyEnumerate:
    """тесты для myEnumerate"""
    
    def test_my_enumerate(self, input_list):
        """возвращает список кортежей, в каждом из которых два элемента: элемент списка и порядковый номер данного элемента"""
        input_copy = copy.deepcopy(input_list)
        assert my_enumerate(input_list) == list(zip(range(len(input_copy)), input_copy))

    def test_my_enumerate_nochange(self, input_list):
        """проверка на не изменность изначального списка"""
        input_copy = copy.deepcopy(input_list)
        assert input_copy != my_enumerate(input_list)


@pytest.mark.parametrize("file_name, right_frequency", right_words_frequency)
class TestWordsFrequency:
    """тесты для wordsFrequency"""
    
    def test_words_frequency(self, file_name, right_frequency, capsys):
        """проверка на подсчет количества слов в файле"""
        words_frequency(file_name)
        captured = capsys.readouterr()
        # преобразуем str из captured.out в dict
        assert right_frequency == ast.literal_eval(captured.out)


@pytest.mark.parametrize("input_list", num_list)
class TestDecorator:
    """декоратор, считающий время выполнения функции"""

    # ожидаемый формат вывода
    pattern = r"\d+(.\d+)?\n"

    def test_decorator_for(self, input_list, capsys):
        """функция с помощью for"""
        for_list(input_list)
        captured = capsys.readouterr()
        assert re.fullmatch(self.pattern, (captured.out)) != None

    def test_decorator_lc(self, input_list, capsys):
        """функция с помощью list comprehensions"""
        lc_list(input_list)
        captured = capsys.readouterr()
        assert re.fullmatch(self.pattern, (captured.out)) != None

    def test_decorator_map(self, input_list, capsys):
        """функция с помощью lmap"""
        map_list(input_list)
        captured = capsys.readouterr()
        assert re.fullmatch(self.pattern, (captured.out)) != None


good_params = [
    ("key", "value"),
    ("key_222", 2),
    ("param", "key"),
    ("param", "key_aaaa"),
    ("key_22", 47),
    ("key_222", 47),
    ("key", "value"),
    ("single", 2222),
    ("single_key", "one_key_only"),
]


# TODO можно ли сохранять одинаковые значения в один ключ?
# TODO добавить проверки на возможность работы с утилитой (можно ли вообще запустить с флагами)
# TODO запустить с несуществующими флагами
class TestStorage:
    """тесты для утилиты storage"""

    @pytest.fixture(scope="class", autouse=True)
    def storage_save(self):
        """фикстура для добавления ключей в хранилище"""
        # чистим файл
        file = open("storage.data", "w")
        file.close()

        for key, value in good_params:
            os.system(f"python src/labs/lab_1/storage.py --key {key} --val {value}")

    @pytest.mark.parametrize("key, value", existing_single_params)
    def test_storage_single_keys(self, key, value, capfd):
        """проверяем на наличие ключей с одиночными параметрами"""
        assert self.check_stored_value(key, value, capfd)

    @pytest.mark.parametrize("key, value", existing_multiple_params)
    def test_storage_multiple_params(self, key, value, capfd):
        """проверяем на наличие ключей с несколькими параметрами"""
        assert self.check_stored_value(key, value, capfd)

    @pytest.mark.parametrize("key", not_existing_params)
    def test_storage_no_existing_params(self, key, capfd):
        """проверяем на наличие ключей с несколькими параметрами"""
        # TODO заменить None or "" на регулярку
        assert self.check_stored_value(key, None, capfd) or self.check_stored_value(
            key, "", capfd
        )

    def check_stored_value(self, key, value, capfd):
        """проверяем правильное ли значение сохранилось в хранилище"""
        os.system(f"python src/labs/lab_1/storage.py --key {key}")
        # тут capfd тк он работает со всеми выводами на уровне системы,
        # а capsys с выводами только на уровне питона
        captured = capfd.readouterr()
        pattern = f"{value}\r?\n?"
        return re.fullmatch(pattern, captured.out)
