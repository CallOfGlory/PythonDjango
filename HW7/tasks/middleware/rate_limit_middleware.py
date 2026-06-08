from django.http import JsonResponse
from django.core.cache import cache
from django.utils.deprecation import MiddlewareMixin
import time


class RateLimitMiddleware(MiddlewareMixin):
    def process_request(self, request):
        # Only apply to restricted-area endpoint
        if '/restricted-area/' in request.path:
            ip_address = self.get_client_ip(request)
            cache_key = f'rate_limit:{ip_address}:restricted-area'

            # Get request history
            request_times = cache.get(cache_key, [])
            current_time = time.time()

            # Filter requests from last minute
            request_times = [t for t in request_times if current_time - t < 60]

            # Check if limit exceeded
            if len(request_times) >= 5:
                return JsonResponse({
                    'error': 'Перевищено ліміт запитів',
                    'message': 'Максимум 5 запитів на хвилину'
                }, status=429)

            # Add current request
            request_times.append(current_time)
            cache.set(cache_key, request_times, timeout=60)

        return None

    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip
