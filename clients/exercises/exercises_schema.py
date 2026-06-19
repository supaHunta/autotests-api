from pydantic import BaseModel, Field, ConfigDict
from pydantic.alias_generators import to_camel


class GetExercisesQuerySchema(BaseModel):
    """
    Описание структуры запроса на получение списка заданий.
    """

    course_id: str = Field(alias="courseId")

class ExerciseSchema(BaseModel):
    """
    Описание структуры задания.
    """
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)

    id: str
    title: str
    course_id: str
    max_score: int | None
    min_score: int | None
    order_index: int
    description: str
    estimated_time: str | None

class GetExercisesResponseSchema(BaseModel):
    """
    Описание структуры ответа на запрос на получение списка заданий.
    """
    exercises: list[ExerciseSchema]

class GetExerciseResponseSchema(BaseModel):
    """
    Описание структуры запроса на получение задания.
    """
    exercise: ExerciseSchema

class CreateExerciseRequestSchema(BaseModel):
    """
    Описание структуры запроса на создание задания.
    """
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)

    title: str
    course_id: str
    max_score: int | None
    min_score: int | None
    order_index: int
    description: str
    estimated_time: str | None

class CreateExerciseResponseSchema(BaseModel):
    """
    Описание структуры ответа на запрос на создание задания.
    """
    exercise: ExerciseSchema

class UpdateExerciseRequestSchema(BaseModel):
    """
    Описание структуры запроса на обновление задания.
    """
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)

    title: str | None
    max_score: int | None
    min_score: int | None
    order_index: int | None
    description: str | None
    estimated_time: str | None

class UpdateExerciseResponseSchema(BaseModel):
    """
    Описание структуры ответа на запрос на обновление задания.
    """
    exercise: ExerciseSchema