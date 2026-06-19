import httpx

from clients.api_client import APIClient
from clients.exercises.exercises_schema import GetExercisesQuerySchema, CreateExerciseRequestSchema, \
    UpdateExerciseRequestSchema, GetExercisesResponseSchema, CreateExerciseResponseSchema, UpdateExerciseResponseSchema
from clients.private_http_builder import get_private_http_client, AuthenticationUserSchema





class ExercisesClient(APIClient):

    """Класс, предоставляющий методы для работы с эндпоинтами упражнений"""

    def get_exercises_api(self, query: GetExercisesQuerySchema) -> httpx.Response:
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

    def create_exercise_api(self, request: CreateExerciseRequestSchema) -> httpx.Response:
        """Метод создает упражнение

        :param request: Словарь, содержащий поля, необходимые для создания упражнения
        :return: Ответ от сервера в виде объекта httpx.Response."""
        return self.post("/api/v1/exercises", json=request.model_dump(by_alias=True))

    def update_exercise_api(self, exercise_id: str, exercise_data: UpdateExerciseRequestSchema) -> httpx.Response:
        """Метод, частично меняющий упражнение

        :param exercise_id: ID упражнения, которое нужно изменить
        :param exercise_data: Словарь, содержащий поля, подлежащие изменению
        :return: Ответ от сервера в виде объекта httpx.Response."""
        return self.patch(f"/api/v1/exercises/{exercise_id}", json=exercise_data.model_dump(by_alias=True))

    def delete_exercise_api(self, exercise_id: str) -> httpx.Response:
        """Метод удаляющий упражнение\

        :param exercise_id: ID упражнения, которое нужно удалить
        :return: Ответ от сервера в виде объекта httpx.Response.
        """
        return self.delete(f"/api/v1/exercises/{exercise_id}")

    def get_exercises(self, query: GetExercisesQuerySchema) -> GetExercisesResponseSchema:
        """
        Метод получает упражнения по конкретному курсу

        :param query: courseId курса, из которого мы будем получать упражнения
        :return: Сериализованный ответ по упражнениям из курса
        """
        response = self.get_exercises_api(query)
        return GetExercisesResponseSchema.model_validate_json(response.text)

    def get_exercise(self, exercise_id: str) -> GetExercisesResponseSchema:
        """
        Метод получающий информацию о конкретном упражнении

        :param exercise_id: ID упражнение
        :return: Сериализованный ответ по запрашиваемому упражнению
        """
        response = self.get_exercise_api(exercise_id=exercise_id)
        return GetExercisesResponseSchema.model_validate_json(response.text)

    def create_exercise(self, request: CreateExerciseRequestSchema) -> CreateExerciseResponseSchema:
        """
        Метод создающий упражнение

        :param request: Словарь, содержащий информацию для создания упражнения
        :return: Сериализованный ответ, содержащий информацию о созданном упражнении
        """
        response = self.create_exercise_api(request=request)
        return CreateExerciseResponseSchema.model_validate_json(response.text)

    def update_exercise(self, exercise_id: str, request: UpdateExerciseRequestSchema) -> UpdateExerciseResponseSchema:
        """
        Метод изменяющий информацию об упражнении

        :param exercise_id: ID упражнения
        :param request: Словарь, содержащий изменения
        :return: Сериализованный ответ, содержащий информацию об измененном упражнении
        """
        response = self.update_exercise_api(exercise_id=exercise_id, exercise_data=request)
        return UpdateExerciseResponseSchema.model_validate_json(response.text)

def get_exercises_client(user: AuthenticationUserSchema) -> ExercisesClient:
    """
        Функция создаёт экземпляр ExercisesClient с уже настроенным HTTP-клиентом.

        :return: Готовый к использованию ExercisesClient.
        """
    return ExercisesClient(get_private_http_client(user))

