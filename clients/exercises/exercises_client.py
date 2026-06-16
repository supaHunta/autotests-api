from typing import TypedDict

import httpx

from clients.api_client import APIClient
from clients.private_http_builder import AuthenticationUserDict, get_private_http_client



class GetExercisesQueryDict(TypedDict):
    """
    Описание структуры запроса на получение списка заданий.
    """
    courseId: str

class Exercise(TypedDict):
    id: str
    title: str
    courseId: str
    maxScore: int | None
    minScore: int | None
    orderIndex: int
    description: str
    estimatedTime: str | None

class GetExercisesResponseDict(TypedDict):
    exercises: list[Exercise]

class GetExerciseResponseDict(TypedDict):
    exercise: Exercise

class CreateExerciseRequestDict(TypedDict):
    title: str
    courseId: str
    maxScore: int | None
    minScore: int | None
    orderIndex: int
    description: str
    estimatedTime: str | None

class CreateExerciseResponseDict(TypedDict):
    exercise: Exercise

class UpdateExerciseRequestDict(TypedDict):
    title: str | None
    maxScore: int | None
    minScore: int | None
    orderIndex: int | None
    description: str | None
    estimatedTime: str | None

class UpdateExerciseResponseDict(TypedDict):
    exercise: Exercise


class ExercisesClient(APIClient):

    """Класс, предоставляющий методы для работы с эндпоинтами упражнений"""

    def get_exercises_api(self, query: GetExercisesQueryDict) -> httpx.Response:
        """
        Метод получения списка заданий.

        :param query: Словарь с courseId.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get("/api/v1/exercises", params=query)

    def get_exercise_api(self, exercise_id: str) -> httpx.Response:
        """Метод получает упражнение по id

        :param exercise_id: ID упражнения
        :return: Ответ от сервера в виде объекта httpx.Response."""
        return self.get(f"/api/v1/exercises/{exercise_id}")

    def create_exercise_api(self, request: CreateExerciseRequestDict) -> httpx.Response:
        """Метод создает упражнение

        :param request: Словарь, содержащий поля, необходимые для создания упражнения
        :return: Ответ от сервера в виде объекта httpx.Response."""
        return self.post("/api/v1/exercises", json=request)

    def update_exercise_api(self, exercise_id: str, exercise_data: UpdateExerciseRequestDict) -> httpx.Response:
        """Метод, частично меняющий упражнение

        :param exercise_id: ID упражнения, которое нужно изменить
        :param exercise_date: Словарь, содержащий поля, подлежащие изменению
        :return: Ответ от сервера в виде объекта httpx.Response."""
        return self.patch(f"/api/v1/exercises/{exercise_id}", json=exercise_data)

    def delete_exercise_api(self, exercise_id: str) -> httpx.Response:
        """Метод удаляющий упражнение\

        :param exercise_id: ID упражнения, которое нужно удалить
        :return: Ответ от сервера в виде объекта httpx.Response.
        """
        return self.delete(f"/api/v1/exercises/{exercise_id}")

    def get_exercises(self, query: GetExercisesQueryDict) -> GetExercisesResponseDict:
        """
        Метод получает упражнения по конкретному курсу

        :param query: courseId курса, из которого мы будем получать упражнения
        :return: Сериализованный ответ по упражнениям из курса
        """
        response = self.get_exercises_api(query)
        return response.json()

    def get_exercise(self, exercise_id: str) -> GetExerciseResponseDict:
        """
        Метод получающий информацию о конкретном упражнении

        :param exercise_id: ID упражнение
        :return: Сериализованный ответ по запрашиваемому упражнению
        """
        response = self.get_exercise_api(exercise_id=exercise_id)
        return response.json()

    def create_exercise(self, request: CreateExerciseRequestDict) -> CreateExerciseResponseDict:
        """
        Метод создающий упражнение

        :param request: Словарь, содержащий информацию для создания упражнения
        :return: Сериализованный ответ, содержащий информацию о созданном упражнении
        """
        response = self.create_exercise_api(request=request)
        return response.json()

    def update_exercise(self, exercise_id: str, request: UpdateExerciseRequestDict) -> UpdateExerciseResponseDict:
        """
        Метод изменяющий информацию об упражнении

        :param exercise_id: ID упражнения
        :param request: Словарь, содержащий изменения
        :return: Сериализованный ответ, содержащий информацию об измененном упражнении
        """
        response = self.update_exercise_api(exercise_id=exercise_id, exercise_data=request)
        return response.json()

def get_exercises_client(user: AuthenticationUserDict) -> ExercisesClient:
    """
        Функция создаёт экземпляр ExercisesClient с уже настроенным HTTP-клиентом.

        :return: Готовый к использованию ExercisesClient.
        """
    return ExercisesClient(get_private_http_client(user))

