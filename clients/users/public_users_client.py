from httpx import Response

from clients.api_client import APIClient

from typing import TypedDict

class UserCreationDict(TypedDict):
    """
    Описание структуры запроса на создание пользователя
    """
    email: str
    password: str
    lastName: str
    firstName: str
    middleName: str

class PublicUsersClient(APIClient):
    """
    Клиент для работы с публичным эндпоинтом /api/v1/users
    """

    def create_user_api(self, request: UserCreationDict) -> Response:
        """
        Метод выполняет создание пользователя

        :param request: Словарь с необходимыми полями для создания пользователя
        :return: Ответ от сервера в виде объекта httpx.Response.
        """
        return self.post("/api/v1/users", json=request)