from typing import TypedDict

import httpx

from clients.api_client import APIClient

class CreateExerciseDict(TypedDict):
    title: str
    courseId: str
    maxScore: int | None
    minScore: int | None
    orderIndex: int
    description: str
    estimatedTime: str | None

class UpdateExerciseDict(TypedDict):
    title: str | None
    maxScore: int | None
    minScore: int | None
    orderIndex: int | None
    description: str | None
    estimatedTime: str | None


class ExercisesClient(APIClient):

    """Класс, предоставляющий методы для работы с эндпоинтами упражнений"""

    def get_exercises_api(self) -> httpx.Response:
        """Метод получает все упражнения

        :return: Ответ от сервера в виде объекта httpx.Response."""
        return self.get("/api/v1/exercises")

    def get_exercise_api(self, exercise_id: str) -> httpx.Response:
        """Метод получает упражнение по id

        :param exercise_id: ID упражнения
        :return: Ответ от сервера в виде объекта httpx.Response."""
        return self.get(f"/api/v1/exercises/{exercise_id}")

    def create_exercise_api(self, request: CreateExerciseDict) -> httpx.Response:
        """Метод создает упражнение

        :param request: Словарь, содержащий поля, необходимые для создания упражнения
        :return: Ответ от сервера в виде объекта httpx.Response."""
        return self.post("/api/v1/exercises", json=request)

    def update_exercise_api(self, exercise_id: str, exercise_date: UpdateExerciseDict) -> httpx.Response:
        """Метод, частично меняющий упражнение

        :param exercise_id: ID упражнения, которое нужно изменить
        :param exercise_date: Словарь, содержащий поля, подлежащие изменению
        :return: Ответ от сервера в виде объекта httpx.Response."""
        return self.patch(f"/api/v1/exercises/{exercise_id}", json=exercise_date)

    def delete_exercise_api(self, exercise_id: str) -> httpx.Response:
        """Метод удаляющий упражнение\

        :param exercise_id: ID упражнения, которое нужно удалить
        :return: Ответ от сервера в виде объекта httpx.Response.
        """
        return self.delete(f"/api/v1/exercises/{exercise_id}")

