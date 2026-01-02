# FastAI

## Репозиторий для бэкенд-разработчиков.

Инструкции и справочная информация по разворачиванию локальной инсталляции собраны
в документе [CONTRIBUTING.md](./CONTRIBUTING.md).

## Как развернуть локально нп Ubuntu 24.04
Необходимо установить [Git](https://git-scm.com/) и [Python](https://www.python.org/).

Склонировать репозиторий можно командой:
```shell
$ git clone https://gitlab.dvmn.org/root/fastapi-articles.git
```
Необходимо установить [uv](https://docs.astral.sh/uv/).
```shell
$ pip install uv
```

После установки uv, переходим в директорию проекта:
```shell
$ cd fastapi-articles
```

Создаем виртуальное окружение со всеми установленными зависимостями:
```shell
$ uv sync
```
После этого активируйте виртуальное окружение в текущей сессии терминала:

```shell
$ source .venv/bin/activate  # для Linux
```

Проверяем, что все зависимости установлены и запустим проект:
```shell
$ fastapi dev src/main.py
```
Приложение будет работать по адресу http://127.0.0.1:8000/
