# Cоздания простого REST API для сайта объявлений с использованием Flask

### Шаг 1: Установка необходимых библиотек
pip install Flask

### Шаг 2: Создание структуры проекта
Создай папку для проекта и внутри нее создай файл app.py:

ad_listing/
│
└── app.py

## Шаг 3: Написание кода
В файле app.py напиши следующий код:

from flask import Flask, jsonify, request

app = Flask(__name__)

#Список для хранения объявлений
ads = []
ad_id_counter = 1

@app.route('/ads', methods=['POST'])
def create_ad():
    global ad_id_counter
    data = request.json
    ad = {
        'id': ad_id_counter,
        'title': data['title'],
        'description': data['description'],
        'created_at': data['created_at'],
        'owner': data['owner']
    }
    ads.append(ad)
    ad_id_counter += 1
    return jsonify(ad), 201

@app.route('/ads', methods=['GET'])
def get_ads():
    return jsonify(ads), 200

@app.route('/ads/<int:ad_id>', methods=['DELETE'])
def delete_ad(ad_id):
    global ads
    ads = [ad for ad in ads if ad['id'] != ad_id]
    return jsonify({'message': 'Ad deleted'}), 204

if __name__ == '__main__':
    app.run(debug=True)

Описание кода
Импорт библиотек: Мы импортируем необходимые модули из Flask.
Создание приложения: Создаем экземпляр Flask.
Хранение объявлений: Используем список ads для хранения объявлений и счетчик ad_id_counter для уникальных идентификаторов.
Метод POST: Создает новое объявление. Данные передаются в формате JSON.
Метод GET: Возвращает все объявления.
Метод DELETE: Удаляет объявление по его идентификатору.
Запуск приложения: Приложение запускается в режиме отладки.

## Шаг 4: Запуск проекта
Чтобы запустить проект, выполни следующую команду в терминале из папки проекта:

python app.py

### POST: Создание нового объявления с передачей данных в формате JSON.
### GET: Получение всех объявлений.
### GET (одиночное): Получение конкретного объявления по его ID.
### DELETE: Удаление объявления по его ID.
