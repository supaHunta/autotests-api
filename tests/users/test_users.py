from http import HTTPStatus

import faker
import pytest

from clients.users.public_users_client import PublicUsersClient
from clients.users.users_schema import GetUserResponseSchema, CreateUserRequestSchema, CreateUserResponseSchema
from tools.assertions.base import assert_status_code
from tools.assertions.schema import validate_json_schema
from tools.assertions.users import assert_get_user_response, assert_create_user_response
from tools.fakers import fake


@pytest.mark.users
@pytest.mark.regression
class TestUsers:

    @pytest.mark.parametrize("email",[
        "mail.ru",
        "gmail.com",
        "example.com"
    ])
    def test_create_user(self, email: str, public_users_client: PublicUsersClient):  # Используем фикстуру API клиента
        # Удалили инициализацию API клиента из теста
        request = CreateUserRequestSchema(email=fake.email(email))
        response = public_users_client.create_user_api(request)
        response_data = CreateUserResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_create_user_response(request, response_data)

        validate_json_schema(response.json(), response_data.model_json_schema())


    def test_get_user_me(self, function_user, private_users_client):
        user_response = private_users_client.get_user_me_api()
        user_me = GetUserResponseSchema.model_validate_json(user_response.text)

        assert_status_code(user_response.status_code, HTTPStatus.OK)
        assert_get_user_response(user_me, function_user.response)
        validate_json_schema(user_response.json(), user_me.model_json_schema())