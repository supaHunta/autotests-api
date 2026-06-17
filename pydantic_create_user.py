from pydantic import BaseModel, Field, EmailStr, ConfigDict
from pydantic.alias_generators import to_camel


class UserSchema(BaseModel):
    """
    Описание структуры пользователя
    """
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)


    id: str
    email: EmailStr
    last_name: str = Field(alias='lastName')
    first_name: str = Field(alias='firstName')
    middle_name: str = Field(alias='middleName')



class CreateUserRequestSchema(BaseModel):
    """
    Описание структуры запроса на создание пользователя
    """
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)

    email: EmailStr
    password: str
    last_name: str = Field(alias='lastName')
    first_name: str = Field(alias='firstName')
    middle_name: str = Field(alias='middleName')


class CreateUserResponseSchema(BaseModel):
    """
    Описание структуры ответа на запрос на создание пользователя
    """
    user: UserSchema