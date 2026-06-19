from pydantic import BaseModel, ConfigDict, Field
from pydantic.alias_generators import to_camel

from clients.files.files_schema import FileSchema
from clients.users.users_schema import UserSchema


class GetCoursesQuerySchema(BaseModel):
    """
    Описание структуры запроса на получение списка курсов.
    """
    user_id: str = Field(alias="userId")


class CourseSchema(BaseModel):
    """
    Описание структуры курса
    """
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)

    id: str
    title: str
    max_score: int | None
    min_score: int | None
    description: str
    preview_file: FileSchema
    estimatedTime: str | None
    created_by_user: UserSchema

class CreateCourseRequestSchema(BaseModel):
    """
    Описание структуры запроса на создание курса
    """
    model_config = ConfigDict(alias_generator=to_camel,populate_by_name=True)

    title: str
    max_score: int | None
    min_score: int | None
    description: str
    estimated_time: str | None
    preview_file_id: str
    created_by_user_id: str

class CreateCourseResponseSchema(BaseModel):
    """
    Описание структуры ответа на запрос на создание курса
    """

    course: CourseSchema

class UpdateCourseRequestSchema(BaseModel):
    """
    Описание структуры запроса на обновление курса
    """
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)

    title: str | None
    maxScore: int | None
    minScore: int | None
    description: str | None
    estimatedTime: str | None

class UpdateCourseResponseSchema(BaseModel):
    """
    Описание структуры ответа на запрос на обновление курса
    """

    course: CourseSchema

