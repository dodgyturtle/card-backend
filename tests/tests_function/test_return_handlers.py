import pytest

from api_app.return_handlers import data_update_check, response_processing


@pytest.mark.parametrize(
    'error_code, data, expect_message',
    (
        ('00', None, {'code': '00', 'message': 'Ok', 'data': None}),
    )
)
def test_return_handlers(error_code, data, expect_message):
    assert response_processing(error_code, data) == expect_message


@pytest.mark.parametrize(
    'data_from_request, data_from_database, expect_result',
    (
        ({'code': '00'}, {'code': '00'}, True),
        ({'code': '01'}, {'code': '00'}, False),
        ({'code': '00', 'code1': '01'}, {'code': '00'}, False),
        ({'code': '00'}, {'code': '00', 'code1': '01'}, True),
        ({'id': 'id', 'code': '00', 'code1': '01'}, {'id': 'id2', 'code': '00', 'code1': '01'}, True),
    )
)
def test_data_update_check(data_from_request, data_from_database, expect_result):
    assert data_update_check(data_from_request, data_from_database) == expect_result
