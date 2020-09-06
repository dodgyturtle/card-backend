import pytest

from api_app.return_handlers import response_processing

@pytest.mark.parametrize(
    'error_code, data, expect_message',
    (
        ('00', None, {'code': '00', 'message': 'Ok', 'data': None}),
    )
)
def test_return_handlers(error_code, data, expect_message):
    assert response_processing(error_code, data) == expect_message
