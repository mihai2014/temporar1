# add new data to response header

from django.template.context_processors import csrf

class MyMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        response['X-My-Header'] = "my value"
        #response['X-CSRFToken'] = csrf(request)['csrf_token']
        #response['mode'] = 'same-origin' # Do not send CSRF token to another domain.        
        return response