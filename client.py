import requests

# URL Вашего API
base_url = 'http://127.0.0.1:5000/ads'

# 1. Создание объявления (POST)
response_post = requests.post(base_url, json={
    'title': 'Объявление 1',
    'description': 'Описание 1',
    'created_at': '2023-10-01',
    'owner': 'Владелец 1'
})
print('POST статус-код:', response_post.status_code)  # Выводим статус-код ответа
print('POST ответ:', response_post.text)               # Выводим текст ответа

# 2. Получение всех объявлений (GET)
response_get = requests.get(base_url)
print('GET статус-код:', response_get.status_code)    # Выводим статус-код ответа
print('GET ответ:', response_get.json())               # Выводим текст ответа в формате JSON

# 3. Получение конкретного объявления (GET)
ad_id = 1  # Замените на ID объявления, которое хотите получить
response_get_single = requests.get(f'{base_url}/{ad_id}')
print('GET (одиночное) статус-код:', response_get_single.status_code)  # Выводим статус-код ответа

try:
    response_data = response_get_single.json()  # Попытка декодирования JSON
    print('GET (одиночное) ответ:', response_data)  # Выводим текст ответа в формате JSON
except requests.exceptions.JSONDecodeError:
    print('Ошибка декодирования JSON:', response_get_single.text)  # Выводим текст ответа, если это не JSON
# 4. Удаление объявления (DELETE)
response_delete = requests.delete(f'{base_url}/{ad_id}')
print('DELETE статус-код:', response_delete.status_code)  # Выводим статус-код ответа
print('DELETE ответ:', response_delete.text)               # Выводим текст ответа