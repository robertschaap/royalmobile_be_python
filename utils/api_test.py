from flask import Flask, jsonify
from utils.api import ApiResponse

app = Flask(__name__)

def test_should_return_json_success_response():
    with app.app_context():
        actual_result = ApiResponse.success("a_response").json

        expected_result = {
            'status': "success",
            'data': "a_response",
            'message': None,
        }

        assert actual_result == expected_result

def test_should_return_json_error_response():
    with app.app_context():
        actual_result = ApiResponse.error("a_message").json

        expected_result = {
            'status': "error",
            'data': None,
            'message': "a_message",
        }

        assert actual_result == expected_result
