from flask import jsonify

class ApiResponse():
    @classmethod
    def success(cls, data):
        return jsonify({
            'status': "success",
            'data': data,
            'message': None,
        })

    @classmethod
    def error(cls, message):
        return jsonify({
            'status': "error",
            'data': None,
            'message': message,
        })
