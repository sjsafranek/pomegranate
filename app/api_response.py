#!/usr/bin/python

class ApiResponseHandler(object):
    def __init__(self):
        self._name = "ApiResponseHandler"

    def unauthorized(self):
        return {
            "status": "fail",
            "data": {
                "error": "unauthorized"
            }
        }

    def not_authenticated(self):
        return {
            "status": "fail",
            "data": {
                "error": "please login"
            }
        }

    def ok(self):
        return {
            "status": "ok"
        }

    def method_not_allowed(self, provided_method, allowed_methods):
        return {
            "status": "fail",
            "data": {
                "error": "bad request",
                "provided_method": provided_method,
                "allowed_methods": allowed_methods
            }
        }

    def fatal(self, error):
        return {
            "status": "fail",
            "data": {
                "error": str(error)
            }
        }

ApiResponse = ApiResponseHandler()
