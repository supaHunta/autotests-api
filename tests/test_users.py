from http import HTTPStatus

import pytest

from clients.users.users_schema import GetUserResponseSchema
from tools.assertions.base import assert_status_code
from tools.assertions.schema import validate_json_schema
from tools.assertions.users import assert_get_user_response


@pytest.mark.regression
@pytest.mark.users
def test_get_user_me(function_user, private_users_client):
    user_response = private_users_client.get_user_me_api()
    user_me = GetUserResponseSchema.model_validate_json(user_response.text)

    assert_status_code(user_response.status_code, HTTPStatus.OK)
    assert_get_user_response(user_me, function_user.response)
    validate_json_schema(user_response.json(), user_me.model_json_schema())