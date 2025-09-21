# DDSApp — Инструкция по запуску

## 1. Клонирование репозитория

```bash
git clone https://github.com/staizy/DDSApp.git
cd DDSApp
```

## 2. Создание и активация виртуального окружения

**Windows:**
```bash
python -m venv .venv
.venv\Scripts\activate
```

**Linux/Mac:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

## 3. Установка зависимостей

```bash
pip install -r requirements.txt
```

## 4. Применение миграций

```bash
python manage.py migrate
```

## 5. Создание суперпользователя

```bash
python manage.py createsuperuser
```

## 6. Запуск сервера разработки

```bash
python manage.py runserver
```

## 7. Открытие сайта

Перейдите в браузере по адресу:  
[http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

> **Админ-панель:**  
> [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

> **Настройки проекта:**  
> Все настройки находятся в файле `DDSApp/settings.py`.

> **Изменение базы данных:**  
> Измените параметр `DATABASES` в `DDSApp/settings.py` при необходимости.
