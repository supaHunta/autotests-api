import httpx

from tools.fakers import fake

#Определяем тело запроса для создания пользователя
create_user_payload = {
  "email": fake.email(),
  "password": "string",
  "lastName": "string",
  "firstName": "string",
  "middleName": "string"
}

#Отправляем запрос на создание пользователя и получаем ответ
create_user_response = httpx.post('http://213.171.26.61:8000/api/v1/users', json=create_user_payload)
create_user_data = create_user_response.json()
print(f"User creation: {create_user_response.status_code}")

#Извлекаем id из ответа
user_id = create_user_data["user"]["id"]

#Определяем тело запроса для получения токена
login_payload = {
    "email": create_user_payload["email"],
    "password": create_user_payload["password"]
}
#Отправляем запрос и получаем ответ
login_response = httpx.post('http://213.171.26.61:8000/api/v1/authentication/login', json=login_payload)
login_response_data = login_response.json()
print(f'Authentication: {login_response.status_code}')
#Выносим токен в отдельную переменную
access_token = login_response_data["token"]["accessToken"]

#Определяем заголовки для следующих запросов
headers = {"Authorization": f'Bearer {access_token}'}


#Определяем тело запроса для обновления информации о пользователе
update_user_payload = {
  "email": fake.email(),
  "lastName": "string",
  "firstName": "string",
  "middleName": "string"
}

#Отправляем запрос на изменение информации о пользователе
update_user_response = httpx.patch(f'http://213.171.26.61:8000/api/v1/users/{user_id}', json=update_user_payload, headers=headers)
print(f"Update user: {update_user_response.status_code}")
