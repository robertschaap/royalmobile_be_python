from flask import jsonify

class ApiResponse():
    @classmethod
    def success(self, data):
        return jsonify({
            'status': "success",
            'data': data,
            'message': None,
        })

    @classmethod
    def error(self, message):
        return jsonify({
            'status': "error",
            'data': None,
            'message': message,
        })
