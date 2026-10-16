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

## Запуск в Docker
1. Сборка образа: `sudo docker build -t lab6-app:v1 .`
2. Запуск контейнера: `sudo docker run -d --name cloud-app -p 8080:5000 lab6-app:v1`
3. Проверка: `curl http://localhost:8080`
