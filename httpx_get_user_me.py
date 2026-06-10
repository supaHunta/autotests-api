import httpx

#Определяем payload для отправки запроса
login_payload = {
    "email": "user1@example.com",
    "password": "string"
}
#Отправляем запрос и получаем ответ
login_response = httpx.post('http://localhost:8000/api/v1/authentication/login', json=login_payload)
login_response_data = login_response.json()

#Выносим токен в отдельную переменную
access_token = login_response_data["token"]["accessToken"]

#Определяем заголовки для следующих запросов
headers = {"Authorization": f'Bearer {access_token}'}
user_response = httpx.get('http://localhost:8000/api/v1/users/me', headers=headers)

#Выводим ответ и статус-код
print(user_response.json())
print(user_response.status_code)


