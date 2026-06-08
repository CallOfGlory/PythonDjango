from django.http import JsonResponse, HttpResponse, Http404
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
import json

data_dict = {}


def data_lookup(request, key):
    if key in data_dict:
        return JsonResponse({'key': key, 'value': data_dict[key]})
    raise Http404(f"Ключ '{key}' не знайдено")


@csrf_exempt
def update_data(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            data_dict.update(data)
            return JsonResponse({'status': 'success', 'updated': data})
        except json.JSONDecodeError:
            return JsonResponse({'status': 'error', 'message': 'Невірний JSON'}, status=400)
    return JsonResponse({'status': 'error', 'message': 'Потрібен POST запит'}, status=405)


def cached_data(request, item_id):
    data = {
        'item_id': item_id,
        'name': f'Item {item_id}',
        'description': f'Опис для елемента {item_id}'
    }
    return JsonResponse(data)


def restricted_area(request):
    return JsonResponse({'message': 'Ви увійшли до обмеженої зони'})


@csrf_exempt
def validate_json(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)

            normalized = {}

            for key, value in data.items():
                # Capitalize string values
                if isinstance(value, str):
                    normalized[key] = value.capitalize()
                # Convert string numbers to integers
                elif isinstance(value, str) and value.isdigit():
                    normalized[key] = int(value)
                else:
                    normalized[key] = value

            return JsonResponse(normalized)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Невірний JSON'}, status=400)
    return JsonResponse({'error': 'Потрібен POST запит'}, status=405)


def check_device(request):
    user_agent = request.META.get('HTTP_USER_AGENT', '').lower()

    mobile_keywords = ['mobile', 'android', 'iphone', 'ipad', 'ipod', 'blackberry', 'windows phone']

    if any(keyword in user_agent for keyword in mobile_keywords):
        return redirect('mobile_page')

    return HttpResponse("Ласкаво просимо на сайт!")


def mobile_page(request):
    return HttpResponse("Мобільна версія сайту")
