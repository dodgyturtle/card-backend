import api_app.settings_errors as errors

def response_processing(error_code: int, data: str = None):
    api_response = {
        'code': error_code,
        'message': errors.DECODING_CODES.get(error_code, errors.TEXT_IF_NO_CODE),
        'data': data,
    }
    return api_response

def data_update_check(data_from_request: dict, data_from_database: dict):
    raw_key = [key for key in data_from_request if (
        key !='id') and (
            data_from_database.get(key) != data_from_request.get(key))]
    print(data_from_request, data_from_database, raw_key)
    return True if not raw_key else False
