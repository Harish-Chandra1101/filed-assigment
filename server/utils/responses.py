class GenericResponse:
    @staticmethod
    def get_success_response(data):
        return {
            'success': True,
            'errors': None,
            'data': data,
        }

    @staticmethod
    def get_error_response(msg: str):
        return {
            'success': False,
            'errors': [str(msg)],
            'data': {},
        }
