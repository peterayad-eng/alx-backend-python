import logging
from datetime import datetime

class RequestLoggingMiddleware:
    """Middleware to log user requests"""
    def __init__(self, get_response =None):
        super().__init__(get_response)
        # Configure file logging
        logging.basicConfig(
            filename='requests.log',
            level=logging.INFO,
            format='%(asctime)s - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )

    def __call__(self, request):
        # Get user info (handle anonymous users)
        user = request.user.username if request.user.is_authenticated else 'Anonymous'
        logger.info(f"User: {user} - Path: {request.path} - Method: {request.method}")

        response = self.get_response(request)
        return response

