from httpx import Response

from clients.api_client import APIClient

from typing import TypedDict

from clients.public_http_builder import get_public_http_client


class User(TypedDict):
    """
    Описание структуры пользователя.
    """
    id: str
    email: str
    lastName: str
    firstName: str
    middleName: str

class CreateUserRequestDict(TypedDict):
    """
    Описание структуры запроса на создание пользователя
    """
    email: str
    password: str
    lastName: str
    firstName: str
    middleName: str

class CreateUserResponseDict(TypedDict):
    """
    Описание структуры ответа создания пользователя.
    """
    user: User



class PublicUsersClient(APIClient):
    """
    Клиент для работы с публичным эндпоинтом /api/v1/users
    """

    def create_user_api(self, request: CreateUserRequestDict) -> Response:
        """
        Метод выполняет создание пользователя

        :param request: Словарь с необходимыми полями для создания пользователя
        :return: Ответ от сервера в виде объекта httpx.Response.
        """
        return self.post("/api/v1/users", json=request)

    def create_user(self, request: CreateUserRequestDict) -> CreateUserResponseDict:
        response = self.create_user_api(request)
        return response.json()

def get_public_users_client():
    return PublicUsersClient(client=get_public_http_client())