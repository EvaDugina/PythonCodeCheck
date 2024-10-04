# PythonCodeCheck
Модуль проверки Python-кода

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
pre-commit install
pre-commit autoupdate
```

##### 2. Использование хука, не дающего изменить файлы auth_ssh и update*
Скопировать скрипт pre-commit.legacy из папки .hooks/_localHooks и вставить его в папку .git/hooks

##### Проверка историю коммитов наизменения и пывысить версию
```console
pipenv run cz bump
```

##### Обновление CHANGELOG
```console
pipenv run cz changelog
```
