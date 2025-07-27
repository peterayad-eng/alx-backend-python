import logging
from datetime import datetime, time
from django.http import HttpResponseForbidden

logger = logging.getLogger(__name__)

class RequestLoggingMiddleware:
    """Middleware to log user requests"""
    def __init__(self, get_response):
        self.get_response = get_response
        # Configure logging
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

class RestrictAccessByTimeMiddleware:
    """
    Middleware that restricts chat access between 9 PM (21:00) and 6 AM (06:00)
    """

    def __init__(self, get_response):
        self.get_response = get_response
        self.restricted_start = time(21, 0)  # 9 PM
        self.restricted_end = time(6, 0)    # 6 AM

    def __call__(self, request):
        current_time = datetime.now().time()

        # Check if request is to chat endpoints during restricted hours
        if (request.path.startswith('/api/chats/') or
            request.path.startswith('/api/conversations/')):

            if self.restricted_end < current_time < self.restricted_start:
                return HttpResponseForbidden(
                    "Chat access is restricted between 9 PM and 6 AM"
                )

        return self.get_response(request)

