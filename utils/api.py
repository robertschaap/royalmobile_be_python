from flask import jsonify

class ApiResponse():
    @classmethod
    def success(cls, data):
        """
        :return: `flask.Response` of passed data converted to JSON
        """
        return jsonify({
            'status': "success",
            'data': data,
            'message': None,
        })

    @classmethod
    def error(cls, message):
        """
        :return: `flask.Response` of passed error message converted to JSON
        """
        return jsonify({
            'status': "error",
            'data': None,
            'message': message,
        })
