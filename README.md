## Развертывание на виртуальной машине

1. Клонирование репозитория:
   `git clone https://github.com/Kubtonk/lab-rab-6.git`
2. Переход в каталог проекта:
   `cd lab-rab-6`
3. Создание и активация venv:
   `python3 -m venv venv && source venv/bin/activate`
4. Установка зависимостей:
   `pip install -r requirements.txt`
5. Настройка порта и запуск:
   `export PORT=5000 && python app.py`
