


# CSV Parser

Простой HTTP сервис для работы с импортируемыми данными в формате CSV.

## Требования

- Python 3.9 или выше

## Установка

1. Склонируйте репозиторий:

```bash
git clone https://github.com/your_username/csv-parser.git
cd csv-parser
```

2. Создайте виртуальное окружение и активируйте его:

```bash
python3 -m venv venv
source venv/bin/activate
```

3. Установите зависимости проекта:

```bash
pip install -r requirements.txt
```

## Запуск

1. Запустите приложение:

```bash
python app.py
```

2. Приложение будет запущено на http://localhost:5000

## Использование

### Загрузка файла

Отправьте POST запрос на `/upload`, указав файл в поле `file`:

```bash
curl -X POST -F "file=@/path/to/your/file.csv" http://localhost:5000/upload
```

### Получение списка файлов

Отправьте GET запрос на `/files`:

```bash
curl http://localhost:5000/files
```

### Получение данных из файла

Отправьте GET запрос на `/data` с параметром `filename`, указывающим имя файла:

```bash
curl http://localhost:5000/data?filename=your_file.csv
```

### Удаление файла

Отправьте DELETE запрос на `/delete/<filename>`, указав имя файла:

```bash
curl -X DELETE http://localhost:5000/delete/your_file.csv
```

## Тестирование

Для запуска тестов выполните следующую команду:

```bash
python -m unittest tests.py
```

## Лицензия

Этот проект лицензирован по лицензии MIT. Подробности смотрите в файле [LICENSE](LICENSE).
```

В обновленном README файле добавлен раздел "Тестирование", который описывает запуск тестов с помощью команды `python -m unittest tests.py`.
