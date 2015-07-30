from django.utils.cache import add_never_cache_headers

class DisableStaffCachingMiddleware(object):
    def process_response(self, request, response):
        if hasattr(request, 'user') and request.user.is_staff:
            add_never_cache_headers(response)
        return response