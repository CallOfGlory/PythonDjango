from django.utils.deprecation import MiddlewareMixin
from django.core.cache import cache


class CustomCacheMiddleware(MiddlewareMixin):
    def process_request(self, request):
        # Check if this is a data/item/ endpoint
        if '/data/item/' in request.path:
            cache_key = f'cached_data:{request.path}'
            cached_response = cache.get(cache_key)

            if cached_response:
                return cached_response

            # Store request for later caching
            request._cache_key = cache_key

        return None

    def process_response(self, request, response):
        # Cache the response if it's a data/item/ endpoint
        if hasattr(request, '_cache_key') and response.status_code == 200:
            cache.set(request._cache_key, response, timeout=300)  # Cache for 5 minutes

        return response
