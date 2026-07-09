from http import HTTPStatus

import pytest

from clients.authentication.authentication_client import get_authentication_client
from clients.authentication.authentication_schema import LoginRequestSchema, LoginResponseSchema
from clients.users.public_users_client import get_public_users_client
from clients.users.users_schema import CreateUserRequestSchema
from tools.assertions.authetication import assert_login_response
from tools.assertions.base import assert_equal, assert_status_code
from tools.assertions.schema import validate_json_schema

@pytest.mark.regression
@pytest.mark.authentication
def test_login():
    public_users_client = get_public_users_client()
    authentication_client = get_authentication_client()

    new_user_request = CreateUserRequestSchema()
    public_users_client.create_user(new_user_request)

    login_response = authentication_client.login_api(
        LoginRequestSchema(
            email=new_user_request.email,
            password=new_user_request.password
        )
    )
    login_response_data = LoginResponseSchema.model_validate_json(login_response.text)

    assert_status_code(login_response.status_code, HTTPStatus.OK)
    assert_login_response(login_response_data)

    validate_json_schema(login_response.json(), LoginResponseSchema.model_json_schema())

