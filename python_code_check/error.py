#!/usr/bin/env python
# -*- coding: utf-8 -*-

from enum import Enum


class Result(Enum):
    SUCCESS = 0
    ERROR_VALIDATE_CONFIGURATION_FILE = 101
    ERROR_GET_CHECKER_BY_TOOL_NAME = 102
    ERROR_VALIDATE_FILES_TO_CHECK = 103


def handle_result(result_code):
    if result_code == Result.SUCCESS:
        result_text = "Успешно!"
    elif result_code == Result.ERROR_VALIDATE_CONFIGURATION_FILE:
        result_text = "Ошибка! Некорректный файл конфигурации"
    elif result_code == Result.ERROR_GET_CHECKER_BY_TOOL_NAME:
        result_text = "Ошибка! Некорректный инструмент проверки"
    elif result_code == Result.ERROR_VALIDATE_FILES_TO_CHECK:
        result_text = "Ошибка! Некорректная передача файлов для проверки"
    else:
        result_text = "Undefined result_code!"

    return result_text
