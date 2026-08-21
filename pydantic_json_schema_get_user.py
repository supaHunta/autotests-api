from clients.private_http_builder import AuthenticationUserSchema
from clients.users.private_users_client import get_private_users_client
from clients.users.public_users_client import get_public_users_client
from clients.users.users_schema import CreateUserRequestSchema, GetUserResponseSchema
# Добавили импорт функции validate_json_schema
from tools.assertions.schema import validate_json_schema
from tools.fakers import fake

#Инициализируем public_users_client
public_users_client = get_public_users_client()

#Определяем данные для создания пользователя
create_user_request = CreateUserRequestSchema(
    email=fake.email(),
    password="string",
    last_name="string",
    first_name="string",
    middle_name="string"
)

#Создаем пользователя для дальнейшей аутентификации и определяем данные для создания приватного клиента
user_data = public_users_client.create_user(create_user_request)
authentication_user = AuthenticationUserSchema(
    email=create_user_request.email,
    password=create_user_request.password
)
#Инициализируем private_users_client
private_users_client = get_private_users_client(authentication_user)

#Получаем информацию о раннее созданном пользователе
get_user_response = private_users_client.get_user_api(user_data.user.id)

#Получаем JSON-схему по которой будем валидировать ответ
get_user_response_schema = GetUserResponseSchema.model_json_schema()

#Валидируем ответ по схеме
validate_json_schema(instance=get_user_response.json(), schema=get_user_response_schema)