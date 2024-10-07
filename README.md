# PythonCodeCheck
Модуль проверки Python-кода


## Установка
```python 
pip install pylint
pip install -r requirements.txt
```

## Виртуальное окружение

### Обновить код в виртуальном окружении
```console
env/Scripts/python setup.py install
```

### Активация виртуального окружения на Windows

1. Запускаем консоль от админа

2. Активация
```console
env/Scripts/activate.bat
```

3. Деактивация
```console
env/Scripts/deactivate.bat
```

4. Подробнее
https://timeweb.cloud/tutorials/python/kak-sozdat-virtualnoe-okruzhenie

5. На Windows, при ошибке "выполнение сценариев отключено в этой системе": 
https://ru.stackoverflow.com/questions/935212/powershell-%D0%B2%D1%8B%D0%BF%D0%BE%D0%BB%D0%BD%D0%B5%D0%BD%D0%B8%D0%B5-%D1%81%D1%86%D0%B5%D0%BD%D0%B0%D1%80%D0%B8%D0%B5%D0%B2-%D0%BE%D1%82%D0%BA%D0%BB%D1%8E%D1%87%D0%B5%D0%BD%D0%BE-%D0%B2-%D1%8D%D1%82%D0%BE%D0%B9-%D1%81%D0%B8%D1%81%D1%82%D0%B5%D0%BC%D0%B5

### ЛОКАЛЬНОЕ ИСПОЛЬЗОВАНИЕ GIT-HOOKS

```console
pip install pre-commit
```

#### Commitizen: Versioning & Commit Conventional Hook
https://dev.to/okeeffed/semantic-versioning-in-python-with-git-hooks-5c5a
https://github.com/commitizen-tools/commitizen

##### 1. Установка необходимых компонентов
```console
pip install --user pipenv
pipenv install --dev pre-commit Commitizen toml
pipenv run cz init
pre-commit autoupdate
pre-commit install
```

##### 2. Использование хука, не дающего изменить файлы auth_ssh и update*
Скопировать скрипт pre-commit.legacy из папки .hooks/_localHooks и вставить его в папку .git/hooks

##### Проверка истории коммитов и bump версии
```console
pipenv run cz bump
```

##### Обновление CHANGELOG
```console
pipenv run cz changelog
```
